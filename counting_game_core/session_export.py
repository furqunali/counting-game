from collections.abc import Iterable
from .analytics import SessionStats

def export_session(results: Iterable[bool], points: int = 0) -> dict[str, int | float]:
    """Return a stable, JSON-friendly summary of a counting session."""
    stats = SessionStats.from_results(results, points)
    return {
        "rounds": stats.rounds,
        "correct": stats.correct,
        "incorrect": stats.incorrect,
        "accuracy": stats.accuracy,
        "points": stats.points,
    }
