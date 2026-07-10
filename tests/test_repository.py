import sqlite3

from scripts.literature_core.models import PaperRecord, ScoreEvidence, ScoreResult
from scripts.literature_core.repository import PaperRepository


def test_upsert_reuses_paper_id_for_arxiv_versions(tmp_path):
    repo = PaperRepository(tmp_path / "literature.db")
    first = repo.upsert(
        PaperRecord(arxiv_id="2607.01234v1", title="Robot", year=2026),
        "arxiv",
        {"v": 1},
    )
    second = repo.upsert(
        PaperRecord(arxiv_id="2607.01234v3", title="Robot", year=2026),
        "arxiv",
        {"v": 3},
    )
    assert first == second
    assert repo.count_papers() == 1


def test_schema_and_score_round_trip(tmp_path):
    path = tmp_path / "literature.db"
    repo = PaperRepository(path)
    paper_id = repo.upsert(
        PaperRecord(title="Robot", year=2026), "fixture", {"id": 1}
    )
    evidence = ScoreEvidence(
        venue={"score": 0},
        institution={"score": 1},
        keywords=[],
        hardware={"score": 0},
        code={"score": 0},
        primary_cs_ro={"score": 0},
    )
    repo.save_score(
        paper_id,
        ScoreResult(total=1.0, level="filtered", evidence=evidence),
        "sop-v1",
    )

    assert repo.get_record(paper_id).title == "Robot"
    assert repo.get_latest_score(paper_id)["total"] == 1.0
    with sqlite3.connect(path) as conn:
        names = {
            row[0]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            )
        }
    assert {
        "papers",
        "paper_sources",
        "score_evidence",
        "ingestion_jobs",
        "citation_edges",
        "search_events",
    } <= names
