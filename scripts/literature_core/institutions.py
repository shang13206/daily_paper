from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class InstitutionStats:
    count: int
    venue_count: int
    code_count: int
    hardware_count: int

    def __post_init__(self) -> None:
        values = (
            self.count,
            self.venue_count,
            self.code_count,
            self.hardware_count,
        )
        if any(value < 0 for value in values):
            raise ValueError("institution counts must be non-negative")
        if any(value > self.count for value in values[1:]):
            raise ValueError("evidence counts cannot exceed paper count")


def compute_scores(
    stats: dict[str, InstitutionStats],
    seed_names: set[str],
    min_papers: int,
) -> dict[str, float]:
    if min_papers < 1:
        raise ValueError("min_papers must be positive")
    max_count = max((item.count for item in stats.values()), default=0)
    result: dict[str, float] = {}
    for name, item in stats.items():
        if item.count < min_papers or max_count == 0:
            result[name] = 8.0 if name in seed_names else 1.0
            continue
        frequency = math.log1p(item.count) / math.log1p(max_count)
        venue = item.venue_count / item.count
        code = item.code_count / item.count
        hardware = item.hardware_count / item.count
        result[name] = round(
            1
            + 9
            * (
                0.30 * frequency
                + 0.25 * venue
                + 0.20 * code
                + 0.25 * hardware
            ),
            2,
        )
    return result
