from dataclasses import dataclass

@dataclass(frozen=True)
class Score:
    attempts: int
    points: int
    perfect: bool

def calculate_score(attempts: int, max_points: int = 1000, penalty: int = 50) -> Score:
    if attempts < 1: raise ValueError("attempts must be positive")
    if max_points < 0 or penalty < 0: raise ValueError("score parameters must be non-negative")
    points = max(0, max_points - (attempts - 1) * penalty)
    return Score(attempts, points, attempts == 1)
