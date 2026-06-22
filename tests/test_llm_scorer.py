from scripts.llm_scorer import _build_command


def test_build_command_for_codex_exec_uses_prompt_argument():
    cmd = _build_command(
        "score these papers",
        "codex",
        "exec --skip-git-repo-check --ephemeral",
        "gpt-5.5",
    )

    assert cmd == [
        "codex",
        "exec",
        "--model",
        "gpt-5.5",
        "--skip-git-repo-check",
        "--ephemeral",
        "score these papers",
    ]
    assert "-p" not in cmd


def test_build_command_for_codex_adds_exec_when_flags_omit_it():
    cmd = _build_command(
        "score these papers",
        "codex",
        "--skip-git-repo-check --ephemeral",
        "",
    )

    assert cmd == [
        "codex",
        "exec",
        "--skip-git-repo-check",
        "--ephemeral",
        "score these papers",
    ]
    assert "-p" not in cmd
