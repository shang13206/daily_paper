#!/usr/bin/env python3
"""Fetch papers from arXiv API for specified categories and date range."""

import argparse
import json
import logging
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

import yaml

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

ARXIV_API_URL = "http://export.arxiv.org/api/query"
ATOM_NS = "{http://www.w3.org/2005/Atom}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"


def load_config(config_path: str = None) -> dict:
    if config_path is None:
        config_path = Path(__file__).parent / "config.yaml"
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def fetch_arxiv_papers(
    categories: list[str],
    date_str: str,
    max_results: int = 200,
    delay: float = 3.0,
    timeout: int = 30,
) -> list[dict]:
    """Fetch papers from arXiv API.

    arXiv publishes new papers around 14:00 ET (18:00 UTC).
    The API's submittedDate range filter is unreliable, so we fetch
    the most recent papers sorted by submittedDate and filter locally.
    We use pagination to ensure we capture all papers for the target date.
    """
    target = datetime.strptime(date_str, "%Y-%m-%d")

    all_papers = {}  # arxiv_id -> paper dict (dedup across categories)

    for cat in categories:
        logger.info(f"Fetching category: {cat} for date {date_str}")

        start = 0
        found_target_date = False
        passed_target_date = False

        while not passed_target_date:
            query = f"cat:{cat}"
            params = {
                "search_query": query,
                "start": start,
                "max_results": max_results,
                "sortBy": "submittedDate",
                "sortOrder": "descending",
            }

            url = f"{ARXIV_API_URL}?{urllib.parse.urlencode(params)}"
            logger.info(f"Requesting: {url}")

            try:
                req = urllib.request.Request(url)
                req.add_header("User-Agent", "DailyPaperBot/1.0")
                with urllib.request.urlopen(req, timeout=timeout) as response:
                    data = response.read().decode("utf-8")
            except Exception as e:
                logger.error(f"Failed to fetch {cat}: {e}")
                break

            try:
                root = ET.fromstring(data)
            except ET.ParseError as e:
                logger.error(f"Failed to parse XML for {cat}: {e}")
                break

            entries = root.findall(f"{ATOM_NS}entry")
            logger.info(f"  Got {len(entries)} entries (start={start})")

            if not entries:
                break

            count = 0
            for entry in entries:
                paper = _parse_entry(entry)
                if paper is None:
                    continue

                # Use updated_date (announcement date) for filtering, not published_date.
                # arXiv sorts by submittedDate (≈ updated), so this is consistent.
                ann_date = paper.get("updated_date", paper["published_date"])[:10]
                try:
                    ann_dt = datetime.strptime(ann_date, "%Y-%m-%d")
                except ValueError:
                    continue

                if ann_dt > target:
                    # Paper announced after target date, skip but keep going
                    continue
                elif ann_dt == target:
                    found_target_date = True
                    arxiv_id = paper["arxiv_id"]
                    if arxiv_id in all_papers:
                        existing_cats = set(all_papers[arxiv_id]["categories"])
                        existing_cats.update(paper["categories"])
                        all_papers[arxiv_id]["categories"] = sorted(existing_cats)
                    else:
                        all_papers[arxiv_id] = paper
                        count += 1
                else:
                    # Paper announced before target date, we've passed it
                    passed_target_date = True
                    break

            logger.info(f"  New papers from this page: {count}")

            # If we didn't find target date and exhausted this page, paginate
            if not passed_target_date and len(entries) == max_results:
                start += max_results
                time.sleep(delay)
            else:
                break

        logger.info(f"  Total new papers from {cat}: {sum(1 for p in all_papers.values() if cat in p.get('categories', []))}")
        time.sleep(delay)

    papers = list(all_papers.values())
    # Sort by announcement date (updated_date), most recent first
    papers.sort(key=lambda p: p.get("updated_date", p["published_date"]), reverse=True)
    logger.info(f"Total unique papers fetched: {len(papers)}")
    return papers


