#!/usr/bin/env python3
"""Add papers to Zotero library: download PDF, generate reading notes, write to SQLite DB."""

import argparse
import json
import logging
import os
import random
import re
import shutil
import sqlite3
import string
import subprocess
import sys
import textwrap
import urllib.request
from datetime import datetime
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────
ZOTERO_DIR = Path(os.path.expanduser("~/Zotero"))
ZOTERO_DB = ZOTERO_DIR / "zotero.sqlite"
ZOTERO_INDEX = ZOTERO_DIR / "zotero_index.json"
ZOTERO_STORAGE = ZOTERO_DIR / "storage"
DATA_DIR = Path(__file__).resolve().parent / "data"
NOTES_DIR = Path(__file__).resolve().parent.parent / "literature" / "notes"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

# ── Collection mapping ─────────────────────────────────────────────────
COLLECTION_RULES = [
    (r"wheeled[-\s]?leg|wheel[-\s]?leg|hybrid.locomotion", "Wheeled-Legged"),
    (r"humanoid", "Humanoid"),
    (r"quadruped", "Quadruped"),
    (r"terrain|parkour|climbing", "Terrain & Parkour"),
    (r"navigation|planning", "Navigation"),
    (r"perception|visual|lidar", "Perception"),
    (r"mpc|model.predictive", "MPC"),
    (r"sim[-\s]?2[-\s]?real|sim[-\s]?to[-\s]?real", "Sim2Real"),
    (r"teacher[-\s]?student|distillation", "Teacher-Student"),
]
DEFAULT_COLLECTION = "RSL"


def map_collection(paper: dict) -> str:
    """Determine best Zotero collection from matched_keywords, categories, and abstract."""
    text_parts = []
    if paper.get("matched_keywords"):
        text_parts.extend(paper["matched_keywords"])
    if paper.get("categories"):
        text_parts.extend(paper["categories"])
    if paper.get("abstract"):
        text_parts.append(paper["abstract"])
    if paper.get("title"):
        text_parts.append(paper["title"])
    blob = " ".join(text_parts).lower()
    for pattern, collection in COLLECTION_RULES:
        if re.search(pattern, blob, re.IGNORECASE):
            return collection
    return DEFAULT_COLLECTION


# ── Helpers ────────────────────────────────────────────────────────────
def gen_key(existing_keys: set) -> str:
    """Generate random 8-char uppercase alphanumeric key, avoiding conflicts."""
    chars = string.ascii_uppercase + string.digits
    for _ in range(1000):
        key = "".join(random.choices(chars, k=8))
        if key not in existing_keys:
            existing_keys.add(key)
            return key
    raise RuntimeError("Could not generate unique key")


def clean_title(title: str, max_len: int = 80) -> str:
    title = title[:max_len]
    title = re.sub(r"[^\w\s-]", "", title)
    title = re.sub(r"\s+", "_", title.strip())
    return title


def split_author(name: str) -> tuple:
    """Split 'First Middle Last' into (firstName, lastName)."""
    parts = name.strip().split()
    if len(parts) <= 1:
        return ("", name.strip())
    return (" ".join(parts[:-1]), parts[-1])


def load_index() -> list:
    if ZOTERO_INDEX.exists():
        return json.loads(ZOTERO_INDEX.read_text(encoding="utf-8"))
    return []


def save_index(index: list):
    ZOTERO_INDEX.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def check_duplicate(index: list, arxiv_id: str, doi: str | None = None) -> bool:
    for item in index:
        if item.get("arxiv_id") == arxiv_id:
            return True
        if doi and item.get("doi") and item["doi"] == doi:
            return True
    return False


# ── Paper resolution ───────────────────────────────────────────────────
def load_scored(date_str: str) -> list | None:
    """Load scored JSON for given date, fall back to fetched."""
    scored = DATA_DIR / f"{date_str}_scored.json"
    if scored.exists():
        return json.loads(scored.read_text(encoding="utf-8"))
    fetched = DATA_DIR / f"{date_str}_fetched.json"
    if fetched.exists():
        return json.loads(fetched.read_text(encoding="utf-8"))
    return None


