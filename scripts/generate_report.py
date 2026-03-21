#!/usr/bin/env python3
"""Generate daily paper report in Markdown format from scored papers."""

import argparse
import json
import logging
import sys
from datetime import datetime
from pathlib import Path

import yaml

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


def truncate_abstract(abstract: str, max_chars: int = 500) -> str:
    """Truncate abstract to max_chars, ending at a sentence boundary if possible."""
    if len(abstract) <= max_chars:
        return abstract
    truncated = abstract[:max_chars]
    # Try to end at a sentence
    last_period = truncated.rfind(".")
    if last_period > max_chars * 0.6:
        return truncated[: last_period + 1]
    return truncated.rstrip() + "..."


def generate_report(scored_data: dict, config: dict) -> str:
    """Generate Markdown report from scored paper data."""
    report_cfg = config["report"]
    top_n = report_cfg["top_n"]
    watch_threshold = report_cfg["watch_threshold"]

    date_str = scored_data["date"]
    papers = scored_data["papers"]
    total_fetched = scored_data["total_fetched"]
    after_filter = scored_data["after_filter"]
    llm_used = scored_data.get("llm_scoring", False)

    # Split into top papers and watch list
    top_papers = papers[:top_n]
    watch_papers = [p for p in papers[top_n:] if p["score"] >= watch_threshold]

    lines = []
    lines.append(f"# \U0001f916 具身智能/机器人学术日报 ({date_str})")
    lines.append("")

    # --- Top papers ---
    lines.append(f"## \U0001f3c6 精选论文 (Top {top_n})")
    lines.append("")

    if not top_papers:
        lines.append("_今日无相关精选论文_")
        lines.append("")
    else:
        for i, paper in enumerate(top_papers, 1):
            lines.append(f"### {i}. {paper['title']}")
            lines.append(f"- **Score:** {paper['score']}")
            cats_str = ", ".join(paper["categories"][:5])
            lines.append(f"- **Categories:** {cats_str}")
            # Venue info
            venue = paper.get("matched_venue", "")
            if venue:
                lines.append(f"- **Venue:** {venue}")
            # Institution info
            institutions = paper.get("matched_institutions", [])
            if institutions:
                lines.append(f"- **Institutions:** {', '.join(institutions)}")
            abstract = truncate_abstract(paper["abstract"])
            lines.append(f"- **Abstract:** {abstract}")
            if paper.get("ai_comment"):
                lines.append(f"- **AI 点评:** {paper['ai_comment']}")
            # Zotero badge
            if paper.get("in_zotero"):
                zot_cols = ", ".join(paper.get("zotero_collections", []))
                zot_note = f" (Collections: {zot_cols})" if zot_cols else ""
                lines.append(f"- 📚 **已在 Zotero 库中**{zot_note}")
            lines.append(
                f"- \U0001f4c4 [arXiv]({paper['abs_url']}) "
                f"| \U0001f4e5 [PDF]({paper['pdf_url']})"
            )
            lines.append("")
            lines.append("---")
            lines.append("")

    # --- Watch list ---
    lines.append(
        f"## \U0001f440 值得关注 (Score >= {watch_threshold} 的其余论文)"
    )
    lines.append("")

    if not watch_papers:
        lines.append("_今日无其他值得关注论文_")
        lines.append("")
    else:
        for paper in watch_papers:
            extra = ""
            venue = paper.get("matched_venue", "")
            if venue:
                extra += f" [{venue}]"
            institutions = paper.get("matched_institutions", [])
            if institutions:
                extra += f" ({', '.join(institutions[:2])})"
            zot_badge = " 📚" if paper.get("in_zotero") else ""
            lines.append(
                f"- **{paper['title']}** (Score: {paper['score']}){extra}{zot_badge} "
                f"[Link]({paper['abs_url']})"
            )
        lines.append("")

    # --- Statistics ---
    lines.append("## \U0001f4ca 今日统计")
    scoring_note = " (含 LLM 精筛)" if llm_used else ""
    zotero_count = sum(1 for p in papers if p.get("in_zotero"))
    zotero_note = f" | 已在 Zotero: {zotero_count} 篇" if zotero_count > 0 else ""
    lines.append(
        f"- 总抓取: {total_fetched} 篇 "
        f"| 通过初筛: {after_filter} 篇 "
        f"| 精选: {len(top_papers)} 篇{scoring_note}{zotero_note}"
    )
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate daily paper report")
    parser.add_argument("input", help="Input JSON file from score_papers.py")
    parser.add_argument("--config", type=str, default=None, help="Config file path")
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output markdown path (default: auto from config)",
    )
    args = parser.parse_args()

    config = load_config(args.config)

    with open(args.input, "r") as f:
        scored_data = json.load(f)

    logger.info(
        f"Loaded {len(scored_data['papers'])} scored papers for {scored_data['date']}"
    )

    report = generate_report(scored_data, config)

    if args.output:
        output_path = Path(args.output)
    else:
        repo_root = Path(__file__).parent.parent
        output_dir = repo_root / config["report"]["output_dir"]
        output_path = output_dir / f"{scored_data['date']}_Daily_Papers.md"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(report)

    logger.info(f"Report saved to {output_path}")


if __name__ == "__main__":
    main()
