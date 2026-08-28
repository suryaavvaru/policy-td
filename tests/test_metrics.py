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


def test_runtime_summary_yields():
    from policy_td.eval.metrics import RuntimeSummary

    summary = RuntimeSummary(
        n=10, base_correct=4, guided_correct=6, helped=2, harmed=0, interventions=4
    )
    assert summary.intervention_rate == 0.4
    assert summary.help_yield == 0.5
    assert summary.harm_yield == 0.0