def resolve_papers_by_date(date_str: str, items: list[int] | None, all_top: bool) -> list[dict]:
    """Resolve papers from daily report by index or top-5."""
    papers_data = load_scored(date_str)
    if not papers_data:
        logger.error(f"No data file found for {date_str}")
        sys.exit(1)

    # Sort by score descending (same as report generation)
    papers_data.sort(key=lambda p: p.get("score", 0), reverse=True)

    if all_top:
        return papers_data[:5]

    if items:
        result = []
        for idx in items:
            if 1 <= idx <= len(papers_data):
                result.append(papers_data[idx - 1])
            else:
                logger.warning(f"Index {idx} out of range (1-{len(papers_data)}), skipping")
        return result

    return []


def fetch_arxiv_metadata(arxiv_id: str) -> dict | None:
    """Fetch paper metadata from arXiv API."""
    import xml.etree.ElementTree as ET

    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "OpenClaw/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read().decode("utf-8")
        root = ET.fromstring(data)
        ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
        entry = root.find("atom:entry", ns)
        if entry is None:
            return None

        title = entry.findtext("atom:title", "", ns).strip().replace("\n", " ")
        abstract = entry.findtext("atom:summary", "", ns).strip().replace("\n", " ")
        published = entry.findtext("atom:published", "", ns)
        authors = [a.findtext("atom:name", "", ns) for a in entry.findall("atom:author", ns)]
        categories = []
        for c in entry.findall("atom:category", ns):
            t = c.get("term", "")
            if t:
                categories.append(t)
        for c in entry.findall("arxiv:primary_category", ns):
            t = c.get("term", "")
            if t and t not in categories:
                categories.insert(0, t)

        return {
            "arxiv_id": arxiv_id,
            "title": title,
            "abstract": abstract,
            "authors": authors,
            "categories": list(set(categories)),
            "published_date": published[:10] if published else "",
            "abs_url": f"https://arxiv.org/abs/{arxiv_id}",
            "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}.pdf",
        }
    except Exception as e:
        logger.error(f"Failed to fetch arXiv metadata for {arxiv_id}: {e}")
        return None


# ── Step 3: Download PDF ──────────────────────────────────────────────
def download_pdf(arxiv_id: str, storage_dir: Path, title: str) -> Path | None:
    """Download PDF to storage_dir, return path or None."""
    pdf_name = f"{clean_title(title)}.pdf"
    pdf_path = storage_dir / pdf_name
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    logger.info(f"Downloading PDF: {url}")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "OpenClaw/1.0"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            pdf_path.write_bytes(resp.read())
        logger.info(f"PDF saved: {pdf_path}")
        return pdf_path
    except Exception as e:
        logger.error(f"PDF download failed for {arxiv_id}: {e}")
        return None


# ── Step 4: Generate reading note ─────────────────────────────────────
NOTE_TEMPLATE = """\
<html>
<head><meta charset="utf-8"></head>
<body>
<h1>🤖 OpenClaw 深度精读笔记: {short_title}</h1>
<p><strong>日期:</strong> {today}</p>
<p><strong>arXiv:</strong> <a href="{abs_url}">{arxiv_id}</a></p>
<p><strong>Collection:</strong> {collection}</p>
<hr>
<h2>🔍 WHY：为什么要写这篇论文？(痛点)</h2>
<p>{abstract_first_sentence}</p>
<h2>💡 WHAT：它提出了什么？(本质)</h2>
<p>{abstract}</p>
<h2>📈 IMPACT：实验证明了什么？(价值)</h2>
<p>详见论文实验章节。</p>
<hr>
<p>📥 <i>Note generated by OpenClaw Agent (simplified).</i></p>
</body>
</html>"""

