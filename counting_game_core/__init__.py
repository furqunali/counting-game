"""Public API for the counting game domain package."""

from .analytics import SessionStats, accuracy, longest_correct_streak
from .session import CountingSession
from .session_metrics import session_metrics
from .sequence import counting_sequence, sequence_until

__all__ = [
    "SessionStats", "CountingSession", "accuracy", "longest_correct_streak",
    "session_metrics", "counting_sequence", "sequence_until",
]
