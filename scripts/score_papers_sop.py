#!/usr/bin/env python3
"""Score fetched papers with the deterministic Paper Evaluation SOP."""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from literature_core.identity import canonical_arxiv_id, canonical_doi, normalize_title
from literature_core.models import PaperRecord, ScoreResult
from literature_core.repository import PaperRepository
from literature_core.sop import contains_term, score_paper


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_CONFIG = SCRIPT_DIR / "config.yaml"
DEFAULT_DATABASE = SCRIPT_DIR / "data" / "literature.db"
DEFAULT_INSTITUTION_SCORES = SCRIPT_DIR / "data" / "institution_scores.json"
DEFAULT_ZOTERO_INDEX = Path.home() / "Zotero" / "zotero_index.json"
URL_PATTERN = re.compile(r"https?://[^\s<>()\[\]{}]+", re.IGNORECASE)
CODE_HOSTS = ("github.com/", "gitlab.com/", "codeberg.org/")
LEVEL_ORDER = {"selected": 0, "watch": 1, "metadata_incomplete": 2, "filtered": 3}


def load_config(path: str | Path) -> dict[str, Any]:
    with Path(path).open(encoding="utf-8") as handle:
        config = yaml.safe_load(handle) or {}
    if "sop" not in config:
        raise ValueError("config is missing the required 'sop' section")
    return config


def load_institution_scores(
    path: str | Path, sop_config: dict[str, Any]
) -> dict[str, float]:
    institution = sop_config["institution"]
    scores = {
        str(name): float(institution["seed_score"])
        for name in institution.get("seed_names", [])
    }
    score_path = Path(path)
    if not score_path.exists():
        return scores
    try:
        payload = json.loads(score_path.read_text(encoding="utf-8"))
        if isinstance(payload, dict) and isinstance(payload.get("scores"), dict):
            payload = payload["scores"]
        if not isinstance(payload, dict):
            raise ValueError("institution score file must contain an object")
        scores.update({str(name): float(value) for name, value in payload.items()})
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        logger.warning("Ignoring invalid institution scores at %s: %s", score_path, exc)
    return scores


def _enrich_links(raw: dict[str, Any]) -> dict[str, Any]:
    enriched = dict(raw)
    if enriched.get("code_url"):
        return enriched
    text = " ".join(
        str(enriched.get(key) or "") for key in ("comment", "abstract")
    )
    urls = [url.rstrip(".,;:") for url in URL_PATTERN.findall(text)]
    enriched["code_url"] = next(
        (url for url in urls if any(host in url.casefold() for host in CODE_HOSTS)),
        "",
    )
    return enriched