def _parse_entry(entry: ET.Element) -> dict | None:
    """Parse a single Atom entry into a paper dict."""
    try:
        title_el = entry.find(f"{ATOM_NS}title")
        if title_el is None or title_el.text is None:
            return None
        title = " ".join(title_el.text.strip().split())

        # NOTE: Use 'updated' (announcement date) not 'published' (submission date).
        # A paper submitted on Monday may be announced on Wednesday; we want the
        # announcement date so that filtering by target date works correctly.

        abstract_el = entry.find(f"{ATOM_NS}summary")
        abstract = ""
        if abstract_el is not None and abstract_el.text:
            abstract = " ".join(abstract_el.text.strip().split())

        authors = []
        affiliations = []
        for author_el in entry.findall(f"{ATOM_NS}author"):
            name_el = author_el.find(f"{ATOM_NS}name")
            if name_el is not None and name_el.text:
                authors.append(name_el.text.strip())
            # Extract affiliation from arxiv:affiliation sub-element
            for aff_el in author_el.findall(f"{ARXIV_NS}affiliation"):
                if aff_el.text:
                    aff = aff_el.text.strip()
                    if aff and aff not in affiliations:
                        affiliations.append(aff)

        # Extract arxiv:comment field (often contains venue info)
        comment = ""
        comment_el = entry.find(f"{ARXIV_NS}comment")
        if comment_el is not None and comment_el.text:
            comment = " ".join(comment_el.text.strip().split())

        # Extract arxiv ID from the entry id URL
        id_el = entry.find(f"{ATOM_NS}id")
        if id_el is None or id_el.text is None:
            return None
        raw_id = id_el.text.strip()
        # e.g. http://arxiv.org/abs/2301.12345v1
        arxiv_id = raw_id.split("/abs/")[-1]

        # Categories
        categories = []
        for cat_el in entry.findall(f"{ARXIV_NS}primary_category"):
            term = cat_el.get("term")
            if term:
                categories.append(term)
        for cat_el in entry.findall(f"{ATOM_NS}category"):
            term = cat_el.get("term")
            if term and term not in categories:
                categories.append(term)

        # Published date (original submission date)
        pub_el = entry.find(f"{ATOM_NS}published")
        published_date = ""
        if pub_el is not None and pub_el.text:
            published_date = pub_el.text.strip()

        # Updated date (arXiv announcement / last-modified date).
        # This is the date arXiv made the paper publicly visible, which is what
        # we want to filter by (not the submission date).
        upd_el = entry.find(f"{ATOM_NS}updated")
        updated_date = published_date  # fallback to published if missing
        if upd_el is not None and upd_el.text:
            updated_date = upd_el.text.strip()

        # Links
        pdf_url = ""
        abs_url = f"https://arxiv.org/abs/{arxiv_id}"
        for link_el in entry.findall(f"{ATOM_NS}link"):
            if link_el.get("title") == "pdf":
                pdf_url = link_el.get("href", "")
        if not pdf_url:
            pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"

        return {
            "arxiv_id": arxiv_id,
            "title": title,
            "abstract": abstract,
            "authors": authors,
            "affiliations": affiliations,
            "comment": comment,
            "categories": categories,
            "published_date": published_date,  # original submission date
            "updated_date": updated_date,       # arXiv announcement date (used for filtering)
            "abs_url": abs_url,
            "pdf_url": pdf_url,
        }
    except Exception as e:
        logger.warning(f"Failed to parse entry: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(description="Fetch papers from arXiv")
    parser.add_argument(
        "--date",
        type=str,
        default=None,
        help="Target date YYYY-MM-DD (default: yesterday)",
    )
    parser.add_argument("--config", type=str, default=None, help="Config file path")
    parser.add_argument(
        "--output", type=str, default=None, help="Output JSON path (default: stdout)"
    )
    args = parser.parse_args()

    config = load_config(args.config)
    arxiv_cfg = config["arxiv"]

    if args.date is None:
        target_date = (datetime.utcnow() - timedelta(days=1)).strftime("%Y-%m-%d")
    else:
        target_date = args.date

    logger.info(f"Target date: {target_date}")

    papers = fetch_arxiv_papers(
        categories=arxiv_cfg["categories"],
        date_str=target_date,
        max_results=arxiv_cfg["max_results_per_category"],
        delay=arxiv_cfg["request_delay"],
        timeout=arxiv_cfg["timeout"],
    )

    output = {
        "date": target_date,
        "fetch_time": datetime.utcnow().isoformat(),
        "total_papers": len(papers),
        "papers": papers,
    }

    json_str = json.dumps(output, ensure_ascii=False, indent=2)

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w") as f:
            f.write(json_str)
        logger.info(f"Saved {len(papers)} papers to {args.output}")
    else:
        print(json_str)


if __name__ == "__main__":
    main()
