"""Stable label names used by Policy-TD."""

CLAIM_SUPPORT_LABELS = (
    "prompt_supported",
    "derived_supported",
    "plausible_uncertain",
    "unsupported",
    "contradiction",
)

ANSWERABILITY_LABELS = (
    "answerable_not_sufficient",
    "answerable_sufficient",
    "not_enough_information",
    "partially_answerable",
)

ENTITY_STATE_LABELS = (
    "ok",
    "entity_binding_error",
    "state_transition_error",
    "relation_direction_error",
)

LOGICAL_OPERATOR_LABELS = (
    "ok",
    "quantifier_error",
    "negation_error",
    "operator_ambiguous",
)

CONSISTENCY_LABELS = (
    "consistent",
    "inconsistent",
    "no_final_answer",
)

ACTION_LABELS = (
    "continue",
    "force_grounded_step",
    "rollback",
    "say_unknown",
    "finalize",
    "repair_final",
)

SHOULD_INTERVENE_LABELS = (
    "no_intervene",
    "intervene",
)
