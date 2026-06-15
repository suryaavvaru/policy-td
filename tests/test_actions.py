from policy_td.core.actions import RuntimeAction


def test_action_vocabulary_is_stable():
    assert {action.value for action in RuntimeAction} == {
        "finalize",
        "say_unknown",
        "repair_final",
        "rollback",
        "force_grounded_step",
        "continue",
    }
