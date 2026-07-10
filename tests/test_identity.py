from scripts.literature_core.identity import (
    canonical_arxiv_id,
    canonical_doi,
    identity_keys,
    normalize_title,
)
from scripts.literature_core.models import PaperRecord


def test_identity_normalization_is_version_and_url_safe():
    assert canonical_arxiv_id("arXiv:2607.01234v3") == "2607.01234"
    assert canonical_doi("https://doi.org/10.1234/ABC.7") == "10.1234/abc.7"
    assert normalize_title("  Robot—Learning: A Study! ") == "robot learning a study"


def test_identity_keys_use_exact_ids_then_title_year():
    paper = PaperRecord(
        arxiv_id="2607.01234v2",
        doi="10.1234/ABC.7",
        title="Robot Learning: A Study",
        year=2026,
    )
    assert identity_keys(paper) == [
        ("arxiv", "2607.01234"),
        ("doi", "10.1234/abc.7"),
        ("title_year", "robot learning a study|2026"),
    ]
