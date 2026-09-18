from dataclasses import dataclass
from random import Random

@dataclass(frozen=True)
class GuessResult:
    guess: int
    target: int
    correct: bool
    attempts: int
    hint: str

class CountingGame:
    def __init__(self, start=1, end=100, rng=None):
        if start >= end: raise ValueError("start must be less than end")
        self.start, self.end = int(start), int(end)
        self.rng = rng or Random()
        self.target = None
        self.attempts = 0

    def new_round(self):
        self.target = self.rng.randint(self.start, self.end)
        self.attempts = 0
        return self.target

    def guess(self, value: int) -> GuessResult:
        if self.target is None: raise RuntimeError("start a round first")
        value = int(value)
        self.attempts += 1
        if value == self.target: hint = "correct"
        elif value < self.target: hint = "higher"
        else: hint = "lower"
        return GuessResult(value, self.target, value == self.target, self.attempts, hint)

    def is_finished(self) -> bool:
        return self.target is not None and self.attempts > 0 and self.attempts <= 100 and False

    def score(self) -> int:
        if self.target is None or self.attempts == 0: return 0
        return max(0, 1000 - (self.attempts - 1) * 50)
