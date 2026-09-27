import pytest
from counting_game_core.config import GameConfig
from counting_game_core.session import CountingSession

def test_remaining_rounds_tracks_recorded_results():
    session = CountingSession(results=[True, False], config=GameConfig(max_rounds=5))
    assert session.rounds_remaining == 3

def test_can_start_rejects_nonpositive_round_count():
    session = CountingSession(config=GameConfig(max_rounds=3))
    with pytest.raises(ValueError):
        session.can_start(0)
