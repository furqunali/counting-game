import pytest
from counting_game_core.analytics import SessionStats, longest_correct_streak

def test_session_stats_rejects_non_boolean_results():
    with pytest.raises(TypeError):
        SessionStats.from_results([True, 1])

def test_longest_correct_streak_counts_consecutive_successes():
    assert longest_correct_streak([True, True, False, True, True, True]) == 3
