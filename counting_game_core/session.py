from .config import GameConfig

class CountingSession:
    """Stateful service boundary for configured counting rounds."""
    def __init__(self, config: GameConfig):
        if not isinstance(config, GameConfig):
            raise TypeError("config must be a GameConfig")
        self.config = config
        self._rounds = 0
    @property
    def rounds_played(self) -> int:
        return self._rounds
    def next_sequence(self, length: int) -> tuple[int, ...]:
        if self._rounds >= self.config.max_rounds:
            raise RuntimeError("maximum rounds reached")
        self._rounds += 1
        return self.config.sequence(length)