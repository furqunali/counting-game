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

    def record(self, correct: bool, points: int = 0) -> None:
        if not isinstance(correct, bool):
            raise TypeError("correct must be a boolean")
        if self._rounds >= self.config.max_rounds:
            raise RuntimeError("maximum rounds reached")
        if isinstance(points, bool) or not isinstance(points, int):
            raise TypeError("points must be an integer")
        self._results.append(correct)
        self._points += points
        self._rounds += 1

    def next_sequence(self, length: int) -> tuple[int, ...]:
        if self._rounds >= self.config.max_rounds:
            raise RuntimeError("maximum rounds reached")
        return self.config.sequence(length)