HTML_STRUCTURE = textwrap.dedent("""\
    <html>
    <head><meta charset="utf-8"></head>
    <body>
    <h1>🤖 OpenClaw 深度精读笔记: {short_title}</h1>
    <p><strong>日期:</strong> {today}</p>
    <p><strong>arXiv:</strong> <a href="{abs_url}">{arxiv_id}</a></p>
    <p><strong>Collection:</strong> {collection}</p>
    <hr>
    <h2>🔍 WHY：为什么要写这篇论文？(痛点)</h2>
    ...
    <h2>💡 WHAT：它提出了什么？(本质)</h2>
    ...
    <h2>🛠️ HOW：它是如何实现的？(机理)</h2>
    ...（含 reward 设计、网络结构、training trick——只要论文有）
    <h2>📈 IMPACT：实验证明了什么？(价值)</h2>
    ...（关键数值结果）
    <h2>⚠️ CRITICAL：局限与挑战 (反思)</h2>
    ...
    <h2>💎 与 OmniBot/RAL 的关联</h2>
    ...（这篇论文对轮足机器人 RL 运动控制 / RAL 论文有什么可借鉴之处）
    <hr>
    <p>📥 <i>Note generated by OpenClaw Agent.</i></p>
    </body>
    </html>""")


def generate_note_llm(paper: dict, collection: str, storage_dir: Path) -> Path | None:
    """Generate HTML reading note using claude CLI."""
    note_path = storage_dir / f"Notes_by_OpenClaw.html"
    short_title = paper["title"].split(":")[0][:40]
    today = datetime.now().strftime("%Y-%m-%d")
    ai_comment = paper.get("ai_comment") or paper.get("llm_comment") or ""

    prompt = (
        "读以下论文（标题+摘要），生成一份深度阅读笔记 HTML。\n"
        "只输出 HTML，不要 markdown 包裹，不要解释。\n\n"
        f"Title: {paper['title']}\n"
        f"Abstract: {paper.get('abstract', '')}\n"
        f"ArXiv: {paper.get('arxiv_id', '')}\n"
        f"Collection: {collection}\n"
        f"AI点评: {ai_comment}\n\n"
        f"笔记格式（严格遵循此结构）：\n{HTML_STRUCTURE}"
    ).replace("{short_title}", short_title).replace("{today}", today).replace(
        "{abs_url}", paper.get("abs_url", "")
    ).replace("{arxiv_id}", paper.get("arxiv_id", "")).replace("{collection}", collection)

    try:
        result = subprocess.run(
            ["claude", "--permission-mode", "bypassPermissions", "--print", "-p", prompt],
            capture_output=True, text=True, timeout=300,
        )
        if result.returncode == 0 and "<html" in result.stdout.lower():
            html = result.stdout.strip()
            # Strip markdown code fences if present
            html = re.sub(r"^```html?\s*\n?", "", html)
            html = re.sub(r"\n?```\s*$", "", html)
            note_path.write_text(html, encoding="utf-8")
            logger.info(f"LLM note generated: {note_path}")
            return note_path
        else:
            logger.warning(f"Claude CLI returned non-zero or no HTML, falling back to simple note")
            raise RuntimeError("claude output invalid")
    except Exception as e:
        logger.warning(f"Claude CLI failed ({e}), generating simplified note")
        return generate_note_simple(paper, collection, storage_dir)


def generate_note_simple(paper: dict, collection: str, storage_dir: Path) -> Path:
    """Fallback: generate simplified note from abstract."""
    note_path = storage_dir / f"Notes_by_OpenClaw.html"
    short_title = paper["title"].split(":")[0][:40]
    today = datetime.now().strftime("%Y-%m-%d")
    abstract = paper.get("abstract", "")
    first_sentence = abstract.split(". ")[0] + "." if ". " in abstract else abstract[:200]

    html = NOTE_TEMPLATE.format(
        short_title=short_title,
        today=today,
        abs_url=paper.get("abs_url", ""),
        arxiv_id=paper.get("arxiv_id", ""),
        collection=collection,
        abstract_first_sentence=first_sentence,
        abstract=abstract,
    )
    note_path.write_text(html, encoding="utf-8")
    logger.info(f"Simple note generated: {note_path}")
    return note_path


