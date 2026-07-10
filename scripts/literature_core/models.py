from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(slots=True)
class PaperRecord:
    paper_id: str | None = None
    arxiv_id: str = ""
    doi: str = ""
    title: str = ""
    normalized_title: str = ""
    year: int | None = None
    abstract: str = ""
    authors: list[str] = field(default_factory=list)
    affiliations: list[str] = field(default_factory=list)
    categories: list[str] = field(default_factory=list)
    primary_category: str = ""
    venue: str = ""
    comment: str = ""
    abs_url: str = ""
    pdf_url: str = ""
    code_url: str = ""
    project_url: str = ""
    published_date: str = ""
    updated_date: str = ""
    metadata_complete: bool = True
    source_names: list[str] = field(default_factory=list)
    raw: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_mapping(cls, value: dict[str, Any], source_name: str) -> "PaperRecord":
        categories = list(value.get("categories") or [])
        published = str(value.get("published_date") or "")
        inferred_year = (
            int(published[:4])
            if len(published) >= 4 and published[:4].isdigit()
            else None
        )
        return cls(
            paper_id=value.get("paper_id"),
            arxiv_id=str(value.get("arxiv_id") or ""),
            doi=str(value.get("doi") or ""),
            title=str(value.get("title") or "").strip(),
            normalized_title=str(value.get("normalized_title") or ""),
            year=value.get("year", inferred_year),
            abstract=str(value.get("abstract") or "").strip(),
            authors=list(value.get("authors") or []),
            affiliations=list(value.get("affiliations") or []),
            categories=categories,
            primary_category=str(
                value.get("primary_category")
                or (categories[0] if categories else "")
            ),
            venue=str(value.get("venue") or value.get("matched_venue") or ""),
            comment=str(value.get("comment") or ""),
            abs_url=str(value.get("abs_url") or value.get("link") or ""),
            pdf_url=str(value.get("pdf_url") or ""),
            code_url=str(value.get("code_url") or ""),
            project_url=str(value.get("project_url") or ""),
            published_date=published,
            updated_date=str(value.get("updated_date") or ""),
            metadata_complete=bool(
                value.get("metadata_complete", value.get("abstract"))
            ),
            source_names=[source_name],
            raw=dict(value),
        )

    def to_mapping(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True, slots=True)
class ScoreEvidence:
    venue: dict[str, Any]
    institution: dict[str, Any]
    keywords: list[dict[str, Any]]
    hardware: dict[str, Any]
    code: dict[str, Any]
    primary_cs_ro: dict[str, Any]


@dataclass(frozen=True, slots=True)
class ScoreResult:
    total: float
    level: str
    evidence: ScoreEvidence
