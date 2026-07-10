from scripts.literature_core.models import PaperRecord


def test_paper_record_round_trips_legacy_mapping():
    raw = {
        "arxiv_id": "2607.01234v2",
        "title": "A Wheeled-Legged Robot",
        "abstract": "We deploy on a real robot.",
        "authors": ["Ada Robot"],
        "affiliations": ["ETH Zurich"],
        "categories": ["cs.RO", "cs.LG"],
        "published_date": "2026-07-10",
        "abs_url": "https://arxiv.org/abs/2607.01234v2",
        "pdf_url": "https://arxiv.org/pdf/2607.01234v2.pdf",
    }

    record = PaperRecord.from_mapping(raw, source_name="arxiv")

    assert record.paper_id is None
    assert record.year == 2026
    assert record.primary_category == "cs.RO"
    assert record.source_names == ["arxiv"]
    assert record.to_mapping()["arxiv_id"] == "2607.01234v2"
