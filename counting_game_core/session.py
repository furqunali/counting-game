from .analytics import SessionStats
from .config import GameConfig

class CountingSession:
    """Stateful service boundary for configured counting rounds."""

    def __init__(self, config: GameConfig | None = None):
        self.config = config or GameConfig()
        if not isinstance(self.config, GameConfig):
            raise TypeError("config must be a GameConfig")
        self._rounds = 0
        self._results: list[bool] = []
        self._points = 0

    @property
    def rounds_played(self) -> int:
        return self._rounds

    @property
    def stats(self) -> SessionStats:
        return SessionStats.from_results(self._results, self._points)

    def can_start(self) -> bool:
        return self._rounds < self.config.max_rounds

    def record(self, correct: bool, points: int = 0) -> None:
        if not isinstance(correct, bool):
            raise TypeError("correct must be a boolean")
        if not self.can_start():
            raise RuntimeError("maximum rounds reached")
        if isinstance(points, bool) or not isinstance(points, int):
            raise TypeError("points must be an integer")
        self._results.append(correct)
        self._points += points
        self._rounds += 1

    def next_sequence(self, length: int) -> tuple[int, ...]:
        if not self.can_start():
            raise RuntimeError("maximum rounds reached")
        self._rounds += 1
        return self.config.sequence(length)
