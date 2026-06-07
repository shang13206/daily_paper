#!/usr/bin/env python3
"""Add papers to Zotero library via Zotero Web API.
Writes items to api.zotero.org (syncs to Zotero client automatically).
PDFs stored to ~/OneDrive/Zotero/storage/{key}/.
API key read from ~/.zotero_api_key.
"""

import argparse
import json
import logging
import os
import re
import subprocess
import sys
import textwrap
import time
import urllib.request
import urllib.error
import urllib.parse
import pwd
from datetime import datetime
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────
# Hermes profile runs may set HOME to ~/.hermes/profiles/<profile>/home.
# Zotero data and the API key live in the real Unix account home.
REAL_HOME = Path(pwd.getpwuid(os.getuid()).pw_dir)
ZOTERO_DIR    = REAL_HOME / "Zotero"
ZOTERO_INDEX  = ZOTERO_DIR / "zotero_index.json"
ONEDRIVE_STORAGE = REAL_HOME / "OneDrive/Zotero/storage"
DATA_DIR      = Path(__file__).resolve().parent / "data"
API_KEY_FILE  = REAL_HOME / ".zotero_api_key"

# Zotero Web API
ZOTERO_USER_ID = 15343773
ZOTERO_API_BASE = f"https://api.zotero.org/users/{ZOTERO_USER_ID}"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

# ── Collection name → key mapping (fetched from API at runtime) ────────
_COLLECTION_CACHE: dict[str, str] = {}

# ── Collection rules ──────────────────────────────────────────────────
# Zotero classification is multi-label: platform + task/topic + method + source.
# IMPORTANT: RSL means ETH Robotic Systems Lab papers, not a generic inbox/default.
COLLECTION_RULES = [
    # Platform axis
    (r"wheeled[-\s]?leg|wheel[-\s]?leg|hybrid[ -]?locomotion|legged[-\s]?wheel", "Wheeled-Legged"),
    (r"humanoid|biped", "Humanoid"),
    (r"quadruped|legged robot|legged locomotion|unitree go2|anymal|go1\b|go2\b", "Quadruped"),
    (r"quadrotor|uav|aerial|drone", "Aerial"),

    # Task/topic axis
    (r"terrain|parkour|climb|rough[ -]?terrain|stairs|slope|obstacle", "Terrain & Parkour"),
    (r"navigat|path planning|motion planning|exploration|slam|locali[sz]ation|mapping", "Navigation"),
    (r"percept|visual|vision|lidar|depth|camera|heightmap|elevation map", "Perception"),
    (r"blind locomotion|exteroceptive-free|without vision|vision-free locomotion", "Blind Locomotion"),
    (r"state estimat|kalman|filtering|odometry|inertial|ekf|ukf", "State Estimation"),
    (r"representation|latent|memory|recurrent|gru|lstm|world model|terrain encoding|encoder|contrastive|self-supervised", "Memory & Representation"),

    # Method/control axis
    (r"mpc|model[ -]?predictive|predictive control|control barrier|\bcbf\b", "MPC"),
    (r"sim[-\s]?2[-\s]?real|sim[-\s]?to[-\s]?real|domain randomi[sz]ation|real[-\s]?world|sim2sim", "Sim2Real"),
    (r"teacher[-\s]?student|distillation|privileged", "Teacher-Student"),
    (r"motion prior|mimic|imitation|motion capture|mocap|diffusion", "Mimic & Motion Prior"),
    (r"gait|style reward|locomotion skill|walking|running", "Gait & Style"),
    (r"whole[-\s]?body|loco[-\s]?manipulation|manipulation", "Whole-Body Control"),
    (r"koopman", "Koopman"),
    (r"multi[-\s]?critic|critic", "Multi Critic"),
    (r"flow policy|normalizing flow", "Flow Policy"),
    (r"theory|theoretical|certified|guarantee|contraction", "Theory"),
    (r"vision[-\s]?language|\bvla\b|large vision-language|vlm", "VLA"),
]

