"""Load and validate frozen GPT-Jackie labels."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from policy_td.labels.schema import GPTJackieLabel


def read_jsonl(path: str | Path) -> list[dict]:
    """Read a JSONL file into dictionaries."""
    rows: list[dict] = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid JSON on line {line_number} in {path}") from exc
    return rows


def validate_gpt_jackie_labels(rows: Iterable[dict]) -> list[GPTJackieLabel]:
    """Validate raw GPT-Jackie label dictionaries."""
    labels: list[GPTJackieLabel] = []
    for row in rows:
        label_payload = row.get("labels", row)
        labels.append(GPTJackieLabel.model_validate(label_payload))
    return labels
