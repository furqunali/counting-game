from .analytics import SessionStats
from .config import GameConfig

class CountingSession:
    """Stateful session service with configured round tracking."""

    def __init__(self, results: list[bool] | None = None, points: int = 0, config: GameConfig | None = None):
        self.results = list(results or [])
        self.points = max(0, int(points))
        self.config = GameConfig() if config is None else config
        if not isinstance(self.config, GameConfig):
            raise TypeError("config must be a GameConfig")

    @property
    def rounds_played(self) -> int:
        return len(self.results)

    def record(self, correct: bool, points: int = 0) -> SessionStats:
        if not isinstance(correct, bool):
            raise TypeError("correct must be a boolean")
        if not self.can_start():
            raise RuntimeError("maximum rounds reached")
        self.results.append(correct)
        self.points += max(0, int(points))
        return self.stats()

    def stats(self) -> SessionStats:
        return SessionStats.from_results(self.results, self.points)

    def can_start(self, next_round: int | None = None) -> bool:
        if next_round is None:
            return self.rounds_played < self.config.max_rounds
        if isinstance(next_round, bool) or not isinstance(next_round, int):
            raise TypeError("next_round must be an integer")
        return self.rounds_played + next_round <= self.config.max_rounds

    def next_sequence(self, length: int) -> tuple[int, ...]:
        if not self.can_start():
            raise RuntimeError("maximum rounds reached")
        sequence = self.config.sequence(length)
        self.results.append(False)
        return sequence