# ── Step 5: Write to Zotero SQLite ────────────────────────────────────
def write_to_zotero_db(paper: dict, collection_name: str, storage_key: str,
                       pdf_path: Path | None, note_path: Path | None,
                       existing_keys: set) -> int | None:
    """Insert paper into Zotero SQLite. Returns new itemID or None on failure."""
    db_backup = str(ZOTERO_DB) + ".openclaw.bak"
    shutil.copy(str(ZOTERO_DB), db_backup)
    logger.info(f"DB backup: {db_backup}")

    conn = sqlite3.connect(str(ZOTERO_DB))
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    cur = conn.cursor()

    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        arxiv_id = paper.get("arxiv_id", "")
        doi = f"10.48550/arXiv.{arxiv_id}" if arxiv_id else ""
        abs_url = paper.get("abs_url", f"https://arxiv.org/abs/{arxiv_id}")
        pub_date = paper.get("published_date", "")[:10]
        categories = paper.get("categories", [])
        primary_cat = categories[0] if categories else "cs.RO"

        # Look up IDs dynamically
        preprint_type_id = cur.execute(
            "SELECT itemTypeID FROM itemTypes WHERE typeName='preprint'"
        ).fetchone()[0]
        attachment_type_id = cur.execute(
            "SELECT itemTypeID FROM itemTypes WHERE typeName='attachment'"
        ).fetchone()[0]
        note_type_id = cur.execute(
            "SELECT itemTypeID FROM itemTypes WHERE typeName='note'"
        ).fetchone()[0]

        # Field IDs
        field_ids = {}
        for row in cur.execute("SELECT fieldID, fieldName FROM fields"):
            field_ids[row[1]] = row[0]

        # Get current max version
        max_version = cur.execute("SELECT MAX(version) FROM items").fetchone()[0] or 0

        conn.execute("BEGIN")

        # ── Insert main item ──
        item_key = gen_key(existing_keys)
        cur.execute(
            "INSERT INTO items (itemTypeID, dateAdded, dateModified, clientDateModified, "
            "libraryID, key, version, synced) VALUES (?,?,?,?,1,?,?,0)",
            (preprint_type_id, now, now, now, item_key, max_version + 1),
        )
        item_id = cur.lastrowid

        # ── Insert field values ──
        field_data = {
            "title": paper["title"],
            "abstractNote": paper.get("abstract", ""),
            "url": abs_url,
            "date": pub_date,
            "DOI": doi,
            "extra": f"arXiv:{arxiv_id} [{primary_cat}]",
            "libraryCatalog": "arXiv.org",
            "repository": "arXiv",
            "archiveID": f"arXiv:{arxiv_id}",
            "accessDate": now,
        }

        for field_name, value in field_data.items():
            if field_name not in field_ids or not value:
                continue
            fid = field_ids[field_name]
            # Check if value already exists in itemDataValues
            row = cur.execute(
                "SELECT valueID FROM itemDataValues WHERE value=?", (value,)
            ).fetchone()
            if row:
                vid = row[0]
            else:
                cur.execute("INSERT INTO itemDataValues (value) VALUES (?)", (value,))
                vid = cur.lastrowid
            cur.execute(
                "INSERT INTO itemData (itemID, fieldID, valueID) VALUES (?,?,?)",
                (item_id, fid, vid),
            )

        # ── Insert creators ──
        author_type_id = 8  # author
        authors = paper.get("authors", [])
        for idx, name in enumerate(authors):
            first, last = split_author(name)
            # Check if creator exists
            row = cur.execute(
                "SELECT creatorID FROM creators WHERE firstName=? AND lastName=? AND fieldMode=0",
                (first, last),
            ).fetchone()
            if row:
                creator_id = row[0]
            else:
                cur.execute(
                    "INSERT INTO creators (firstName, lastName, fieldMode) VALUES (?,?,0)",
                    (first, last),
                )
                creator_id = cur.lastrowid
            cur.execute(
                "INSERT INTO itemCreators (itemID, creatorID, creatorTypeID, orderIndex) "
                "VALUES (?,?,?,?)",
                (item_id, creator_id, author_type_id, idx),
            )

        # ── Insert collection association ──
        row = cur.execute(
            "SELECT collectionID FROM collections WHERE collectionName=? AND libraryID=1",
            (collection_name,),
        ).fetchone()
        if row:
            coll_id = row[0]
        else:
            # Create collection
            coll_key = gen_key(existing_keys)
            cur.execute(
                "INSERT INTO collections (collectionName, parentCollectionID, clientDateModified, "
                "libraryID, key, version, synced) VALUES (?,NULL,?,1,?,?,0)",
                (collection_name, now, coll_key, max_version + 2),
            )
            coll_id = cur.lastrowid
            logger.info(f"Created new collection: {collection_name} (ID={coll_id})")

        # Get next orderIndex for collection
        max_order = cur.execute(
            "SELECT MAX(orderIndex) FROM collectionItems WHERE collectionID=?", (coll_id,)
        ).fetchone()[0]
        next_order = (max_order or 0) + 1
        cur.execute(
            "INSERT INTO collectionItems (collectionID, itemID, orderIndex) VALUES (?,?,?)",
            (coll_id, item_id, next_order),
        )

        # ── Insert tags ──
        tag_names = [f"Computer Science - Robotics", "/unread"]
        for tname in tag_names:
            row = cur.execute("SELECT tagID FROM tags WHERE name=?", (tname,)).fetchone()
            if row:
                tag_id = row[0]
            else:
                cur.execute("INSERT INTO tags (name) VALUES (?)", (tname,))
                tag_id = cur.lastrowid
            cur.execute(
                "INSERT OR IGNORE INTO itemTags (itemID, tagID, type) VALUES (?,?,0)",
                (item_id, tag_id),
            )

        # ── Insert PDF attachment ──
        if pdf_path and pdf_path.exists():
            att_key = gen_key(existing_keys)
            cur.execute(
                "INSERT INTO items (itemTypeID, dateAdded, dateModified, clientDateModified, "
                "libraryID, key, version, synced) VALUES (?,?,?,?,1,?,?,0)",
                (attachment_type_id, now, now, now, att_key, max_version + 3),
            )
            att_id = cur.lastrowid
            cur.execute(
                "INSERT INTO itemAttachments (itemID, parentItemID, linkMode, contentType, path, syncState) "
                "VALUES (?,?,1,?,?,0)",
                (att_id, item_id, "application/pdf", f"storage:{pdf_path.name}"),
            )

        # ── Insert HTML note attachment ──
        if note_path and note_path.exists():
            note_att_key = gen_key(existing_keys)
            cur.execute(
                "INSERT INTO items (itemTypeID, dateAdded, dateModified, clientDateModified, "
                "libraryID, key, version, synced) VALUES (?,?,?,?,1,?,?,0)",
                (attachment_type_id, now, now, now, note_att_key, max_version + 4),
            )
            note_att_id = cur.lastrowid
            cur.execute(
                "INSERT INTO itemAttachments (itemID, parentItemID, linkMode, contentType, path, syncState) "
                "VALUES (?,?,1,?,?,0)",
                (note_att_id, item_id, "text/html", f"storage:Notes_by_OpenClaw.html"),
            )

        conn.commit()
        logger.info(f"DB write successful: itemID={item_id}, key={item_key}")
        return item_id

    except Exception as e:
        conn.rollback()
        logger.error(f"DB write failed, rolled back: {e}")
        # Restore backup
        shutil.copy(db_backup, str(ZOTERO_DB))
        logger.info("Restored DB from backup")
        return None
    finally:
        conn.close()


