from .analytics import SessionStats
from .config import GameConfig


class CountingSession:
    """Stateful session service with configured round tracking."""

    def __init__(
        self,
        results: list[bool] | None = None,
        points: int = 0,
        config: GameConfig | None = None,
    ):
        self.results = list(results or [])
        self.points = max(0, int(points))
        self.config = GameConfig() if config is None else config
        if not isinstance(self.config, GameConfig):
            raise TypeError("config must be a GameConfig")
        if len(self.results) > self.config.max_rounds:
            raise ValueError("results exceed configured maximum rounds")
        if any(not isinstance(result, bool) for result in self.results):
            raise TypeError("results must contain booleans")

    @property
    def rounds_played(self) -> int:
        return len(self.results)

    @property
    def rounds_remaining(self) -> int:
        return max(0, self.config.max_rounds - self.rounds_played)

    @property
    def is_complete(self) -> bool:
        """Return whether the configured round limit has been reached."""
        return self.rounds_played >= self.config.max_rounds

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
        if next_round < 1:
            raise ValueError("next_round must be positive")
        return self.rounds_played + next_round <= self.config.max_rounds

    def next_sequence(self, length: int) -> tuple[int, ...]:
        if not self.can_start():
            raise RuntimeError("maximum rounds reached")
        sequence = self.config.sequence(length)
        self.results.append(False)
        return sequence

    def to_dict(self) -> dict[str, object]:
        """Return a JSON-compatible snapshot of the current session."""
        return {
            "results": list(self.results),
            "points": self.points,
            "config": {
                "start": self.config.start,
                "end": self.config.end,
                "max_rounds": self.config.max_rounds,
                "step": self.config.step,
            },
        }

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "CountingSession":
        """Restore a session from a snapshot produced by to_dict."""
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary")
        config_data = data.get("config")
        results = data.get("results")
        if not isinstance(config_data, dict):
            raise TypeError("config must be a dictionary")
        if not isinstance(results, list):
            raise TypeError("results must be a list")
        try:
            config = GameConfig(
                start=config_data["start"],
                end=config_data["end"],
                max_rounds=config_data["max_rounds"],
                step=config_data["step"],
            )
        except KeyError as exc:
            raise ValueError(f"missing config field: {exc.args[0]}") from exc
        return cls(results=results, points=data.get("points", 0), config=config)
