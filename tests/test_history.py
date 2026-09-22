import pytest
from counting_game_core.history import RoundHistory, RoundRecord
from counting_game_core.analytics import longest_correct_streak

def test_history_tracks_points():
    history = RoundHistory()
    history.add(RoundRecord(True, 1, 1000))
    history.add(RoundRecord(False, 2, 0))
    assert history.total_points() == 1000
    assert len(history.records()) == 2

def test_history_rejects_invalid_records():
    with pytest.raises(ValueError):
        RoundHistory().add(RoundRecord(True, 0, 10))

def test_longest_correct_streak():
    assert longest_correct_streak([True, True, False, True, True, True]) == 3
    assert longest_correct_streak([]) == 0

def test_longest_correct_streak_rejects_non_boolean_values():
    with pytest.raises(TypeError):
        longest_correct_streak([True, 1])
