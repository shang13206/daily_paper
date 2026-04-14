from datetime import datetime

import pytest

from scripts.fetch_papers import (
    _extract_articles_from_list_section,
    _extract_list_sections,
    fetch_arxiv_papers,
)
from scripts.score_papers import filter_papers, venue_institution_bonus


SAMPLE_LIST_HTML = """
<html><body>
<h3>Fri, 10 Apr 2026 (showing first 2 of 2 entries)</h3>
<dl id='articles'>
  <dt>
    <a href="/abs/2604.00001" title="Abstract" id="2604.00001">arXiv:2604.00001</a>
  </dt>
  <dd>
    <div class='meta'>
      <div class='list-title mathjax'><span class='descriptor'>Title:</span>
        A Robot Paper
      </div>
      <div class='list-authors'><a href="/search/?q=A">Alice</a>, <a href="/search/?q=B">Bob</a></div>
      <div class='list-comments mathjax'><span class='descriptor'>Comments:</span>
        Accepted to ICRA 2026
      </div>
      <div class='list-subjects'><span class='descriptor'>Subjects:</span>
        <span class="primary-subject">Robotics (cs.RO)</span>; Artificial Intelligence (cs.AI)
      </div>
    </div>
  </dd>
</dl>
</body></html>
"""


SCORE_CONFIG = {
    "scoring": {
        "filter": {
            "exclude_keywords": ["student dropout"],
            "core_include_keywords": ["quadruped", "sim-to-real", "navigation", "slam"],
            "perception_keywords": ["depth estimation", "visual odometry"],
            "robotics_context_keywords": ["robot", "robotics", "navigation", "mobile robot"],
            "require_robotics_context_for_perception": True,
            "allow_primary_csro": True,
        },
        "venue_bonus": {"tier1": 35, "tier2": 20, "tier3": 10},
        "venue_keywords": {
            "tier1": ["TRO"],
            "tier2": ["ICRA"],
            "tier3": [],
        },
        "institution_bonus": {"tier1": 15, "tier2": 8},
        "institution_keywords": {"tier1": ["FAIR"], "tier2": []},
    }
}


def test_extract_list_sections_and_articles():
    sections = _extract_list_sections(SAMPLE_LIST_HTML)
    assert len(sections) == 1
    assert sections[0][0] == datetime(2026, 4, 10)

    articles = _extract_articles_from_list_section(
        sections[0][1], "cs.RO", "2026-04-10"
    )
    assert len(articles) == 1
    paper = articles[0]
    assert paper["arxiv_id"] == "2604.00001"
    assert paper["title"] == "A Robot Paper"
    assert paper["authors"] == ["Alice", "Bob"]
    assert paper["comment"] == "Accepted to ICRA 2026"
    assert paper["categories"] == ["cs.RO", "cs.AI"]
    assert paper["updated_date"] == "2026-04-10"


def test_fetch_arxiv_papers_raises_if_all_sources_fail(monkeypatch):
    def boom(*args, **kwargs):
        raise RuntimeError("network down")

    monkeypatch.setattr("scripts.fetch_papers._http_get", boom)

    with pytest.raises(RuntimeError, match="All arXiv fetch attempts failed"):
        fetch_arxiv_papers(["cs.RO"], "2026-04-10", max_results=1, delay=0, timeout=1, days=1)


def test_short_acronyms_do_not_match_inside_other_words():
    bonus, matched_venue, matched_institutions = venue_institution_bonus(
        {
            "comment": "This paper studies student dropout with a control baseline.",
            "affiliations": ["Center for Fairness in ML"],
        },
        SCORE_CONFIG,
    )
    assert bonus == 0
    assert matched_venue == ""
    assert matched_institutions == []


def test_short_acronyms_still_match_as_standalone_tokens():
    bonus, matched_venue, matched_institutions = venue_institution_bonus(
        {
            "comment": "Accepted to TRO and ICRA 2026.",
            "affiliations": ["Meta FAIR"],
        },
        SCORE_CONFIG,
    )
    assert bonus == 35 + 15
    assert matched_venue == "TRO"
    assert matched_institutions == ["FAIR"]


def test_filter_keeps_perception_only_with_robotics_context():
    papers = [
        {
            "title": "Monocular depth estimation for general web videos",
            "abstract": "A depth estimation benchmark for internet videos.",
            "categories": ["cs.CV"],
        },
        {
            "title": "Monocular depth estimation for mobile robot navigation",
            "abstract": "A robot navigation system with depth estimation.",
            "categories": ["cs.CV"],
        },
    ]
    kept = filter_papers(papers, SCORE_CONFIG)
    assert len(kept) == 1
    assert kept[0]["title"] == "Monocular depth estimation for mobile robot navigation"


def test_filter_keeps_core_robotics_and_primary_csro_backstop():
    papers = [
        {
            "title": "Quadruped locomotion with sim-to-real adaptation",
            "abstract": "A quadruped robot policy for rough terrain.",
            "categories": ["cs.AI", "cs.RO"],
        },
        {
            "title": "A compliant parallel manipulator design note",
            "abstract": "Robot kinematics without locomotion or navigation.",
            "categories": ["cs.RO"],
        },
    ]
    kept = filter_papers(papers, SCORE_CONFIG)
    assert len(kept) == 2
