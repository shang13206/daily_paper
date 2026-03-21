#!/usr/bin/env python3
"""LLM-based paper scoring via Claude CLI subprocess."""

import json
import logging
import subprocess
import sys

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


def score_batch_with_llm(
    papers: list[dict],
    research_profile: str,
    claude_command: str = "claude",
    claude_flags: str = "--permission-mode bypassPermissions --print",
    model: str = "sonnet",
) -> list[dict]:
    """Score a batch of papers using Claude CLI.

    Returns a list of {"paper_index": int, "score": int, "comment": str} dicts.
    Returns empty list on failure.
    """
    prompt = build_prompt(papers, research_profile)

    cmd_parts = [claude_command]
    if model:
        cmd_parts.extend(["--model", model])
    cmd_parts.extend(claude_flags.split())
    cmd_parts.extend(["-p", prompt])

    try:
        logger.info(f"Calling Claude CLI for {len(papers)} papers...")
        result = subprocess.run(
            cmd_parts,
            capture_output=True,
            text=True,
            timeout=120,
        )

        if result.returncode != 0:
            logger.error(f"Claude CLI failed (exit {result.returncode}): {result.stderr[:500]}")
            return []

        output = result.stdout.strip()

        # Try to extract JSON from the output (handle markdown fences if present)
        if "```" in output:
            # Extract content between ``` markers
            lines = output.split("\n")
            json_lines = []
            in_block = False
            for line in lines:
                if line.strip().startswith("```"):
                    in_block = not in_block
                    continue
                if in_block:
                    json_lines.append(line)
            output = "\n".join(json_lines)

        parsed = json.loads(output)
        results = parsed.get("results", [])
        logger.info(f"LLM returned {len(results)} scores")
        return results

    except subprocess.TimeoutExpired:
        logger.error("Claude CLI timed out")
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
