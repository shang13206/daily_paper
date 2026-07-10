from __future__ import annotations

import re
import unicodedata

from .models import PaperRecord


def canonical_arxiv_id(value: str) -> str:
    normalized = value.strip().removeprefix("arXiv:").removeprefix("arxiv:")
    normalized = normalized.rsplit("/", 1)[-1]
    return re.sub(r"v\d+$", "", normalized)


def canonical_doi(value: str) -> str:
    normalized = value.strip().casefold()
    normalized = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", normalized)
    return normalized.removeprefix("doi:").strip()


def normalize_title(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).casefold()
    normalized = re.sub(r"[^\w\s]", " ", normalized, flags=re.UNICODE)
    return " ".join(normalized.split())


def identity_keys(paper: PaperRecord) -> list[tuple[str, str]]:
    keys: list[tuple[str, str]] = []
    arxiv_id = canonical_arxiv_id(paper.arxiv_id)
    doi = canonical_doi(paper.doi)
    title = normalize_title(paper.title)
    if arxiv_id:
        keys.append(("arxiv", arxiv_id))
    if doi:
        keys.append(("doi", doi))
    if title and paper.year is not None:
        keys.append(("title_year", f"{title}|{paper.year}"))
    return keys