SOURCE_RULES = [
    (r"science robotics", "Science Robotics"),
    (r"\bcoRL\b|conference on robot learning", "CoRL"),
    (r"\bicra\b", "ICRA"),
    (r"\bijrr\b|international journal of robotics research", "IJRR"),
    (r"\biros\b", "IROS"),
    (r"\bra-l\b|\bral\b|robotics and automation letters", "RAL"),
    (r"\brss\b|robotics: science and systems", "RSS"),
    (r"\btro\b|transactions on robotics", "TRO"),
]

RSL_RULE = r"\beth( zurich| zürich)?\b|robotic systems lab|\brsl\b|hutter|farshidian|bellicoso|fankhauser|miki|lee, joonho|rudin"
DEFAULT_COLLECTION = ""
NEEDS_REVIEW_TAG = "needs-review"


# ── API helpers ────────────────────────────────────────────────────────
def get_api_key() -> str:
    if API_KEY_FILE.exists():
        key = API_KEY_FILE.read_text().strip()
        if key:
            return key
    key = os.environ.get("ZOTERO_API_KEY", "")
    if key:
        return key
    raise RuntimeError(f"Zotero API key not found. Put it in {API_KEY_FILE} or set ZOTERO_API_KEY env var.")


def _request_with_retry(req: urllib.request.Request, timeout: int = 30,
                         max_retries: int = 3, backoff: float = 5.0) -> tuple[int, bytes]:
    """Execute a urllib request with retry on transient errors (timeout / 5xx).
    Returns (status_code, body_bytes). Raises on persistent failure.
    """
    last_exc = None
    for attempt in range(1, max_retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.status, resp.read()
        except urllib.error.HTTPError as e:
            if e.code < 500:
                raise  # 4xx — don't retry
            last_exc = e
            logger.warning(f"HTTP {e.code} on attempt {attempt}/{max_retries}, retrying in {backoff}s…")
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last_exc = e
            logger.warning(f"Network error on attempt {attempt}/{max_retries}: {e}, retrying in {backoff}s…")
        if attempt < max_retries:
            time.sleep(backoff)
            backoff *= 2  # exponential backoff
    raise last_exc  # propagate after all retries exhausted


def zotero_request(method: str, path: str, body=None, api_key: str = "") -> tuple[int, any]:
    """Make a Zotero Web API request (with retry on transient errors)."""
    url = ZOTERO_API_BASE + path
    data = json.dumps(body).encode() if body is not None else None
    headers = {
        "Zotero-API-Key": api_key,
        "Zotero-API-Version": "3",
        "Content-Type": "application/json",
        "User-Agent": "OpenClaw/1.0",
    }
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        status, body_bytes = _request_with_retry(req, timeout=30)
        body_str = body_bytes.decode()
        return status, json.loads(body_str) if body_str.strip() else {}
    except urllib.error.HTTPError as e:
        body_str = e.read().decode()
        logger.error(f"HTTP {e.code} for {method} {url}: {body_str[:200]}")
        return e.code, {}
    except Exception as e:
        logger.error(f"Request failed after retries: {method} {url}: {e}")
        return 0, {}


def fetch_collections(api_key: str) -> dict[str, str]:
    """Return {name: key} dict for all collections."""
    global _COLLECTION_CACHE
    if _COLLECTION_CACHE:
        return _COLLECTION_CACHE
    status, data = zotero_request("GET", "/collections?limit=100", api_key=api_key)
    if status == 200:
        _COLLECTION_CACHE = {c["data"]["name"]: c["key"] for c in data}
    return _COLLECTION_CACHE


# ── Collection mapping ─────────────────────────────────────────────────
def _paper_text(paper: dict) -> str:
    authors = paper.get("authors", [])
    author_text = " ".join(
        a if isinstance(a, str) else " ".join(str(v) for v in a.values())
        for a in authors
    )
    return " ".join([
        paper.get("title", ""),
        paper.get("abstract", ""),
        paper.get("comment", ""),
        paper.get("venue", ""),
        author_text,
        " ".join(paper.get("matched_keywords", [])),
        " ".join(paper.get("matched_institutions", [])),
        " ".join(paper.get("categories", [])),
    ])


def _append_unique(items: list[str], value: str):
    if value and value not in items:
        items.append(value)


def map_collections(paper: dict) -> list[str]:
    """Return ordered Zotero collection names for a paper.

    RSL is reserved for ETH Robotic Systems Lab papers. Empty result means
    "no confident collection"; callers should add NEEDS_REVIEW_TAG rather
    than falling back to RSL.
    """
    text = _paper_text(paper)
    collections: list[str] = []

    for pattern, collection in COLLECTION_RULES:
        if re.search(pattern, text, re.IGNORECASE):
            _append_unique(collections, collection)

    # Source/venue axis. Use venue/comment/matched_venue if available.
    source_text = " ".join([
        paper.get("venue", ""),
        paper.get("comment", ""),
        str(paper.get("matched_venue", "")),
    ])
    for pattern, collection in SOURCE_RULES:
        if re.search(pattern, source_text, re.IGNORECASE):
            _append_unique(collections, collection)

    # ETH RSL lab axis, not a default collection.
    if re.search(RSL_RULE, text, re.IGNORECASE):
        _append_unique(collections, "RSL")

    return collections


def map_collection(paper: dict) -> str:
    """Backward-compatible single-label mapper: first label or empty."""
    mapped = map_collections(paper)
    return mapped[0] if mapped else DEFAULT_COLLECTION


# ── Index helpers ──────────────────────────────────────────────────────
def load_index() -> list:
    if ZOTERO_INDEX.exists():
        return json.loads(ZOTERO_INDEX.read_text(encoding="utf-8"))
    return []


def save_index(index: list):
    ZOTERO_INDEX.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def check_duplicate(index: list, arxiv_id: str, doi: str = "") -> bool:
    clean_id = arxiv_id.replace("v1", "").replace("v2", "").replace("v3", "")
    for item in index:
        item_id = (item.get("arxiv_id") or "").replace("v1", "").replace("v2", "").replace("v3", "")
        if item_id == clean_id:
            return True
        if doi and item.get("doi") == doi:
            return True
    return False


# ── arXiv metadata ─────────────────────────────────────────────────────
def fetch_arxiv_metadata(arxiv_id: str) -> dict | None:
    import xml.etree.ElementTree as ET
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "OpenClaw/1.0"})
        _, body = _request_with_retry(req, timeout=30)
        data = body.decode("utf-8")
        root = ET.fromstring(data)
        ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
        entry = root.find("atom:entry", ns)
        if entry is None:
            return None
        title    = entry.findtext("atom:title", "", ns).strip().replace("\n", " ")
        abstract = entry.findtext("atom:summary", "", ns).strip().replace("\n", " ")
        published = entry.findtext("atom:published", "", ns)
        authors  = [a.findtext("atom:name", "", ns) for a in entry.findall("atom:author", ns)]
        comment  = entry.findtext("arxiv:comment", "", ns) or ""
        cats = [c.get("term", "") for c in entry.findall("atom:category", ns) if c.get("term")]

        # Try to extract venue from comment
        venue = ""
        for kw in ["ICRA", "IROS", "CoRL", "RSS", "RA-L", "RAL", "TRO", "IJRR", "Science Robotics", "NeurIPS", "ICLR"]:
            if kw.lower() in comment.lower():
                venue = kw
                break

        return {
            "arxiv_id": arxiv_id,
            "title": title,
            "abstract": abstract,
            "authors": authors,
            "categories": cats,
            "published_date": published[:10] if published else "",
            "abs_url": f"https://arxiv.org/abs/{arxiv_id}",
            "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}.pdf",
            "venue": venue,
            "comment": comment,
        }
    except Exception as e:
        logger.error(f"Failed to fetch arXiv metadata for {arxiv_id}: {e}")
        return None


