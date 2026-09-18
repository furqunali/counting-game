from dataclasses import dataclass
from random import Random

@dataclass(frozen=True)
class RoundResult:
    guess: int
    target: int
    correct: bool
    attempts: int
    hint: str

class CountingGameEngine:
    def __init__(self, start=1, end=100, rng=None):
        if start >= end:
            raise ValueError("start must be less than end")
        self.start, self.end = int(start), int(end)
        self.rng = rng or Random()
        self.target = None
        self.attempts = 0
        self.finished = False

    def new_round(self):
        self.target = self.rng.randint(self.start, self.end)
        self.attempts = 0
        self.finished = False
        return self.target

    def guess(self, value):
        if self.target is None:
            raise RuntimeError("start a round first")
        if self.finished:
            raise RuntimeError("round is already finished")
        value = int(value)
        self.attempts += 1
        correct = value == self.target
        if correct:
            hint = "correct"
            self.finished = True
        elif value < self.target:
            hint = "higher"
        else:
            hint = "lower"
        return RoundResult(value, self.target, correct, self.attempts, hint)

    def is_finished(self):
        return self.finished

    def score(self):
        return max(0, 1000 - (self.attempts - 1) * 50) if self.finished else 0
