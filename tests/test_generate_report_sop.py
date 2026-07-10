from scripts.generate_report import generate_report


def test_report_uses_sop_selected_and_watch_levels():
    evidence = {
        "venue": {"tier": "tier1", "term": "ICRA", "score": 10},
        "institution": {"name": "", "score": 0},
        "keywords": [{"group": "core", "term": "locomotion", "score": 5}],
        "hardware": {"terms": ["real robot", "Unitree"], "score": 4},
        "code": {"url": "https://github.com/example/repo", "score": 3},
        "primary_cs_ro": {"category": "cs.RO", "score": 2},
    }
    scored = {
        "date": "2026-07-09",
        "total_fetched": 3,
        "after_filter": 2,
        "selected_count": 1,
        "watch_count": 1,
        "filtered_count": 1,
        "scoring_mechanism": "paper-evaluation-sop-v1",
        "papers": [
            {
                "title": "Selected Paper",
                "score": 24,
                "score_level": "selected",
                "score_evidence": evidence,
                "categories": ["cs.RO"],
                "abstract": "Selected abstract.",
                "abs_url": "https://arxiv.org/abs/1",
                "pdf_url": "https://arxiv.org/pdf/1.pdf",
                "ingestion_status": "pending",
            },
            {
                "title": "Watch Paper",
                "score": 6,
                "score_level": "watch",
                "score_evidence": evidence,
                "categories": ["cs.RO"],
                "abstract": "Watch abstract.",
                "abs_url": "https://arxiv.org/abs/2",
                "pdf_url": "https://arxiv.org/pdf/2.pdf",
                "ingestion_status": "not_applicable",
            },
            {
                "title": "Filtered Paper",
                "score": 0,
                "score_level": "filtered",
                "score_evidence": evidence,
                "categories": ["cs.LG"],
                "abstract": "Filtered abstract.",
                "abs_url": "https://arxiv.org/abs/3",
                "pdf_url": "https://arxiv.org/pdf/3.pdf",
                "ingestion_status": "not_applicable",
            },
        ],
    }
    config = {"report": {"top_n": 5, "watch_threshold": 20}}

    report = generate_report(scored, config)

    assert "SOP 精选论文 (≥ 8 分)" in report
    assert "Selected Paper" in report
    assert "SOP 评分证据" in report
    assert "待入库" in report
    assert "Watch Paper" in report
    assert "Filtered Paper" not in report
    assert "精选: 1 篇 | 关注: 1 篇 | 过滤: 1 篇" in report
