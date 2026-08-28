"""Paired runtime metrics for Policy-TD."""

from dataclasses import dataclass


def helped(base_correct: bool, guided_correct: bool) -> bool:
    """Return True when guided output corrects a baseline failure."""
    return (not base_correct) and guided_correct


def harmed(base_correct: bool, guided_correct: bool) -> bool:
    """Return True when guided output corrupts a baseline success."""
    return base_correct and (not guided_correct)


def paired_delta(base_correct: bool, guided_correct: bool) -> int:
    """Return paired accuracy delta for one example."""
    return int(guided_correct) - int(base_correct)


@dataclass(frozen=True)
class RuntimeOutcome:
    """Paired correctness outcome for one baseline/guided example."""

    base_correct: bool
    guided_correct: bool

    @property
    def helped(self) -> bool:
        return helped(self.base_correct, self.guided_correct)

    @property
    def harmed(self) -> bool:
        return harmed(self.base_correct, self.guided_correct)

    @property
    def delta(self) -> int:
        return paired_delta(self.base_correct, self.guided_correct)


@dataclass(frozen=True)
class RuntimeSummary:
    """Aggregate runtime metrics."""

    n: int
    base_correct: int
    guided_correct: int
    helped: int
    harmed: int
    interventions: int

    @property
    def base_accuracy(self) -> float:
        return self.base_correct / self.n if self.n else 0.0

    @property
    def guided_accuracy(self) -> float:
        return self.guided_correct / self.n if self.n else 0.0

    @property
    def delta_accuracy(self) -> float:
        return self.guided_accuracy - self.base_accuracy

    @property
    def net_helped(self) -> int:
        return self.helped - self.harmed

    @property
    def intervention_rate(self) -> float:
        return self.interventions / self.n if self.n else 0.0

    @property
    def help_yield(self) -> float:
        """Fraction of behavior-changing interventions that produce a helped outcome."""
        return self.helped / self.interventions if self.interventions else 0.0

    @property
    def harm_yield(self) -> float:
        """Fraction of behavior-changing interventions that produce a harmed outcome."""
        return self.harmed / self.interventions if self.interventions else 0.0