# ── PDF download (OneDrive only) ──────────────────────────────────────
def download_pdf(pdf_url: str, storage_dir: Path, title: str) -> Path | None:
    """Download PDF to ~/OneDrive/Zotero/storage/{key}/ — no Zotero cloud upload."""
    safe = re.sub(r'[<>:"/\\|?*]', '', title)[:70].strip().replace(' ', '_')
    pdf_path = storage_dir / f"{safe}.pdf"

    # Try both bare URL and v1 variant
    urls_to_try = [pdf_url]
    # If URL ends with .pdf, also try inserting v1 before .pdf
    if pdf_url.endswith(".pdf") and "v1" not in pdf_url:
        urls_to_try.append(pdf_url.replace(".pdf", "v1.pdf"))

    for url in urls_to_try:
        logger.info(f"Downloading PDF: {url}")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            _, body = _request_with_retry(req, timeout=60, max_retries=3, backoff=5.0)
            if len(body) < 1000:
                logger.warning(f"Response too small ({len(body)}B), probably not a PDF — skipping")
                continue
            pdf_path.write_bytes(body)
            logger.info(f"PDF saved to OneDrive: {pdf_path} ({len(body)//1024} KB)")
            return pdf_path
        except Exception as e:
            logger.warning(f"PDF download failed ({url}): {e}")

    logger.error("All PDF download attempts failed")
    return None


