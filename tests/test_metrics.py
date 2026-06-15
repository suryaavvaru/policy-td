from policy_td.eval.metrics import RuntimeOutcome, harmed, helped, paired_delta


def test_helped():
    assert helped(False, True)
    assert not helped(True, True)
    assert not helped(False, False)


def test_harmed():
    assert harmed(True, False)
    assert not harmed(False, True)
    assert not harmed(True, True)


def test_paired_delta():
    assert paired_delta(False, True) == 1
    assert paired_delta(True, False) == -1
    assert paired_delta(True, True) == 0


def test_runtime_outcome_properties():
    outcome = RuntimeOutcome(base_correct=False, guided_correct=True)
    assert outcome.helped
    assert not outcome.harmed
    assert outcome.delta == 1
