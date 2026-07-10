from __future__ import annotations

import json
import sqlite3
import uuid
from dataclasses import asdict
from pathlib import Path
from typing import Any

from .identity import (
    canonical_arxiv_id,
    canonical_doi,
    identity_keys,
    normalize_title,
)
from .models import PaperRecord, ScoreResult


SCHEMA = """
CREATE TABLE IF NOT EXISTS papers (
  paper_id TEXT PRIMARY KEY,
  arxiv_id TEXT,
  doi TEXT,
  normalized_title TEXT NOT NULL,
  year INTEGER,
  record_json TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'candidate',
  first_seen_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_seen_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE UNIQUE INDEX IF NOT EXISTS papers_arxiv_unique
  ON papers(arxiv_id) WHERE arxiv_id <> '';
CREATE UNIQUE INDEX IF NOT EXISTS papers_doi_unique
  ON papers(doi) WHERE doi <> '';
CREATE INDEX IF NOT EXISTS papers_title_year
  ON papers(normalized_title, year);
CREATE TABLE IF NOT EXISTS paper_sources (
  paper_id TEXT NOT NULL REFERENCES papers(paper_id),
  source_name TEXT NOT NULL,
  source_record_id TEXT NOT NULL,
  raw_json TEXT NOT NULL,
  seen_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (paper_id, source_name, source_record_id)
);
CREATE TABLE IF NOT EXISTS score_evidence (
  paper_id TEXT NOT NULL REFERENCES papers(paper_id),
  scorer_version TEXT NOT NULL,
  total REAL NOT NULL,
  level TEXT NOT NULL,
  evidence_json TEXT NOT NULL,
  scored_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (paper_id, scorer_version)
);
CREATE TABLE IF NOT EXISTS ingestion_jobs (
  paper_id TEXT PRIMARY KEY REFERENCES papers(paper_id),
  stage TEXT NOT NULL,
  attempts INTEGER NOT NULL DEFAULT 0,
  last_error TEXT NOT NULL DEFAULT '',
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS citation_edges (
  citing_paper_id TEXT NOT NULL,
  cited_paper_id TEXT NOT NULL,
  source_name TEXT NOT NULL,
  PRIMARY KEY (citing_paper_id, cited_paper_id, source_name)
);
CREATE TABLE IF NOT EXISTS search_events (
  event_id TEXT PRIMARY KEY,
  query TEXT NOT NULL,
  scope TEXT NOT NULL,
  result_ids_json TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""


class PaperRepository:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as conn:
            conn.executescript(SCHEMA)

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def _find_existing(
        self, conn: sqlite3.Connection, paper: PaperRecord
    ) -> str | None:
        for kind, value in identity_keys(paper):
            if kind == "arxiv":
                row = conn.execute(
                    "SELECT paper_id FROM papers WHERE arxiv_id = ?", (value,)
                ).fetchone()
            elif kind == "doi":
                row = conn.execute(
                    "SELECT paper_id FROM papers WHERE doi = ?", (value,)
                ).fetchone()
            else:
                title, year = value.rsplit("|", 1)
                row = conn.execute(
                    "SELECT paper_id FROM papers "
                    "WHERE normalized_title = ? AND year = ?",
                    (title, int(year)),
                ).fetchone()
            if row:
                return str(row["paper_id"])
        return None

    def upsert(
        self, paper: PaperRecord, source_name: str, raw: dict[str, Any]
    ) -> str:
        paper.arxiv_id = canonical_arxiv_id(paper.arxiv_id)
        paper.doi = canonical_doi(paper.doi)
        paper.normalized_title = normalize_title(paper.title)
        with self._connect() as conn:
            paper_id = self._find_existing(conn, paper) or uuid.uuid4().hex
            paper.paper_id = paper_id
            payload = json.dumps(paper.to_mapping(), ensure_ascii=False)
            conn.execute(
                """INSERT INTO papers(
                       paper_id, arxiv_id, doi, normalized_title, year, record_json
                   ) VALUES (?, ?, ?, ?, ?, ?)
                   ON CONFLICT(paper_id) DO UPDATE SET
                     arxiv_id = CASE
                       WHEN excluded.arxiv_id <> '' THEN excluded.arxiv_id
                       ELSE papers.arxiv_id END,
                     doi = CASE
                       WHEN excluded.doi <> '' THEN excluded.doi
                       ELSE papers.doi END,
                     normalized_title = excluded.normalized_title,
                     year = COALESCE(excluded.year, papers.year),
                     record_json = excluded.record_json,
                     last_seen_at = CURRENT_TIMESTAMP""",
                (
                    paper_id,
                    paper.arxiv_id,
                    paper.doi,
                    paper.normalized_title,
                    paper.year,
                    payload,
                ),
            )
            source_record_id = (
                paper.arxiv_id
                or paper.doi
                or f"{paper.normalized_title}|{paper.year or ''}"
            )
            conn.execute(
                """INSERT INTO paper_sources(
                       paper_id, source_name, source_record_id, raw_json
                   ) VALUES (?, ?, ?, ?)
                   ON CONFLICT(paper_id, source_name, source_record_id)
                   DO UPDATE SET
                     raw_json = excluded.raw_json,
                     seen_at = CURRENT_TIMESTAMP""",
                (
                    paper_id,
                    source_name,
                    source_record_id,
                    json.dumps(raw, ensure_ascii=False),
                ),
            )
        return paper_id

    def count_papers(self) -> int:
        with self._connect() as conn:
            return int(conn.execute("SELECT COUNT(*) FROM papers").fetchone()[0])

    def get_record(self, paper_id: str) -> PaperRecord:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT record_json FROM papers WHERE paper_id = ?", (paper_id,)
            ).fetchone()
        if row is None:
            raise KeyError(paper_id)
        return PaperRecord.from_mapping(
            json.loads(row["record_json"]), source_name="sqlite"
        )

    def save_score(
        self, paper_id: str, result: ScoreResult, scorer_version: str
    ) -> None:
        evidence_json = json.dumps(
            asdict(result.evidence), ensure_ascii=False, sort_keys=True
        )
        with self._connect() as conn:
            conn.execute(
                """INSERT INTO score_evidence(
                       paper_id, scorer_version, total, level, evidence_json
                   ) VALUES (?, ?, ?, ?, ?)
                   ON CONFLICT(paper_id, scorer_version) DO UPDATE SET
                     total = excluded.total,
                     level = excluded.level,
                     evidence_json = excluded.evidence_json,
                     scored_at = CURRENT_TIMESTAMP""",
                (
                    paper_id,
                    scorer_version,
                    result.total,
                    result.level,
                    evidence_json,
                ),
            )

    def get_latest_score(self, paper_id: str) -> dict[str, Any]:
        with self._connect() as conn:
            row = conn.execute(
                """SELECT scorer_version, total, level, evidence_json, scored_at
                   FROM score_evidence
                   WHERE paper_id = ?
                   ORDER BY scored_at DESC
                   LIMIT 1""",
                (paper_id,),
            ).fetchone()
        if row is None:
            raise KeyError(paper_id)
        return {
            "scorer_version": row["scorer_version"],
            "total": row["total"],
            "level": row["level"],
            "evidence": json.loads(row["evidence_json"]),
            "scored_at": row["scored_at"],
        }
