"""Typed teacher-label schema used by the public Policy-TD artifact."""

from pydantic import BaseModel, ConfigDict, Field, field_validator

from policy_td.core.actions import RuntimeAction
from policy_td.core.constants import (
    ANSWERABILITY_LABELS,
    CLAIM_SUPPORT_LABELS,
    CONSISTENCY_LABELS,
    ENTITY_STATE_LABELS,
    LOGICAL_OPERATOR_LABELS,
)


class GPTJackieLabel(BaseModel):
    """Validated teacher label for one frozen-student trace.

    Unknown fields are rejected so that misspelled or off-schema teacher
    outputs cannot be silently dropped during artifact validation.
    """

    model_config = ConfigDict(extra="forbid")

    claim_support: str
    answerability: str
    entity_state: str
    logical_operator: str
    answer_trace_consistency: str
    best_action: RuntimeAction
    should_intervene: bool | None = None
    confidence: float | None = Field(default=None, ge=0.0, le=1.0)
    failure_span: str | None = None
    repair_hint: str | None = None
    unsupported_claims: list[str] = Field(default_factory=list)

    @field_validator("claim_support")
    @classmethod
    def validate_claim_support(cls, value: str) -> str:
        if value not in CLAIM_SUPPORT_LABELS:
            raise ValueError(f"invalid claim_support label: {value}")
        return value

    @field_validator("answerability")
    @classmethod
    def validate_answerability(cls, value: str) -> str:
        if value not in ANSWERABILITY_LABELS:
            raise ValueError(f"invalid answerability label: {value}")
        return value

    @field_validator("entity_state")
    @classmethod
    def validate_entity_state(cls, value: str) -> str:
        if value not in ENTITY_STATE_LABELS:
            raise ValueError(f"invalid entity_state label: {value}")
        return value

    @field_validator("logical_operator")
    @classmethod
    def validate_logical_operator(cls, value: str) -> str:
        if value not in LOGICAL_OPERATOR_LABELS:
            raise ValueError(f"invalid logical_operator label: {value}")
        return value

    @field_validator("answer_trace_consistency")
    @classmethod
    def validate_consistency(cls, value: str) -> str:
        if value not in CONSISTENCY_LABELS:
            raise ValueError(f"invalid answer_trace_consistency label: {value}")
        return value