# ── Main processing ───────────────────────────────────────────────────
def process_paper(paper: dict, index: list, existing_keys: set, no_db_write: bool = False) -> dict | None:
    """Process a single paper through all steps. Returns index entry or None."""
    arxiv_id = paper.get("arxiv_id", "")
    doi = f"10.48550/arXiv.{arxiv_id}" if arxiv_id else None
    title = paper.get("title", "Unknown")

    # Step 1: Dedup
    if check_duplicate(index, arxiv_id, doi):
        logger.info(f"⏭️  Already in library: {title[:60]}")
        print(f"⏭️  已存在，跳过: {title[:60]}")
        return None

    # Step 2: Determine collection
    collection = map_collection(paper)
    logger.info(f"📁 Collection: {collection}")

    # Step 3: Download PDF
    storage_key = gen_key(existing_keys)
    storage_dir = ZOTERO_STORAGE / storage_key
    storage_dir.mkdir(parents=True, exist_ok=True)

    pdf_path = download_pdf(arxiv_id, storage_dir, title)

    # Step 4: Generate note
    note_path = generate_note_llm(paper, collection, storage_dir)

    if no_db_write:
        print(f"🔍 [DRY RUN] Would add: {title[:60]}")
        print(f"   📁 Collection: {collection}")
        if pdf_path:
            print(f"   📄 PDF: {pdf_path}")
        if note_path:
            print(f"   📝 Note: {note_path}")
        print(f"   🔑 Storage Key: {storage_key}")
        return {"dry_run": True}

    # Step 5: Write to Zotero DB
    item_id = write_to_zotero_db(paper, collection, storage_key, pdf_path, note_path, existing_keys)
    if item_id is None:
        return None

    # Step 6: Update index
    abs_url = paper.get("abs_url", f"https://arxiv.org/abs/{arxiv_id}")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {
        "itemID": item_id,
        "type": "preprint",
        "title": title,
        "doi": doi or "",
        "url": abs_url,
        "arxiv_id": arxiv_id,
        "collections": [collection],
        "tags": ["Computer Science - Robotics", "/unread"],
        "dateAdded": now,
        "abstract": paper.get("abstract", "")[:200],
    }
    index.append(entry)
    save_index(index)

    # Step 7: Report
    print(f"✅ 已入库: {title[:60]}")
    print(f"   📁 Collection: {collection}")
    if pdf_path:
        print(f"   📄 PDF: {pdf_path}")
    if note_path:
        print(f"   📝 Note: {note_path}")
    print(f"   🔑 Zotero Key: {storage_key}")

    return entry


