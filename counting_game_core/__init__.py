"""Public API for the counting game domain package."""

from .analytics import SessionStats, accuracy, longest_correct_streak
from .persistence import session_from_json, session_to_json
from .session import CountingSession
from .session_metrics import session_metrics
from .sequence import counting_sequence, sequence_until

__all__ = [
    "SessionStats", "CountingSession", "accuracy", "longest_correct_streak",
    "session_metrics", "counting_sequence", "sequence_until",
    "session_to_json", "session_from_json",
]
