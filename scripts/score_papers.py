#!/usr/bin/env python3
"""Four-layer scoring pipeline:
1. Keyword filter (discard irrelevant papers)
2. Keyword weighted scoring (base score)
3. Venue/Institution bonus (from comment & affiliations)
4. LLM fine scoring (optional, for papers above threshold)
"""

import argparse
import json
import logging
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml

# Zotero index for dedup
ZOTERO_INDEX = os.path.expanduser("~/Zotero/zotero_index.json")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)


def load_config(config_path: str = None) -> dict:
    if config_path is None:
        config_path = Path(__file__).parent / "config.yaml"
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def _text_blob(paper: dict) -> str:
    """Combine title + abstract into a lowercase searchable blob."""
    return (paper.get("title", "") + " " + paper.get("abstract", "")).lower()


def _keyword_in_text(keyword: str, text: str) -> bool:
    """Check if keyword appears in text (case-insensitive, word boundary aware)."""
    pattern = re.escape(keyword.lower())
    if len(keyword) <= 4:
        pattern = r"\b" + pattern + r"\b"
    return bool(re.search(pattern, text))


# ---- Layer 1: Keyword Filter ----

def filter_papers(papers: list[dict], config: dict) -> list[dict]:
    """Discard papers that match exclude keywords AND don't match any include keywords."""
    filter_cfg = config["scoring"]["filter"]
    exclude_kws = [kw.lower() for kw in filter_cfg["exclude_keywords"]]
    include_kws = [kw.lower() for kw in filter_cfg["include_keywords"]]

    kept = []
    for paper in papers:
        text = _text_blob(paper)

        has_include = any(_keyword_in_text(kw, text) for kw in include_kws)
        if has_include:
            kept.append(paper)
            continue

        has_exclude = any(_keyword_in_text(kw, text) for kw in exclude_kws)
        if has_exclude:
            logger.debug(f"Filtered out: {paper['title'][:80]}")
            continue

        kept.append(paper)

    logger.info(
        f"Filter: {len(papers)} -> {len(kept)} papers "
        f"({len(papers) - len(kept)} filtered out)"
    )
    return kept


# ---- Layer 2: Keyword Weighted Scoring ----

def keyword_score(paper: dict, config: dict) -> tuple[int, list[str]]:
    """Compute keyword-based score and return (score, matched_keywords)."""
    scoring_cfg = config["scoring"]
    high_weight = scoring_cfg["high_weight"]
    mid_weight = scoring_cfg["mid_weight"]
    low_weight = scoring_cfg["low_weight"]
    category_bonus = scoring_cfg.get("category_bonus", {})

    keyword_groups = [
        (scoring_cfg["keywords"]["high"], high_weight),
        (scoring_cfg["keywords"]["mid"], mid_weight),
        (scoring_cfg["keywords"]["low"], low_weight),
    ]

    text = _text_blob(paper)
    score = 0
    matched_keywords = []

    for keywords, weight in keyword_groups:
        for kw in keywords:
            if _keyword_in_text(kw, text):
                score += weight
                matched_keywords.append(kw)

    for cat in paper.get("categories", []):
        if cat in category_bonus:
            score += category_bonus[cat]

    return score, matched_keywords


# ---- Layer 3: Venue / Institution Bonus ----

def venue_institution_bonus(paper: dict, config: dict) -> tuple[int, str, list[str]]:
    """Compute bonus from venue (comment field) and institution (affiliations).

    Returns (bonus_score, matched_venue, matched_institutions).
    """
    scoring_cfg = config["scoring"]
    bonus = 0
    matched_venue = ""
    matched_institutions = []

    # --- Venue matching from arxiv comment ---
    comment = paper.get("comment", "")
    if comment:
        comment_lower = comment.lower()
        venue_bonus_cfg = scoring_cfg.get("venue_bonus", {})
        venue_keywords = scoring_cfg.get("venue_keywords", {})

        venue_found = False
        for tier in ["tier1", "tier2", "tier3"]:
            if venue_found:
                break
            tier_bonus = venue_bonus_cfg.get(tier, 0)
            for venue_kw in venue_keywords.get(tier, []):
                if venue_kw.lower() in comment_lower:
                    bonus += tier_bonus
                    matched_venue = venue_kw.strip()
                    venue_found = True
                    break

    # --- Institution matching from affiliations ---
    affiliations = paper.get("affiliations", [])
    if affiliations:
        aff_text = " ".join(affiliations).lower()
        inst_bonus_cfg = scoring_cfg.get("institution_bonus", {})
        inst_keywords = scoring_cfg.get("institution_keywords", {})

        best_inst_tier_bonus = 0
        for tier in ["tier1", "tier2"]:
            tier_bonus = inst_bonus_cfg.get(tier, 0)
            for inst_kw in inst_keywords.get(tier, []):
                if inst_kw.lower() in aff_text:
                    if inst_kw not in matched_institutions:
                        matched_institutions.append(inst_kw)
                    if tier_bonus > best_inst_tier_bonus:
                        best_inst_tier_bonus = tier_bonus

        bonus += best_inst_tier_bonus

    return bonus, matched_venue, matched_institutions


