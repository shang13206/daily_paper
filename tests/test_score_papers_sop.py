import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCORER = REPO_ROOT / "scripts" / "score_papers_sop.py"


def _fetched_payload() -> dict:
    return {
        "date": "2026-07-09",
        "fetch_time": "2026-07-10T00:00:00",
        "total_papers": 3,
        "papers": [
            {
                "arxiv_id": "2607.00001v1",
                "title": "Humanoid Locomotion on a Real Robot",
                "abstract": "A real robot is deployed on Unitree hardware.",
                "comment": "Accepted to ICRA 2026. Code: https://github.com/example/humanoid",
                "categories": ["cs.RO", "cs.AI"],
                "authors": ["A. Author"],
                "affiliations": [],
                "abs_url": "https://arxiv.org/abs/2607.00001v1",
                "pdf_url": "https://arxiv.org/pdf/2607.00001v1.pdf",
            },
            {
                "arxiv_id": "2607.00002v1",
                "title": "Robot Navigation in Warehouses",
                "abstract": "A robot navigation benchmark.",
                "comment": "",
                "categories": ["cs.RO"],
                "authors": ["B. Author"],
                "affiliations": [],
                "abs_url": "https://arxiv.org/abs/2607.00002v1",
                "pdf_url": "https://arxiv.org/pdf/2607.00002v1.pdf",
            },
            {
                "arxiv_id": "2607.00003v1",
                "title": "Ordinal Regression",
                "abstract": "A general rank estimation benchmark.",
                "comment": "Accepted to ICML 2026. Code: https://github.com/example/ranking",
                "categories": ["cs.LG"],
                "authors": ["C. Author"],
                "affiliations": [],
                "abs_url": "https://arxiv.org/abs/2607.00003v1",
                "pdf_url": "https://arxiv.org/pdf/2607.00003v1.pdf",
            },
        ],
    }


def test_cli_emits_sop_levels_evidence_and_counts(tmp_path):
    input_path = tmp_path / "fetched.json"
    output_path = tmp_path / "scored.json"
    database_path = tmp_path / "literature.db"
    input_path.write_text(json.dumps(_fetched_payload()), encoding="utf-8")

    subprocess.run(
        [
            sys.executable,
            str(SCORER),
            str(input_path),
            "--config",
            str(REPO_ROOT / "scripts" / "config.yaml"),
            "--output",
            str(output_path),
            "--database",
            str(database_path),
            "--zotero-index",
            str(tmp_path / "missing-zotero-index.json"),
        ],
        cwd=REPO_ROOT,
        check=True,
    )

    result = json.loads(output_path.read_text(encoding="utf-8"))
    assert result["scoring_mechanism"] == "paper-evaluation-sop-v1"
    assert result["selected_count"] == 1
    assert result["watch_count"] == 1
    assert result["filtered_count"] == 1
    assert result["after_filter"] == 2
    assert [paper["score_level"] for paper in result["papers"]] == [
        "selected",
        "watch",
        "filtered",
    ]

    selected = result["papers"][0]
    assert selected["score"] >= 8
    assert selected["score_evidence"]["venue"]["score"] == 10
    assert selected["score_evidence"]["hardware"]["score"] == 4
    assert selected["score_evidence"]["code"]["score"] == 3
    assert selected["ingestion_status"] == "pending"
    assert selected["paper_id"]
    assert database_path.exists()

    unrelated = result["papers"][2]
    assert unrelated["score"] >= 8
    assert unrelated["score_level"] == "filtered"
    assert unrelated["domain_relevant"] is False
    assert unrelated["exclusion_reason"] == "outside_robotics_domain"


def test_daily_entrypoint_invokes_sop_scorer():
    runner = (REPO_ROOT / "scripts" / "run_daily.sh").read_text(encoding="utf-8")
    assert 'python3 "$SCRIPT_DIR/score_papers_sop.py"' in runner
    assert 'python3 "$SCRIPT_DIR/score_papers.py"' not in runner
