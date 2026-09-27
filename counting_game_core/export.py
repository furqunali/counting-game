from collections.abc import Iterable

def session_record(results: Iterable[bool], points: int = 0) -> dict[str, int | float]:
    """Convert round outcomes into a stable, JSON-friendly session record."""
    if isinstance(points, bool) or not isinstance(points, int):
        raise TypeError("points must be an integer")
    total = correct = 0
    for result in results:
        if not isinstance(result, bool):
            raise TypeError("results must contain booleans")
        total += 1
        correct += int(result)
    return {"rounds": total, "correct": correct, "incorrect": total - correct,
            "accuracy": correct / total if total else 0.0, "points": points}
