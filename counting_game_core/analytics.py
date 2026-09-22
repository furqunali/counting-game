from dataclasses import dataclass
from typing import Iterable

@dataclass(frozen=True)
class SessionStats:
    rounds: int
    correct: int
    incorrect: int
    accuracy: float
    points: int

    @classmethod
    def from_results(cls, results: Iterable[bool], points: int = 0):
        values = list(results)
        correct = sum(1 for value in values if value)
        rounds = len(values)
        return cls(rounds, correct, rounds - correct, correct / rounds if rounds else 0.0, int(points))

def accuracy(correct: int, rounds: int) -> float:
    if correct < 0 or rounds < 0 or correct > rounds:
        raise ValueError("invalid round counters")
    return correct / rounds if rounds else 0.0
