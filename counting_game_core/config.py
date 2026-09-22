from dataclasses import dataclass

@dataclass(frozen=True)
class GameConfig:
    """Validated configuration for a counting-game session."""
    start: int = 1
    end: int = 100
    max_rounds: int = 10

    def __post_init__(self):
        if isinstance(self.start, bool) or not isinstance(self.start, int): raise TypeError("start must be an integer")
        if isinstance(self.end, bool) or not isinstance(self.end, int): raise TypeError("end must be an integer")
        if self.start >= self.end: raise ValueError("start must be less than end")
        if isinstance(self.max_rounds, bool) or not isinstance(self.max_rounds, int): raise TypeError("max_rounds must be an integer")
        if self.max_rounds < 1: raise ValueError("max_rounds must be positive")
