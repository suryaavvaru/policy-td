"""Inspect frozen Policy-TD result tables."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def format_pct(value: float) -> str:
    return f"{100 * value:.2f}%"


def inspect_pooled(table_path: Path) -> None:
    df = pd.read_csv(table_path)

    keep = [
        "suite",
        "condition",
        "n",
        "base_acc",
        "guided_acc",
        "delta_acc",
        "helped",
        "harmed",
        "intervention_rate",
    ]

    missing = [column for column in keep if column not in df.columns]
    if missing:
        raise ValueError(f"missing expected columns: {missing}")

    print("Frozen Policy-TD pooled runtime summary")
    print("=" * 44)

    for _, row in df[keep].iterrows():
        print(
            f"{row['suite']:28s} "
            f"{row['condition']:22s} "
            f"n={int(row['n']):5d} "
            f"base={format_pct(row['base_acc']):>7s} "
            f"guided={format_pct(row['guided_acc']):>7s} "
            f"delta={100 * row['delta_acc']:+6.2f} pp "
            f"helped={int(row['helped']):4d} "
            f"harmed={int(row['harmed']):4d} "
            f"int={format_pct(row['intervention_rate']):>7s}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=Path("results/frozen_release/internal_plus_real_external"),
    )
    args = parser.parse_args()

    table_path = args.results_dir / "TABLE_2_runtime_pooled_condition.csv"
    inspect_pooled(table_path)


if __name__ == "__main__":
    main()