def get_existing_keys() -> set:
    """Load all existing storage keys from Zotero."""
    keys = set()
    if ZOTERO_STORAGE.exists():
        for d in ZOTERO_STORAGE.iterdir():
            if d.is_dir():
                keys.add(d.name)
    # Also get keys from DB
    if ZOTERO_DB.exists():
        try:
            conn = sqlite3.connect(str(ZOTERO_DB))
            for row in conn.execute("SELECT key FROM items"):
                keys.add(row[0])
            conn.close()
        except Exception:
            pass
    return keys


def main():
    parser = argparse.ArgumentParser(description="Add papers to Zotero library")
    parser.add_argument("--date", help="Date of daily report (YYYY-MM-DD)")
    parser.add_argument("--items", help="Comma-separated item indices from daily report (1-based)")
    parser.add_argument("--arxiv", nargs="+", help="arXiv IDs to add directly")
    parser.add_argument("--all-top", action="store_true", help="Add all Top 5 papers from daily report")
    parser.add_argument("--no-db-write", action="store_true", help="Dry run: skip DB write and index update")
    args = parser.parse_args()

    if not args.date and not args.arxiv:
        parser.error("Must specify --date or --arxiv")
    if args.date and not args.items and not args.all_top and not args.arxiv:
        parser.error("With --date, must specify --items or --all-top")

    index = load_index()
    existing_keys = get_existing_keys()
    papers = []

    # Resolve papers from date + items
    if args.date and (args.items or args.all_top):
        item_indices = None
        if args.items:
            item_indices = [int(x.strip()) for x in args.items.split(",")]
        papers.extend(resolve_papers_by_date(args.date, item_indices, args.all_top))

    # Resolve papers from arxiv IDs
    if args.arxiv:
        for aid in args.arxiv:
            aid = aid.strip().replace("arxiv:", "").replace("arXiv:", "")
            meta = fetch_arxiv_metadata(aid)
            if meta:
                papers.append(meta)
            else:
                logger.error(f"Could not fetch metadata for {aid}")

    if not papers:
        logger.error("No papers to process")
        sys.exit(1)

    logger.info(f"Processing {len(papers)} paper(s)...")
    added = 0
    for paper in papers:
        result = process_paper(paper, index, existing_keys, args.no_db_write)
        if result:
            added += 1

    print(f"\n{'='*50}")
    print(f"完成: {added}/{len(papers)} 篇论文已处理")


if __name__ == "__main__":
    main()