# ---- Layer 4: LLM Scoring ----

def llm_score_papers(papers: list[dict], config: dict) -> dict:
    """Call LLM scorer for papers above threshold. Returns {index: {score, comment}}."""
    from llm_scorer import score_papers_with_llm

    llm_cfg = config.get("llm", {})
    research_profile = config.get("research_profile", "")

    return score_papers_with_llm(
        papers,
        research_profile=research_profile,
        batch_size=llm_cfg.get("batch_size", 5),
        claude_command=llm_cfg.get("claude_command", "claude"),
        claude_flags=llm_cfg.get("claude_flags", "--permission-mode bypassPermissions --print"),
        model=llm_cfg.get("model", "sonnet"),
    )


# ---- Main Scoring Pipeline ----

def score_papers(papers: list[dict], config: dict, enable_llm: bool = True) -> list[dict]:
    """Full four-layer scoring pipeline."""
    comment_templates = config.get("comment_templates", {})
    llm_cfg = config.get("llm", {})
    llm_enabled = enable_llm and llm_cfg.get("enable_llm_scoring", False)
    llm_threshold = llm_cfg.get("llm_score_threshold", 10)

    scored = []
    for paper in papers:
        # Layer 2: keyword scoring
        kw_score, matched_keywords = keyword_score(paper, config)

        # Layer 3: venue/institution bonus
        vi_bonus, matched_venue, matched_institutions = venue_institution_bonus(paper, config)

        rule_score = min(kw_score + vi_bonus, 100)

        # Generate rule-based comment
        rule_comment = _generate_comment(matched_keywords, comment_templates)

        paper_scored = {
            **paper,
            "score": rule_score,
            "keyword_score": kw_score,
            "venue_bonus": vi_bonus,
            "matched_keywords": matched_keywords,
            "matched_venue": matched_venue,
            "matched_institutions": matched_institutions,
            "ai_comment": rule_comment,
            "llm_score": None,
            "llm_comment": None,
        }
        scored.append(paper_scored)

    # Layer 4: LLM scoring for papers above threshold
    if llm_enabled:
        llm_candidates = [
            (i, p) for i, p in enumerate(scored) if p["score"] >= llm_threshold
        ]

        if llm_candidates:
            logger.info(
                f"LLM scoring: {len(llm_candidates)} papers above threshold ({llm_threshold})"
            )
            candidate_papers = [p for _, p in llm_candidates]
            candidate_indices = [i for i, _ in llm_candidates]

            try:
                llm_results = llm_score_papers(candidate_papers, config)

                for batch_idx, global_idx in enumerate(candidate_indices):
                    if batch_idx in llm_results:
                        result = llm_results[batch_idx]
                        scored[global_idx]["llm_score"] = result["score"]
                        scored[global_idx]["llm_comment"] = result["comment"]
                        # Use LLM comment as ai_comment when available
                        scored[global_idx]["ai_comment"] = result["comment"]
                        # Blend: final score = 0.4 * rule + 0.6 * llm
                        rule_s = scored[global_idx]["score"]
                        llm_s = result["score"]
                        blended = int(0.4 * rule_s + 0.6 * llm_s)
                        scored[global_idx]["score"] = min(blended, 100)

                logger.info(f"LLM scoring applied to {len(llm_results)} papers")
            except Exception as e:
                logger.error(f"LLM scoring failed, falling back to rule scores: {e}")
        else:
            logger.info("No papers above LLM threshold, skipping LLM scoring")
    else:
        logger.info("LLM scoring disabled")

    # Zotero dedup: mark papers already in the library
    scored = _mark_zotero_duplicates(scored)

    # Sort by score descending, then by title
    scored.sort(key=lambda p: (-p["score"], p["title"]))
    logger.info(
        f"Scored {len(scored)} papers. "
        f"Top score: {scored[0]['score'] if scored else 0}"
    )
    return scored


