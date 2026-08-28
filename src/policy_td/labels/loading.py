"""Load and validate frozen teacher labels."""

from __future__ import annotations

from collections.abc import Iterable

from policy_td.labels.schema import GPTJackieLabel


def validate_gpt_jackie_labels(rows: Iterable[dict]) -> list[GPTJackieLabel]:
    """Validate raw teacher-label dictionaries.

    Rows may either contain the label object directly or wrap it under a
    top-level ``labels`` key, matching the frozen artifact format.
    """
    labels: list[GPTJackieLabel] = []
    for row in rows:
        label_payload = row.get("labels", row)
        labels.append(GPTJackieLabel.model_validate(label_payload))
    return labels
