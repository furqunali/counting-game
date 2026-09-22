from collections.abc import Iterable


def session_metrics(results: Iterable[bool]) -> dict[str, int]:
    """Summarize correct, incorrect, and total rounds for a session."""
    correct = incorrect = 0
    for result in results:
        if not isinstance(result, bool):
            raise TypeError("results must contain booleans")
        if result:
            correct += 1
        else:
            incorrect += 1
    return {"correct": correct, "incorrect": incorrect, "total": correct + incorrect}