def _load_zotero_identities(path: str | Path) -> tuple[set[str], set[str], set[str]]:
    index_path = Path(path)
    if not index_path.exists():
        return set(), set(), set()
    try:
        payload = json.loads(index_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        logger.warning("Ignoring unreadable Zotero index at %s: %s", index_path, exc)
        return set(), set(), set()
    if not isinstance(payload, list):
        return set(), set(), set()
    arxiv_ids = {
        canonical_arxiv_id(str(item.get("arxiv_id") or ""))
        for item in payload
        if isinstance(item, dict) and item.get("arxiv_id")
    }
    dois = {
        canonical_doi(str(item.get("doi") or ""))
        for item in payload
        if isinstance(item, dict) and item.get("doi")
    }
    titles = {
        normalize_title(str(item.get("title") or ""))
        for item in payload
        if isinstance(item, dict) and item.get("title")
    }
    return arxiv_ids, dois, titles


def _is_in_zotero(
    paper: PaperRecord, identities: tuple[set[str], set[str], set[str]]
) -> bool:
    arxiv_ids, dois, titles = identities
    return bool(
        (paper.arxiv_id and canonical_arxiv_id(paper.arxiv_id) in arxiv_ids)
        or (paper.doi and canonical_doi(paper.doi) in dois)
        or (paper.title and normalize_title(paper.title) in titles)
    )


def _is_domain_relevant(paper: PaperRecord, sop_config: dict[str, Any]) -> bool:
    gate = sop_config.get("domain_gate") or {}
    if gate.get("allow_primary_cs_ro", True) and paper.primary_category == "cs.RO":
        return True
    text = " ".join([paper.title, paper.abstract, paper.comment, paper.venue])
    return any(contains_term(str(term), text) for term in gate.get("terms", []))


def score_fetched_data(
    fetched: dict[str, Any],
    config: dict[str, Any],
    institution_scores: dict[str, float],
    repository: PaperRepository,
    zotero_identities: tuple[set[str], set[str], set[str]],
) -> dict[str, Any]:
    sop_config = config["sop"]
    scorer_version = str(sop_config["version"])
    papers: list[dict[str, Any]] = []

    for raw in fetched.get("papers") or []:
        source = _enrich_links(dict(raw))
        record = PaperRecord.from_mapping(source, source_name="arxiv")
        paper_id = repository.upsert(record, source_name="arxiv", raw=source)
        result = score_paper(record, sop_config, institution_scores)
        domain_relevant = _is_domain_relevant(record, sop_config)
        exclusion_reason = ""
        if not domain_relevant:
            result = ScoreResult(
                total=result.total,
                level="filtered",
                evidence=result.evidence,
            )
            exclusion_reason = "outside_robotics_domain"
        if not record.metadata_complete:
            result = ScoreResult(
                total=result.total,
                level="metadata_incomplete",
                evidence=result.evidence,
            )
            exclusion_reason = "metadata_incomplete"
        repository.save_score(paper_id, result, scorer_version)

        in_zotero = _is_in_zotero(record, zotero_identities)
        if result.level == "selected":
            ingestion_status = "complete" if in_zotero else "pending"
        else:
            ingestion_status = "not_applicable"

        evidence = asdict(result.evidence)
        papers.append(
            {
                **source,
                "paper_id": paper_id,
                "primary_category": record.primary_category,
                "code_url": record.code_url,
                "project_url": record.project_url,
                "score": result.total,
                "score_level": result.level,
                "score_evidence": evidence,
                "scorer_version": scorer_version,
                "domain_relevant": domain_relevant,
                "exclusion_reason": exclusion_reason,
                "matched_keywords": [item["term"] for item in evidence["keywords"]],
                "matched_venue": evidence["venue"].get("term", ""),
                "matched_institutions": (
                    [evidence["institution"]["name"]]
                    if evidence["institution"].get("name")
                    else []
                ),
                "in_zotero": in_zotero,
                "zotero_collections": [],
                "ingestion_status": ingestion_status,
            }
        )

    papers.sort(
        key=lambda paper: (
            LEVEL_ORDER.get(str(paper["score_level"]), 99),
            -float(paper["score"]),
            str(paper.get("title") or "").casefold(),
        )
    )
    counts = {
        level: sum(1 for paper in papers if paper["score_level"] == level)
        for level in LEVEL_ORDER
    }
    selected_count = counts["selected"]
    watch_count = counts["watch"]
    filtered_count = counts["filtered"]
    metadata_incomplete_count = counts["metadata_incomplete"]

    return {
        "date": fetched.get("date", ""),
        "fetch_time": fetched.get("fetch_time", ""),
        "score_time": datetime.now(timezone.utc).isoformat(),
        "scoring_mechanism": scorer_version,
        "llm_scoring": False,
        "total_fetched": int(fetched.get("total_papers", len(papers))),
        "after_filter": selected_count + watch_count,
        "selected_count": selected_count,
        "watch_count": watch_count,
        "filtered_count": filtered_count,
        "metadata_incomplete_count": metadata_incomplete_count,
        "papers": papers,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Score fetched papers with the deterministic Paper Evaluation SOP"
    )
    parser.add_argument("input", type=Path, help="JSON produced by fetch_papers.py")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    parser.add_argument(
        "--institution-scores", type=Path, default=DEFAULT_INSTITUTION_SCORES
    )
    parser.add_argument("--zotero-index", type=Path, default=DEFAULT_ZOTERO_INDEX)
    args = parser.parse_args()

    config = load_config(args.config)
    fetched = json.loads(args.input.read_text(encoding="utf-8"))
    institution_scores = load_institution_scores(args.institution_scores, config["sop"])
    repository = PaperRepository(args.database)
    zotero_identities = _load_zotero_identities(args.zotero_index)
    result = score_fetched_data(
        fetched,
        config,
        institution_scores,
        repository,
        zotero_identities,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    logger.info(
        "SOP scoring complete: selected=%d watch=%d filtered=%d metadata_incomplete=%d",
        result["selected_count"],
        result["watch_count"],
        result["filtered_count"],
        result["metadata_incomplete_count"],
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
