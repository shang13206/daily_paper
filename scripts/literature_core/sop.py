from __future__ import annotations

import re
from typing import Any

from .models import PaperRecord, ScoreEvidence, ScoreResult


def contains_term(term: str, text: str) -> bool:
    escaped = re.escape(term.casefold())
    return re.search(rf"(?<!\w){escaped}(?!\w)", text.casefold()) is not None


def assign_level(total: float, config: dict[str, Any]) -> str:
    if total >= float(config["thresholds"]["selected"]):
        return "selected"
    if total >= float(config["thresholds"]["watch"]):
        return "watch"
    return "filtered"


def _keyword_is_eligible(
    group: str, term: str, text: str, config: dict[str, Any]
) -> bool:
    if not contains_term(term, text):
        return False
    if group != "related" or term.casefold() != "reinforcement learning":
        return True
    context_terms = config["keywords"]["related"].get(
        "robotics_context_terms", []
    )
    return any(contains_term(context, text) for context in context_terms)


def score_paper(
    paper: PaperRecord,
    config: dict[str, Any],
    institution_scores: dict[str, float],
) -> ScoreResult:
    text = " ".join([paper.title, paper.abstract, paper.comment, paper.venue])

    venue = {"tier": "", "term": "", "score": 0}
    for tier in ("tier1", "tier2"):
        hit = next(
            (
                term
                for term in config["venue"][tier]["terms"]
                if contains_term(term, text)
            ),
            "",
        )
        if hit:
            venue = {
                "tier": tier,
                "term": hit,
                "score": int(config["venue"][tier]["score"]),
            }
            break

    institution_hits = [
        (name, float(institution_scores[name]))
        for name in paper.affiliations
        if name in institution_scores
    ]
    institution_name, institution_score = max(
        institution_hits, key=lambda item: item[1], default=("", 0.0)
    )
    institution = {
        "name": institution_name,
        "score": round(institution_score, 2),
    }

    keywords: list[dict[str, Any]] = []
    for group in ("core", "related", "general"):
        weight = int(config["keywords"][group]["score"])
        for term in config["keywords"][group]["terms"]:
            if _keyword_is_eligible(group, term, text, config):
                keywords.append({"group": group, "term": term, "score": weight})

    hardware_terms = sorted(
        {
            term
            for term in config["hardware"]["terms"]
            if contains_term(term, text)
        }
    )
    hardware_score = (
        int(config["hardware"]["score"])
        if len(hardware_terms)
        >= int(config["hardware"]["min_distinct_evidence"])
        else 0
    )
    hardware = {"terms": hardware_terms, "score": hardware_score}

    code_url = paper.code_url or paper.project_url
    code = {
        "url": code_url,
        "score": int(config["code"]["score"]) if code_url else 0,
    }
    primary_cs_ro = {
        "category": paper.primary_category,
        "score": (
            int(config["primary_cs_ro"]["score"])
            if paper.primary_category == "cs.RO"
            else 0
        ),
    }

    total = round(
        float(venue["score"])
        + float(institution["score"])
        + sum(float(item["score"]) for item in keywords)
        + float(hardware["score"])
        + float(code["score"])
        + float(primary_cs_ro["score"]),
        2,
    )
    evidence = ScoreEvidence(
        venue=venue,
        institution=institution,
        keywords=keywords,
        hardware=hardware,
        code=code,
        primary_cs_ro=primary_cs_ro,
    )
    return ScoreResult(
        total=total,
        level=assign_level(total, config),
        evidence=evidence,
    )
