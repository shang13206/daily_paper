import scripts.score_papers as scorer


def _base_config():
    return {
        "scoring": {
            "high_weight": 18,
            "mid_weight": 10,
            "low_weight": 5,
            "keywords": {
                "high": ["locomotion control"],
                "mid": ["quadruped"],
                "low": [],
            },
            "category_bonus": {"cs.RO": 12},
            "filter": {"deprioritize_keywords": []},
            "deprioritize_penalty": 8,
            "algorithmic_adjustment": {
                "system_demo_penalty": 12,
                "weak_relevance_penalty": 16,
                "system_demo_keywords": [
                    "long-distance",
                    "field experiment",
                    "commercially available",
                    "demonstrate",
                ],
                "algorithmic_keywords": [
                    "we propose",
                    "reward function",
                    "policy architecture",
                    "representation",
                    "estimator",
                    "planner",
                ],
            },
        },
        "llm": {"enable_llm_scoring": False},
        "comment_templates": {},
    }


def _paper(title, abstract):
    return {
        "title": title,
        "abstract": abstract,
        "categories": ["cs.RO"],
        "comment": "",
        "affiliations": [],
    }


def test_system_demo_paper_is_deprioritized_when_algorithmic_signal_is_weak(monkeypatch):
    monkeypatch.setattr(scorer, "ZOTERO_INDEX", "/tmp/nonexistent-zotero-index.json")
    paper = _paper(
        "Long-Distance Real-World Navigation of the Legged-Wheeled Robot Go2-W Using Deep Reinforcement Learning",
        "This paper reports a locomotion control and autonomous navigation system "
        "for a commercially available quadruped robot and demonstrates "
        "long-distance field experiment results.",
    )

    scored = scorer.score_papers([paper], _base_config(), enable_llm=False)

    assert scored[0]["keyword_score"] == 40
    assert scored[0]["score"] == 28
    assert "system_demo_without_algorithmic_signal:-12" in scored[0]["score_adjustments"]


def test_algorithmic_method_paper_keeps_score_when_method_signal_is_clear(monkeypatch):
    monkeypatch.setattr(scorer, "ZOTERO_INDEX", "/tmp/nonexistent-zotero-index.json")
    paper = _paper(
        "Policy Architecture for Long-Distance Quadruped Locomotion Control",
        "We propose a policy architecture and reward function for quadruped "
        "locomotion control. The method includes a representation estimator "
        "and is validated in a long-distance field experiment.",
    )

    scored = scorer.score_papers([paper], _base_config(), enable_llm=False)

    assert scored[0]["keyword_score"] == 40
    assert scored[0]["score"] == 40
    assert scored[0]["score_adjustments"] == []


def test_venue_only_csro_paper_is_deprioritized_as_weak_relevance(monkeypatch):
    monkeypatch.setattr(scorer, "ZOTERO_INDEX", "/tmp/nonexistent-zotero-index.json")
    config = _base_config()
    config["scoring"]["venue_bonus"] = {"tier2": 20}
    config["scoring"]["venue_keywords"] = {"tier2": ["IROS"]}
    paper = _paper(
        "Membrane-based Acoustic Microrobots",
        "Acoustic microrobots are designed for targeted drug delivery and "
        "minimally invasive medicine.",
    )
    paper["comment"] = "Accepted to IROS 2026"

    scored = scorer.score_papers([paper], config, enable_llm=False)

    assert scored[0]["keyword_score"] == 12
    assert scored[0]["venue_bonus"] == 20
    assert scored[0]["score"] == 16
    assert "weak_relevance_without_topic_signal:-16" in scored[0]["score_adjustments"]


def test_dispreferred_surgical_topic_does_not_rank_high_from_venue_and_sim2real(monkeypatch):
    monkeypatch.setattr(scorer, "ZOTERO_INDEX", "/tmp/nonexistent-zotero-index.json")
    config = scorer.load_config("/home/sshang/daily_paper/scripts/config.yaml")
    paper = _paper(
        "Overcoming Imperfect Kinematics in Surgical Robotics Through Sim-to-Real Visuomotor Learning",
        "Robot-assisted surgery uses sim-to-real visuomotor learning for a "
        "surgical robot in minimally invasive procedures.",
    )
    paper["comment"] = "Accepted to ICRA 2026"

    scored = scorer.score_papers([paper], config, enable_llm=False)

    assert scored[0]["score"] < 30


def test_dispreferred_grasping_topic_does_not_rank_high_from_sim2real_keywords(monkeypatch):
    monkeypatch.setattr(scorer, "ZOTERO_INDEX", "/tmp/nonexistent-zotero-index.json")
    config = scorer.load_config("/home/sshang/daily_paper/scripts/config.yaml")
    paper = _paper(
        "Pose-Agnostic Robotic Functional Grasping via Observation-Action Canonicalization",
        "Functional robotic grasping uses sim-to-real and domain randomization "
        "for mug-handle grasping.",
    )

    scored = scorer.score_papers([paper], config, enable_llm=False)

    assert scored[0]["score"] < 30
