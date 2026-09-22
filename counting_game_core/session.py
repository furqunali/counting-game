from dataclasses import dataclass, field
from .analytics import SessionStats
from .validation import validate_rounds

@dataclass
class CountingSession:
    results: list[bool] = field(default_factory=list)
    points: int = 0

    def record(self, correct: bool, points: int = 0) -> SessionStats:
        self.results.append(bool(correct))
        self.points += max(0, int(points))
        return self.stats()

    def stats(self) -> SessionStats:
        return SessionStats.from_results(self.results, self.points)

    def can_start(self, rounds: int) -> bool:
        return len(self.results) < validate_rounds(rounds)
