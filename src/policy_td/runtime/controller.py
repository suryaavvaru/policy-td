"""Runtime controller utilities."""

from dataclasses import dataclass

from policy_td.core.actions import RuntimeAction


@dataclass(frozen=True)
class ControllerDecision:
    """One runtime controller decision."""

    action: RuntimeAction
    should_intervene: bool
    confidence: float | None = None


def is_behavior_changing(action: RuntimeAction) -> bool:
    """Return whether an action changes baseline behavior."""
    return action not in {RuntimeAction.FINALIZE, RuntimeAction.CONTINUE}


def router_off(decision: ControllerDecision) -> ControllerDecision:
    """Disable behavior-changing interventions while preserving the evaluation path."""
    return ControllerDecision(
        action=RuntimeAction.FINALIZE,
        should_intervene=False,
        confidence=decision.confidence,
    )
