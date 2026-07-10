from scripts.literature_core.models import PaperRecord
from scripts.literature_core.sop import score_paper


def test_sop_accumulates_each_explicit_keyword_once(sop_config):
    paper = PaperRecord(
        title="Dexterous Manipulation for an Embodied AI Robot",
        abstract=(
            "Dexterous manipulation on a real robot deployed on Unitree hardware."
        ),
        categories=["cs.RO"],
        primary_category="cs.RO",
        affiliations=["Unknown Lab"],
        code_url="https://github.com/example/repo",
    )
    result = score_paper(paper, sop_config, {"Unknown Lab": 1.0})
    matched = {item["term"] for item in result.evidence.keywords}
    assert {
        "dexterous manipulation",
        "manipulation",
        "embodied AI",
        "embodied",
        "robot",
    } <= matched
    assert result.evidence.hardware["score"] == 4
    assert result.evidence.code["score"] == 3
    assert result.evidence.primary_cs_ro["score"] == 2


def test_sop_uses_highest_venue_and_institution_only(sop_config):
    paper = PaperRecord(
        title="Control",
        abstract="Accepted to ICRA and presented at CVPR.",
        affiliations=["Lab A", "Lab B"],
    )
    result = score_paper(paper, sop_config, {"Lab A": 2.0, "Lab B": 7.25})
    assert result.evidence.venue["score"] == 10
    assert result.evidence.institution == {"name": "Lab B", "score": 7.25}


def test_sop_levels_keep_decimal_boundaries(sop_config):
    selected = score_paper(
        PaperRecord(title="Control", affiliations=["Lab"]),
        sop_config,
        {"Lab": 8.0},
    )
    watch = score_paper(
        PaperRecord(title="Control", affiliations=["Lab"]),
        sop_config,
        {"Lab": 7.99},
    )
    filtered = score_paper(
        PaperRecord(title="Control", affiliations=["Lab"]),
        sop_config,
        {"Lab": 4.99},
    )
    assert (selected.level, watch.level, filtered.level) == (
        "selected",
        "watch",
        "filtered",
    )


def test_reinforcement_learning_requires_robotics_context(sop_config):
    generic = score_paper(
        PaperRecord(
            title="Reinforcement Learning for Portfolio Optimization",
            abstract="A reinforcement learning algorithm for financial markets.",
        ),
        sop_config,
        {},
    )
    robotics = score_paper(
        PaperRecord(
            title="Reinforcement Learning for Robot Control",
            abstract="A reinforcement learning policy for a mobile robot.",
        ),
        sop_config,
        {},
    )

    assert "reinforcement learning" not in {
        item["term"] for item in generic.evidence.keywords
    }
    assert "reinforcement learning" in {
        item["term"] for item in robotics.evidence.keywords
    }
