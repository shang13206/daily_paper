#!/usr/bin/env python3
"""LLM-based paper scoring via Claude CLI subprocess."""

import json
import logging
import re
import shlex
import subprocess
import sys
from pathlib import Path

logger = logging.getLogger(__name__)


def build_prompt(papers: list[dict], research_profile: str) -> str:
    """Build the LLM prompt for scoring a batch of papers."""
    papers_text = ""
    for i, paper in enumerate(papers, 1):
        papers_text += f"\n--- Paper {i} ---\n"
        papers_text += f"Title: {paper['title']}\n"
        papers_text += f"Abstract: {paper['abstract']}\n"

    prompt = f"""You are a research paper relevance scorer. Score each paper's relevance to the researcher's profile.

## Researcher Profile
{research_profile}

## Papers to Score
{papers_text}

## Instructions
For each paper, provide:
- score: integer 0-100 (0=irrelevant, 100=perfectly aligned with research)
- comment: one concise sentence in Chinese explaining relevance

Scoring guidelines:
- 80-100: Directly addresses core research (wheeled-legged robots, RL locomotion, sim-to-real)
- 60-79: Closely related (legged robot RL, terrain adaptation, Isaac/MuJoCo for locomotion)
- 40-59: Moderately related (general robot learning, other legged robots, relevant methods)
- 20-39: Tangentially related (general RL, robot manipulation, embodied AI)
- 0-19: Not relevant to the research profile

Respond with ONLY valid JSON, no markdown fences, no extra text:
{{"results": [{{"paper_index": 1, "score": <int>, "comment": "<string>"}}, ...]}}"""
    return prompt


def _extract_json_object(output: str) -> dict:
    """Extract the first JSON object from CLI output.

    Hermes CLI prints a `session_id: ...` line before the model response in
    gateway-friendly mode, while Claude may wrap JSON in markdown fences.  The
    scorer should accept both instead of treating useful output as failure.
    """
    output = output.strip()

    if "```" in output:
        blocks = re.findall(r"```(?:json)?\s*(.*?)```", output, flags=re.S | re.I)
        for block in blocks:
            try:
                return json.loads(block.strip())
            except json.JSONDecodeError:
                continue

    try:
        return json.loads(output)
    except json.JSONDecodeError:
        pass

    decoder = json.JSONDecoder()
    for match in re.finditer(r"\{", output):
        try:
            obj, _ = decoder.raw_decode(output[match.start():])
            if isinstance(obj, dict):
                return obj
        except json.JSONDecodeError:
            continue
    raise json.JSONDecodeError("No JSON object found in LLM output", output, 0)


def _build_command(
    prompt: str,
    claude_command: str,
    claude_flags: str,
    model: str,
) -> list[str]:
    """Build either a Claude CLI command or a Hermes CLI command.

    Historical config used Claude Code (`claude --model sonnet ... -p`).  On
    this machine Claude Code is installed but not logged in, while Hermes is
    authenticated.  If `claude_command` is set to `hermes`, pass the prompt as
    the final argument to the configured `-q` flag and do not inject Claude-only
    `--model` syntax.
    """
    cmd_parts = [claude_command]
    flags = shlex.split(claude_flags or "")
    executable = Path(claude_command).name

    if executable == "hermes":
        cmd_parts.extend(flags)
        if model:
            # `hermes chat` accepts -m/--model after the `chat` subcommand.
            try:
                chat_idx = cmd_parts.index("chat")
                cmd_parts[chat_idx + 1:chat_idx + 1] = ["--model", model]
            except ValueError:
                cmd_parts.extend(["--model", model])
        cmd_parts.append(prompt)
    else:
        if model:
            cmd_parts.extend(["--model", model])
        cmd_parts.extend(flags)
        cmd_parts.extend(["-p", prompt])
    return cmd_parts


def score_batch_with_llm(
    papers: list[dict],
    research_profile: str,
    claude_command: str = "claude",
    claude_flags: str = "--permission-mode bypassPermissions --print",
    model: str = "sonnet",
) -> list[dict]:
    """Score a batch of papers using a local LLM CLI.

    Returns a list of {"paper_index": int, "score": int, "comment": str} dicts.
    Returns empty list on failure.
    """
    prompt = build_prompt(papers, research_profile)
    cmd_parts = _build_command(prompt, claude_command, claude_flags, model)

    try:
        logger.info(f"Calling LLM CLI for {len(papers)} papers via {claude_command}...")
        result = subprocess.run(
            cmd_parts,
            capture_output=True,
            text=True,
            timeout=180,
        )

        if result.returncode != 0:
            stderr = (result.stderr or result.stdout or "")[:500]
            logger.error(f"LLM CLI failed (exit {result.returncode}): {stderr}")
            return []

        parsed = _extract_json_object(result.stdout)
        results = parsed.get("results", [])
        logger.info(f"LLM returned {len(results)} scores")
        return results

    except subprocess.TimeoutExpired:
        logger.error("LLM CLI timed out")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse LLM output as JSON: {e}")
        logger.debug(f"Raw output: {result.stdout[:500] if 'result' in dir() else 'N/A'}")
        return []
    except Exception as e:
        logger.error(f"LLM scoring error: {e}")
        return []


def score_papers_with_llm(
    papers: list[dict],
    research_profile: str,
    batch_size: int = 5,
    claude_command: str = "claude",
    claude_flags: str = "--permission-mode bypassPermissions --print",
    model: str = "sonnet",
) -> dict:
    """Score multiple papers in batches.

    Returns a dict mapping paper index (in the input list) to
    {"score": int, "comment": str}.
    """
    results = {}

    for batch_start in range(0, len(papers), batch_size):
        batch = papers[batch_start:batch_start + batch_size]
        logger.info(
            f"LLM scoring batch {batch_start // batch_size + 1} "
            f"({len(batch)} papers, {batch_start+1}-{batch_start+len(batch)} of {len(papers)})"
        )

        batch_results = score_batch_with_llm(
            batch,
            research_profile,
            claude_command=claude_command,
            claude_flags=claude_flags,
            model=model,
        )

        for item in batch_results:
            # paper_index in the batch is 1-based
            paper_idx = batch_start + item["paper_index"] - 1
            results[paper_idx] = {
                "score": int(item["score"]),
                "comment": item["comment"],
            }

    logger.info(f"LLM scoring complete: {len(results)}/{len(papers)} papers scored")
    return results