# ── OneDrive sync helper ───────────────────────────────────────────────
def _sync_onedrive(local_dir: Path):
    """Trigger onedrive --synchronize for a specific directory after adding new files."""
    import subprocess, shutil
    if not shutil.which("onedrive"):
        return
    # Convert absolute path to relative OneDrive path
    try:
        onedrive_root = Path(os.path.expanduser("~/OneDrive"))
        rel = str(local_dir.relative_to(onedrive_root))
    except ValueError:
        return
    env = os.environ.copy()
    env["HTTPS_PROXY"] = "http://127.0.0.1:7897"
    env["HTTP_PROXY"] = "http://127.0.0.1:7897"
    logger.info(f"Triggering OneDrive sync for: {rel}")
    try:
        subprocess.run(
            ["onedrive", "--synchronize", "--single-directory", rel, "--resync"],
            env=env, timeout=120, capture_output=True
        )
        logger.info(f"OneDrive sync done: {rel}")
    except Exception as e:
        logger.warning(f"OneDrive sync failed (non-critical): {e}")


# ── Note generation ────────────────────────────────────────────────────
HTML_STRUCTURE = textwrap.dedent("""\
    <html>
    <head><meta charset="utf-8"></head>
    <body>
    <h1>🤖 OpenClaw 深度精读笔记: {short_title}</h1>
    <p><strong>日期:</strong> {today} | <strong>arXiv:</strong> <a href="{abs_url}">{arxiv_id}</a> | <strong>Collection:</strong> {collection}</p>
    <hr>
    <h2>🔍 WHY：为什么要写这篇论文？(痛点)</h2>
    ...
    <h2>💡 WHAT：它提出了什么？(本质)</h2>
    ...
    <h2>🛠️ HOW：它是如何实现的？(机理)</h2>
    ...（含 reward 设计、网络结构、training trick）
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


def generate_note(paper: dict, collection: str, storage_dir: Path) -> Path | None:
    note_path = storage_dir / "Notes_by_OpenClaw.html"
    short_title = paper["title"].split(":")[0][:40]
    today = datetime.now().strftime("%Y-%m-%d")
    abs_url = paper.get("abs_url", f"https://arxiv.org/abs/{paper.get('arxiv_id','')}")
    arxiv_id = paper.get("arxiv_id", "")
    ai_comment = paper.get("ai_comment") or paper.get("llm_comment") or ""

    prompt = (
        "读以下论文（标题+摘要），生成一份深度阅读笔记 HTML。\n"
        "只输出 HTML，不要 markdown 包裹，不要解释。\n\n"
        f"Title: {paper['title']}\n"
        f"Abstract: {paper.get('abstract', '')}\n"
        f"ArXiv: {arxiv_id}\n"
        f"Collection: {collection}\n"
        f"AI点评: {ai_comment}\n\n"
        f"笔记格式（严格遵循此结构）：\n"
        + HTML_STRUCTURE
            .replace("{short_title}", short_title)
            .replace("{today}", today)
            .replace("{abs_url}", abs_url)
            .replace("{arxiv_id}", arxiv_id)
            .replace("{collection}", collection)
    )

    try:
        result = subprocess.run(
            ["claude", "--permission-mode", "bypassPermissions", "--print", "-p", prompt],
            capture_output=True, text=True, timeout=300,
        )
        if result.returncode == 0 and "<html" in result.stdout.lower():
            html = result.stdout.strip()
            html = re.sub(r"^```html?\s*\n?", "", html)
            html = re.sub(r"\n?```\s*$", "", html)
            note_path.write_text(html, encoding="utf-8")
            logger.info(f"LLM note generated: {note_path}")
            return note_path
        else:
            raise RuntimeError("claude output invalid")
    except Exception as e:
        logger.warning(f"Claude CLI failed ({e}), using simple note")

    # Fallback: simple note
    first_sentence = paper.get("abstract", "")[:300]
    html = f"""<html><head><meta charset="utf-8"></head><body>
<h1>🤖 {paper['title']}</h1>
<p><strong>arXiv:</strong> <a href="{abs_url}">{arxiv_id}</a> | <strong>Collection:</strong> {collection}</p>
<p><strong>Date added:</strong> {today}</p>
<hr>
<h2>Abstract</h2><p>{first_sentence}...</p>
<h2>AI 点评</h2><p>{ai_comment}</p>
<hr><p><i>Note generated by OpenClaw (simplified).</i></p>
</body></html>"""
    note_path.write_text(html, encoding="utf-8")
    logger.info(f"Simple note generated: {note_path}")
    return note_path


# ── Paper resolution ───────────────────────────────────────────────────
def load_scored(date_str: str) -> list | None:
    scored = DATA_DIR / f"{date_str}_scored.json"
    if scored.exists():
        d = json.loads(scored.read_text())
        return d.get("papers", d) if isinstance(d, dict) else d
    fetched = DATA_DIR / f"{date_str}_fetched.json"
    if fetched.exists():
        d = json.loads(fetched.read_text())
        return d.get("papers", d) if isinstance(d, dict) else d
    return None


def resolve_papers_by_date(date_str: str, items: list[int] | None, all_top: bool) -> list[dict]:
    papers_data = load_scored(date_str)
    if not papers_data:
        logger.error(f"No data file found for {date_str}")
        sys.exit(1)
    papers_data.sort(key=lambda p: p.get("final_score", p.get("score", 0)), reverse=True)
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


# ── Main process_paper ─────────────────────────────────────────────────
def process_paper(paper: dict, index: list, api_key: str, dry_run: bool = False) -> dict | None:
    title    = paper.get("title", "").strip()
    arxiv_id = paper.get("arxiv_id", "").strip()
    if not title or not arxiv_id:
        logger.error("Paper missing title or arxiv_id, skipping.")
        return None

    # Dedup check
    if check_duplicate(index, arxiv_id):
        logger.info(f"[SKIP] Already in library: {title[:60]}")
        return None

    collection_names = map_collections(paper)
    collection_label = ", ".join(collection_names) if collection_names else "(none; needs review)"
    logger.info(f"📁 Collections: {collection_label}")

    if dry_run:
        logger.info(f"[DRY RUN] Would add: {title[:60]}")
        return {"title": title, "arxiv_id": arxiv_id, "collections": collection_names}

    # Fetch collection keys
    collections = fetch_collections(api_key)
    collection_keys = []
    for name in collection_names:
        key = collections.get(name)
        if key:
            collection_keys.append(key)
        else:
            logger.warning(f"Collection '{name}' not found, skipping it")

    # Build Zotero item
    authors = paper.get("authors", [])
    creators = []
    for a in authors:
        if isinstance(a, str):
            parts = a.strip().split()
            creators.append({
                "creatorType": "author",
                "firstName": " ".join(parts[:-1]) if len(parts) > 1 else "",
                "lastName": parts[-1] if parts else a,
            })
        elif isinstance(a, dict):
            creators.append({"creatorType": "author", **a})

    venue = paper.get("venue", "")
    extra_lines = [f"arXiv: {arxiv_id}"]
    if venue:
        extra_lines.append(f"PublicationType: {venue}")

    zotero_item = {
        "itemType": "preprint",
        "title": title,
        "creators": creators,
        "abstractNote": paper.get("abstract", ""),
        "repository": "arXiv",
        "archiveID": f"arXiv:{arxiv_id.replace('v1','').replace('v2','').replace('v3','')}",
        "url": paper.get("abs_url", f"https://arxiv.org/abs/{arxiv_id}"),
        "date": paper.get("published_date", paper.get("updated_date", "")),
        "extra": "\n".join(extra_lines),
        "collections": collection_keys,
    }

    # Write to Zotero Web API
    status, resp = zotero_request("POST", "/items", [zotero_item], api_key=api_key)
    if status != 200 or not resp.get("successful"):
        logger.error(f"Failed to add item: status={status} {str(resp)[:150]}")
        return None

    item_key = resp["successful"]["0"]["key"]
    logger.info(f"Zotero item created: key={item_key}")

    # Download PDF to ~/OneDrive/Zotero/storage/{key}/ (local only, no cloud upload)
    storage_dir = ONEDRIVE_STORAGE / item_key
    storage_dir.mkdir(parents=True, exist_ok=True)
    pdf_url = paper.get("pdf_url", f"https://arxiv.org/pdf/{arxiv_id}.pdf")
    pdf_path = download_pdf(pdf_url, storage_dir, title)

    # Register as linked_file attachment with portable relative path
    # Requires Zotero "Linked Attachment Base Directory" set to ~/OneDrive/Zotero (or Windows equivalent)
    if pdf_path and pdf_path.exists():
        rel_to_onedrive = pdf_path.relative_to(ONEDRIVE_STORAGE.parent)
        zotero_path = f"attachments:{rel_to_onedrive.as_posix()}"

        attach = {
            "itemType": "attachment",
            "parentItem": item_key,
            "linkMode": "linked_file",
            "title": pdf_path.stem[:60],
            "path": zotero_path,
            "contentType": "application/pdf",
            "collections": [],
        }
        a_status, a_resp = zotero_request("POST", "/items", [attach], api_key=api_key)
        if a_status == 200 and a_resp.get("successful"):
            logger.info(f"PDF linked_file attachment registered: {pdf_path.name}")
            _sync_onedrive(pdf_path.parent)
        else:
            logger.warning(f"PDF attachment registration failed: {a_status} {str(a_resp)[:100]}")
            logger.info(f"PDF still saved locally at: {pdf_path}")

    # Generate reading note
    note_path = generate_note(paper, collection_label, storage_dir)

    # Update local index
    entry = {
        "itemID": None,
        "key": item_key,
        "type": "preprint",
        "title": title,
        "doi": "",
        "url": zotero_item["url"],
        "arxiv_id": arxiv_id,
        "collections": collection_names,
        "tags": ["cs.RO", "/unread"] + ([] if collection_names else [NEEDS_REVIEW_TAG]),
        "dateAdded": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "abstract": paper.get("abstract", "")[:200],
        "venue": venue,
    }
    index.append(entry)
    save_index(index)

    print(f"✅ 已入库: {title[:60]}")
    print(f"   📁 Collections: {collection_label}")
    if pdf_path:
        print(f"   📄 PDF: {pdf_path}")
    if note_path:
        print(f"   📝 Note: {note_path}")
    print(f"   🔑 Zotero Key: {item_key}")

    return entry


# ── CLI ────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Add papers to Zotero library")
    parser.add_argument("--date",     help="Date of daily report (YYYY-MM-DD)")
    parser.add_argument("--items",    help="Comma-separated item indices from daily report (1-based)")
    parser.add_argument("--arxiv",    nargs="+", help="arXiv IDs to add directly")
    parser.add_argument("--all-top",  action="store_true", help="Add all Top 5 papers from daily report")
    parser.add_argument("--no-db-write", action="store_true", help="Dry run: skip write")
    args = parser.parse_args()

    if not args.date and not args.arxiv:
        parser.error("Must specify --date or --arxiv")

    api_key = get_api_key()
    index = load_index()
    papers = []

    if args.date:
        item_indices = [int(x.strip()) for x in args.items.split(",")] if args.items else None
        if item_indices or args.all_top:
            papers.extend(resolve_papers_by_date(args.date, item_indices, args.all_top))
        elif not args.arxiv:
            parser.error("With --date, must specify --items, --all-top, or --arxiv")

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
        result = process_paper(paper, index, api_key, dry_run=args.no_db_write)
        if result:
            added += 1

    print(f"\n{'='*50}")
    print(f"完成: {added}/{len(papers)} 篇论文已处理")


if __name__ == "__main__":
    main()
