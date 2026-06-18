#!/usr/bin/env python3
"""Fetch papers from arXiv API for specified categories and date range."""

import argparse
import html
import json
import logging
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

import yaml

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

ARXIV_API_URL = "http://export.arxiv.org/api/query"
ARXIV_LIST_URL_TEMPLATE = "https://arxiv.org/list/{category}/pastweek?show=2000"
ATOM_NS = "{http://www.w3.org/2005/Atom}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"
DEFAULT_USER_AGENT = "DailyPaperBot/1.0 (Hermes Agent; research use)"


def _canonical_arxiv_id(arxiv_id: str) -> str:
    """Return arXiv ID without version suffix for de-duplicating sources.

    arXiv API entries normally include a version suffix (e.g. 2606.12397v1),
    while HTML list parsing yields the base ID (2606.12397).  The same paper can
    otherwise appear twice in one fetched file when one category falls back to
    HTML and another succeeds via the API.
    """
    return re.sub(r"v\d+$", "", arxiv_id.strip())


def load_config(config_path: str = None) -> dict:
    if config_path is None:
        config_path = Path(__file__).parent / "config.yaml"
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def _http_get(
    url: str,
    timeout: int,
    *,
    user_agent: str = DEFAULT_USER_AGENT,
    retries: int = 3,
    backoff_base: float = 5.0,
) -> str:
    """Fetch a URL with retry/backoff for transient and rate-limit failures."""
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url)
            req.add_header("User-Agent", user_agent)
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return response.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            last_error = e
            retriable = e.code in {429, 500, 502, 503, 504}
            if retriable and attempt < retries:
                wait_s = backoff_base * attempt
                logger.warning(
                    f"HTTP {e.code} for {url}; retrying in {wait_s:.1f}s "
                    f"({attempt}/{retries})"
                )
                time.sleep(wait_s)
                continue
            raise
        except (TimeoutError, urllib.error.URLError) as e:
            last_error = e
            if attempt < retries:
                wait_s = backoff_base * attempt
                logger.warning(
                    f"Transient fetch error for {url}: {e}; retrying in {wait_s:.1f}s "
                    f"({attempt}/{retries})"
                )
                time.sleep(wait_s)
                continue
            raise

    if last_error is not None:
        raise last_error
    raise RuntimeError(f"Failed to fetch URL: {url}")


def _strip_html(text: str) -> str:
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", text)).split())


def _extract_list_sections(list_html: str) -> list[tuple[datetime, str]]:
    """Return [(section_date, html_block)] from an arXiv list page."""
    parts = re.split(r"<h3>(.*?)</h3>", list_html, flags=re.S)
    sections = []
    for i in range(1, len(parts), 2):
        heading_html = parts[i]
        body_html = parts[i + 1] if i + 1 < len(parts) else ""
        heading_text = _strip_html(heading_html)
        m = re.search(r"([A-Z][a-z]{2},\s+\d{1,2}\s+[A-Z][a-z]{2}\s+\d{4})", heading_text)
        if not m:
            continue
        section_date = datetime.strptime(m.group(1), "%a, %d %b %Y")
        sections.append((section_date, body_html))
    return sections