def _mark_zotero_duplicates(papers: list[dict]) -> list[dict]:
    """Mark papers that already exist in the local Zotero library."""
    if not os.path.exists(ZOTERO_INDEX):
        logger.info("Zotero index not found, skipping dedup")
        for p in papers:
            p["in_zotero"] = False
            p["zotero_collections"] = []
        return papers

    try:
        with open(ZOTERO_INDEX, "r", encoding="utf-8") as f:
            zotero_papers = json.load(f)
    except Exception as e:
        logger.warning(f"Failed to load Zotero index: {e}")
        for p in papers:
            p["in_zotero"] = False
            p["zotero_collections"] = []
        return papers

    # Build lookup sets
    arxiv_ids = {}
    dois = {}
    titles = {}
    for zp in zotero_papers:
        if zp.get("arxiv_id"):
            arxiv_ids[zp["arxiv_id"]] = zp
        if zp.get("doi"):
            dois[zp["doi"].lower()] = zp
        if zp.get("title"):
            titles[zp["title"].lower().strip()] = zp

    dup_count = 0
    for p in papers:
        match = None
        # Check arXiv ID
        link = p.get("link", "")
        arxiv_id = None
        m = re.search(r"(\d{4}\.\d{4,5})", link)
        if m:
            arxiv_id = m.group(1)
        if arxiv_id and arxiv_id in arxiv_ids:
            match = arxiv_ids[arxiv_id]
        # Check DOI
        if not match and p.get("doi") and p["doi"].lower() in dois:
            match = dois[p["doi"].lower()]
        # Check title
        if not match and p.get("title") and p["title"].lower().strip() in titles:
            match = titles[p["title"].lower().strip()]

        if match:
            p["in_zotero"] = True
            p["zotero_collections"] = match.get("collections", [])
            dup_count += 1
        else:
            p["in_zotero"] = False
            p["zotero_collections"] = []

    logger.info(f"Zotero dedup: {dup_count}/{len(papers)} papers already in library")
    return papers


def _generate_comment(matched_keywords: list[str], templates: dict) -> str:
    """Generate a one-line AI comment based on matched keywords."""
    if not matched_keywords:
        return "General robotics/AI paper"

    for kw in matched_keywords:
        for template_key, template_text in templates.items():
            if template_key in kw or kw in template_key:
                return template_text

    areas = list(dict.fromkeys(matched_keywords[:3]))
    return f"Matches keywords: {', '.join(areas)}"


def main():
    parser = argparse.ArgumentParser(description="Score and filter arXiv papers")
    parser.add_argument("input", help="Input JSON file from fetch_papers.py")
    parser.add_argument("--config", type=str, default=None, help="Config file path")
    parser.add_argument(
        "--output", type=str, default=None, help="Output JSON path (default: stdout)"
    )
    parser.add_argument(
        "--no-llm", action="store_true", help="Disable LLM scoring"
    )
    args = parser.parse_args()

    config = load_config(args.config)

    with open(args.input, "r") as f:
        data = json.load(f)

    papers = data["papers"]
    logger.info(f"Loaded {len(papers)} papers from {args.input}")

    # Layer 1: filter
    filtered = filter_papers(papers, config)

    # Layers 2-4: score
    enable_llm = not args.no_llm
    scored = score_papers(filtered, config, enable_llm=enable_llm)

    output = {
        "date": data["date"],
        "fetch_time": data["fetch_time"],
        "score_time": datetime.utcnow().isoformat(),
        "total_fetched": data["total_papers"],
        "after_filter": len(filtered),
        "llm_scoring": enable_llm and config.get("llm", {}).get("enable_llm_scoring", False),
        "papers": scored,
    }

    json_str = json.dumps(output, ensure_ascii=False, indent=2)

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w") as f:
            f.write(json_str)
        logger.info(f"Saved {len(scored)} scored papers to {args.output}")
    else:
        print(json_str)


if __name__ == "__main__":
    main()
