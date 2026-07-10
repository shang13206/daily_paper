import math

from scripts.literature_core.institutions import InstitutionStats, compute_scores


def test_dynamic_formula_matches_sop():
    stats = {
        "Lab A": InstitutionStats(
            count=10, venue_count=8, code_count=5, hardware_count=6
        ),
        "Lab B": InstitutionStats(
            count=3, venue_count=0, code_count=0, hardware_count=0
        ),
    }
    scores = compute_scores(stats, seed_names=set(), min_papers=3)
    expected = 1 + 9 * (
        0.30 * 1.0 + 0.25 * 0.8 + 0.20 * 0.5 + 0.25 * 0.6
    )
    assert math.isclose(scores["Lab A"], round(expected, 2))


def test_cold_start_uses_seed_or_default():
    stats = {
        "MIT": InstitutionStats(
            count=2, venue_count=2, code_count=2, hardware_count=2
        ),
        "New Lab": InstitutionStats(
            count=1, venue_count=1, code_count=1, hardware_count=1
        ),
    }
    assert compute_scores(stats, seed_names={"MIT"}, min_papers=3) == {
        "MIT": 8.0,
        "New Lab": 1.0,
    }


def test_empty_stats_is_valid():
    assert compute_scores({}, seed_names={"MIT"}, min_papers=3) == {}