def _extract_articles_from_list_section(
    section_html: str, category: str, updated_date: str
) -> list[dict]:
    """Parse arXiv /list HTML blocks into paper records without abstracts."""
    articles = []
    for dt_html, dd_html in re.findall(r"<dt>(.*?)</dt>\s*<dd>(.*?)</dd>", section_html, flags=re.S):
        id_match = re.search(r'href\s*=\s*"/abs/([^"?#]+)"', dt_html)
        if not id_match:
            continue
        arxiv_id = id_match.group(1).strip()

        title_match = re.search(
            r"list-title[^>]*>\s*<span[^>]*>Title:</span>\s*(.*?)\s*</div>",
            dd_html,
            flags=re.S,
        )
        title = _strip_html(title_match.group(1)) if title_match else arxiv_id

        authors_match = re.search(r"<div class='list-authors'>(.*?)</div>", dd_html, flags=re.S)
        authors = []
        if authors_match:
            authors = [
                _strip_html(a)
                for a in re.findall(r">([^<]+)</a>", authors_match.group(1), flags=re.S)
            ]

        comments_match = re.search(r"<div class='list-comments[^']*'>(.*?)</div>", dd_html, flags=re.S)
        comment = ""
        if comments_match:
            comment = _strip_html(comments_match.group(1)).removeprefix("Comments:").strip()

        subjects_match = re.search(r"<div class='list-subjects'>(.*?)</div>", dd_html, flags=re.S)
        categories = [category]
        if subjects_match:
            subjects_text = _strip_html(subjects_match.group(1)).removeprefix("Subjects:").strip()
            parsed_categories = re.findall(r"\(([A-Za-z0-9.\-]+)\)", subjects_text)
            if parsed_categories:
                categories = []
                for cat in parsed_categories:
                    if cat not in categories:
                        categories.append(cat)

        articles.append(
            {
                "arxiv_id": arxiv_id,
                "title": title,
                "abstract": "",
                "authors": authors,
                "affiliations": [],
                "comment": comment,
                "categories": categories,
                "published_date": updated_date,
                "updated_date": updated_date,
                "abs_url": f"https://arxiv.org/abs/{arxiv_id}",
                "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}.pdf",
            }
        )
    return articles


def _fetch_abstract_from_abs_page(
    arxiv_id: str,
    timeout: int,
    *,
    user_agent: str = DEFAULT_USER_AGENT,
    delay: float = 0.15,
) -> tuple[str, list[str], str]:
    """Fetch title/authors/abstract from the paper abstract page."""
    url = f"https://arxiv.org/abs/{arxiv_id}"
    page = _http_get(url, timeout=timeout, user_agent=user_agent, retries=3, backoff_base=2.0)

    def meta_one(name: str) -> str:
        m = re.search(
            rf'<meta\s+name="{re.escape(name)}"\s+content="(.*?)"\s*/?>',
            page,
            flags=re.S,
        )
        return html.unescape(m.group(1)).strip() if m else ""

    title = meta_one("citation_title")
    abstract = meta_one("citation_abstract")
    authors = [
        html.unescape(a).strip()
        for a in re.findall(
            r'<meta\s+name="citation_author"\s+content="(.*?)"\s*/?>',
            page,
            flags=re.S,
        )
        if a.strip()
    ]

    if delay > 0:
        time.sleep(delay)
    return title, authors, abstract


def _fetch_via_html_fallback(
    category: str,
    start_date: datetime,
    target: datetime,
    timeout: int,
    enrich_abstracts: bool = False,
) -> list[dict]:
    """Fallback when export.arxiv.org API is blocked or rate-limited."""
    list_url = ARXIV_LIST_URL_TEMPLATE.format(category=category)
    logger.warning(f"Falling back to arXiv HTML listing for {category}: {list_url}")
    list_html = _http_get(list_url, timeout=timeout, retries=3, backoff_base=2.0)

    candidates = []
    for section_date, section_html in _extract_list_sections(list_html):
        if section_date > target or section_date < start_date:
            continue
        updated_date = section_date.strftime("%Y-%m-%d")
        candidates.extend(_extract_articles_from_list_section(section_html, category, updated_date))

    logger.info(f"HTML fallback found {len(candidates)} candidate papers for {category}")

    if not enrich_abstracts:
        logger.info(
            "HTML fallback abstract enrichment disabled; returning list metadata only "
            f"for {len(candidates)} {category} papers"
        )
        return candidates

    enriched = []
    for idx, paper in enumerate(candidates, 1):
        try:
            title, authors, abstract = _fetch_abstract_from_abs_page(
                paper["arxiv_id"], timeout=timeout
            )
            if title:
                paper["title"] = title
            if authors:
                paper["authors"] = authors
            paper["abstract"] = abstract
        except Exception as e:
            logger.warning(f"Failed to enrich {paper['arxiv_id']} via abs page: {e}")

        if idx % 25 == 0:
            logger.info(f"  HTML fallback enriched {idx}/{len(candidates)} papers for {category}")
        enriched.append(paper)

    return enriched


