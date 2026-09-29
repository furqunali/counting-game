from collections.abc import Iterable

def session_outcome(results: Iterable[bool]) -> dict[str, int | float]:
    """Summarize a completed session with a completion rate."""
    values = list(results)
    if any(not isinstance(value, bool) for value in values):
        raise TypeError("results must contain booleans")
    total = len(values)
    correct = sum(values)
    return {"rounds": total, "correct": correct, "incorrect": total - correct,
            "completion_rate": correct / total if total else 0.0}
