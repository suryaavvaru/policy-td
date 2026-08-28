import json

import pandas as pd
import pytest

from policy_td.eval.validation import validate_runtime_table


def valid_row():
    return {
        "n": 10,
        "base_correct": 4,
        "guided_correct": 6,
        "base_acc": 0.4,
        "guided_acc": 0.6,
        "delta_acc": 0.2,
        "helped": 2,
        "harmed": 0,
        "net": 2,
        "intervention_rate": 0.2,
        "intervention_precision": 1.0,
        "false_intervention_rate": 0.0,
        "actions": json.dumps({"finalize": 8, "say_unknown": 2}),
    }


def test_valid_runtime_table():
    validate_runtime_table(pd.DataFrame([valid_row()]))


def test_inconsistent_helped_harmed_fails():
    row = valid_row()
    row["helped"] = 1
    with pytest.raises(ValueError, match="helped/harmed"):
        validate_runtime_table(pd.DataFrame([row]))


def test_action_counts_must_sum_to_n():
    row = valid_row()
    row["actions"] = json.dumps({"finalize": 7, "say_unknown": 2})
    with pytest.raises(ValueError, match="do not sum"):
        validate_runtime_table(pd.DataFrame([row]))
