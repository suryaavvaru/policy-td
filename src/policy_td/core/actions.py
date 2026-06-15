"""Runtime action vocabulary for Policy-TD."""

from enum import Enum


class RuntimeAction(str, Enum):
    """Typed intervention actions available to the runtime controller."""

    FINALIZE = "finalize"
    SAY_UNKNOWN = "say_unknown"
    REPAIR_FINAL = "repair_final"
    ROLLBACK = "rollback"
    FORCE_GROUNDED_STEP = "force_grounded_step"
    CONTINUE = "continue"


ACTION_DESCRIPTIONS: dict[RuntimeAction, str] = {
    RuntimeAction.FINALIZE: "Accept the current student answer.",
    RuntimeAction.SAY_UNKNOWN: "Return an abstention when the prompt lacks sufficient support.",
    RuntimeAction.REPAIR_FINAL: "Apply a bounded correction to the final answer.",
    RuntimeAction.ROLLBACK: "Discard an unsafe trajectory and revert to a safer state.",
    RuntimeAction.FORCE_GROUNDED_STEP: "Request a constrained continuation grounded in the prompt.",
    RuntimeAction.CONTINUE: "Allow generation to proceed without behavior-changing intervention.",
}
