import pytest
from counting_game_core.history import RoundHistory, RoundRecord

def test_history_tracks_points():
    history = RoundHistory()
    history.add(RoundRecord(True, 1, 1000))
    history.add(RoundRecord(False, 2, 0))
    assert history.total_points() == 1000
    assert len(history.records()) == 2

def test_history_rejects_invalid_records():
    with pytest.raises(ValueError):
        RoundHistory().add(RoundRecord(True, 0, 10))
