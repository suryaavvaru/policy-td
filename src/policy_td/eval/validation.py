"""Validation helpers for curated frozen result tables."""

from __future__ import annotations

import json
import math

import pandas as pd

_REQUIRED_RUNTIME_COLUMNS = {
    "n",
    "base_correct",
    "guided_correct",
    "base_acc",
    "guided_acc",
    "delta_acc",
    "helped",
    "harmed",
}


def _close(left: float, right: float, *, tolerance: float) -> bool:
    return math.isclose(float(left), float(right), rel_tol=0.0, abs_tol=tolerance)


def validate_runtime_table(df: pd.DataFrame, *, tolerance: float = 2e-6) -> None:
    """Validate arithmetic invariants in a frozen runtime summary table.

    The public CSVs are rounded to six decimals, so a small absolute
    tolerance is expected when recomputing ratios from integer counts.
    """
    missing = sorted(_REQUIRED_RUNTIME_COLUMNS.difference(df.columns))
    if missing:
        raise ValueError(f"missing required runtime columns: {missing}")

    for index, row in df.iterrows():
        n = int(row["n"])
        if n <= 0:
            raise ValueError(f"row {index}: n must be positive")

        base_correct = int(row["base_correct"])
        guided_correct = int(row["guided_correct"])
        helped = int(row["helped"])
        harmed = int(row["harmed"])

        for name, value in {
            "base_correct": base_correct,
            "guided_correct": guided_correct,
            "helped": helped,
            "harmed": harmed,
        }.items():
            if value < 0 or value > n:
                raise ValueError(f"row {index}: {name}={value} outside [0, n]")

        if not _close(row["base_acc"], base_correct / n, tolerance=tolerance):
            raise ValueError(f"row {index}: base_acc is inconsistent with base_correct/n")
        if not _close(row["guided_acc"], guided_correct / n, tolerance=tolerance):
            raise ValueError(f"row {index}: guided_acc is inconsistent with guided_correct/n")
        if not _close(
            row["delta_acc"], guided_correct / n - base_correct / n, tolerance=tolerance
        ):
            raise ValueError(f"row {index}: delta_acc is inconsistent with paired counts")

        if guided_correct - base_correct != helped - harmed:
            raise ValueError(f"row {index}: helped/harmed identity is inconsistent")

        if "net" in df.columns and int(row["net"]) != helped - harmed:
            raise ValueError(f"row {index}: net is inconsistent with helped-harmed")

        for metric in (
            "intervention_rate",
            "intervention_precision",
            "false_intervention_rate",
            "base_unsupported_rate",
            "guided_unsupported_rate",
        ):
            if metric in df.columns and not (0.0 <= float(row[metric]) <= 1.0):
                raise ValueError(f"row {index}: {metric} must be in [0, 1]")

        if "actions" in df.columns:
            actions = json.loads(row["actions"])
            if not isinstance(actions, dict):
                raise ValueError(f"row {index}: actions must decode to an object")
            if any(int(count) < 0 for count in actions.values()):
                raise ValueError(f"row {index}: action counts cannot be negative")
            if sum(int(count) for count in actions.values()) != n:
                raise ValueError(f"row {index}: action counts do not sum to n")
