import pytest
from pydantic import ValidationError

from policy_td.labels.schema import GPTJackieLabel


def valid_payload():
    return {
        "claim_support": "derived_supported",
        "answerability": "answerable_sufficient",
        "entity_state": "ok",
        "logical_operator": "ok",
        "answer_trace_consistency": "consistent",
        "best_action": "finalize",
        "should_intervene": False,
        "confidence": 0.9,
    }


def test_valid_gpt_jackie_label():
    label = GPTJackieLabel.model_validate(valid_payload())
    assert label.best_action.value == "finalize"


def test_invalid_claim_support_fails():
    payload = valid_payload()
    payload["claim_support"] = "made_up_label"
    with pytest.raises(ValidationError):
        GPTJackieLabel.model_validate(payload)


def test_unknown_field_fails_closed():
    payload = valid_payload()
    payload["best_actoin"] = payload["best_action"]
    with pytest.raises(ValidationError):
        GPTJackieLabel.model_validate(payload)


def test_optional_diagnostic_fields_are_supported():
    payload = valid_payload()
    payload.update({
        "failure_span": "unsupported clause",
        "repair_hint": "abstain",
        "unsupported_claims": ["claim A"],
    })
    label = GPTJackieLabel.model_validate(payload)
    assert label.unsupported_claims == ["claim A"]