def fetch_arxiv_papers(
    categories: list[str],
    date_str: str,
    max_results: int = 200,
    delay: float = 3.0,
    timeout: int = 30,
    days: int = 1,
) -> list[dict]:
    """Fetch papers from arXiv API.

    arXiv publishes new papers around 14:00 ET (18:00 UTC).
    The API's submittedDate range filter is unreliable, so we fetch
    the most recent papers sorted by submittedDate and filter locally.
    We use pagination to ensure we capture all papers for the target date range.

    Args:
        days: Number of days to fetch, counting back from date_str (inclusive).
              E.g. days=3 fetches [date_str-2, date_str-1, date_str].
    """
    target = datetime.strptime(date_str, "%Y-%m-%d")
    start_date = target - timedelta(days=days - 1)

    all_papers = {}  # arxiv_id -> paper dict (dedup across categories)
    api_failures = []

    for cat in categories:
        logger.info(f"Fetching category: {cat} for date {date_str}")

        start = 0
        passed_target_date = False
        used_fallback = False

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
                data = _http_get(
                    url,
                    timeout=timeout,
                    retries=3,
                    backoff_base=max(delay, 3.0),
                )
            except Exception as e:
                logger.error(f"Failed to fetch {cat} via API: {e}")
                api_failures.append((cat, str(e)))
                try:
                    fallback_papers = _fetch_via_html_fallback(
                        category=cat,
                        start_date=start_date,
                        target=target,
                        timeout=timeout,
                    )
                    for paper in fallback_papers:
                        arxiv_id = _canonical_arxiv_id(paper["arxiv_id"])
                        if arxiv_id in all_papers:
                            existing_cats = set(all_papers[arxiv_id]["categories"])
                            existing_cats.update(paper["categories"])
                            all_papers[arxiv_id]["categories"] = sorted(existing_cats)
                        else:
                            all_papers[arxiv_id] = paper
                    logger.info(f"  HTML fallback recovered {len(fallback_papers)} papers from {cat}")
                    used_fallback = True
                except Exception as fallback_error:
                    logger.error(f"HTML fallback failed for {cat}: {fallback_error}")
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
                elif ann_dt >= start_date:
                    # Paper falls within the target date range [start_date, target]
                    arxiv_id = _canonical_arxiv_id(paper["arxiv_id"])
                    if arxiv_id in all_papers:
                        existing_cats = set(all_papers[arxiv_id]["categories"])
                        existing_cats.update(paper["categories"])
                        all_papers[arxiv_id]["categories"] = sorted(existing_cats)
                    else:
                        all_papers[arxiv_id] = paper
                        count += 1
                else:
                    # Paper announced before start_date, we've passed the range
                    passed_target_date = True
                    break

            logger.info(f"  New papers from this page: {count}")

            # If we didn't pass the target date and exhausted this page, paginate
            if not passed_target_date and len(entries) == max_results:
                start += max_results
                time.sleep(delay)
            else:
                break

        if not used_fallback:
            logger.info(
                f"  Total new papers from {cat}: "
                f"{sum(1 for p in all_papers.values() if cat in p.get('categories', []))}"
            )
            time.sleep(delay)

    papers = list(all_papers.values())
    papers.sort(key=lambda p: p.get("updated_date", p["published_date"]), reverse=True)

    if not papers and api_failures:
        failure_summary = "; ".join(f"{cat}: {err}" for cat, err in api_failures)
        raise RuntimeError(f"All arXiv fetch attempts failed. {failure_summary}")

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
        upd_el = entry.find(f"{ATOM_NS}updated")
        updated_date = published_date
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
            "published_date": published_date,
            "updated_date": updated_date,
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
    parser.add_argument(
        "--days",
        type=int,
        default=1,
        help="Number of days to fetch back from --date (default: 1, i.e. single day)",
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
        days=args.days,
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
