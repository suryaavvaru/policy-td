from policy_td.core.actions import RuntimeAction
from policy_td.runtime.controller import ControllerDecision, is_behavior_changing, router_off


def test_behavior_changing_actions():
    assert not is_behavior_changing(RuntimeAction.FINALIZE)
    assert not is_behavior_changing(RuntimeAction.CONTINUE)
    assert is_behavior_changing(RuntimeAction.SAY_UNKNOWN)


def test_router_off_disables_intervention():
    decision = ControllerDecision(
        action=RuntimeAction.SAY_UNKNOWN,
        should_intervene=True,
        confidence=0.8,
    )
    disabled = router_off(decision)
    assert disabled.action == RuntimeAction.FINALIZE
    assert disabled.should_intervene is False
    assert disabled.confidence == 0.8
