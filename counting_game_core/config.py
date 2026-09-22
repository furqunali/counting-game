from dataclasses import dataclass

@dataclass(frozen=True)
class GameConfig:
    """Validated configuration for a counting-game session."""
    start: int = 1
    end: int = 100
    max_rounds: int = 10
    step: int = 1

    def __post_init__(self):
        for name, value in (("start", self.start), ("end", self.end), ("max_rounds", self.max_rounds), ("step", self.step)):
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError(f"{name} must be an integer")
        if self.start >= self.end:
            raise ValueError("start must be less than end")
        if self.max_rounds < 1:
            raise ValueError("max_rounds must be positive")
        if self.step == 0:
            raise ValueError("step must not be zero")

    def sequence(self, length: int) -> tuple[int, ...]:
        """Generate the configured counting sequence for a round."""
        if isinstance(length, bool) or not isinstance(length, int):
            raise TypeError("length must be an integer")
        if length < 1:
            raise ValueError("length must be positive")
        return tuple(self.start + index * self.step for index in range(length))
