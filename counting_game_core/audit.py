from collections.abc import Iterable

def audit_rounds(results: Iterable[bool]) -> dict[str, int | float]:
    """Summarize round outcomes for audit and training feedback."""
    total = correct = streak = longest = 0
    for value in results:
        if not isinstance(value, bool):
            raise TypeError("round results must be booleans")
        total += 1
        if value:
            correct += 1
            streak += 1
            longest = max(longest, streak)
        else:
            streak = 0
    return {"total": total, "correct": correct, "incorrect": total - correct,
            "accuracy": correct / total if total else 0.0, "longest_streak": longest}
