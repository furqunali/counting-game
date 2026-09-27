import pytest
from counting_game_core.config import GameConfig
from counting_game_core.session import CountingSession

def test_session_tracks_rounds_and_sequences():
    session = CountingSession(GameConfig(start=2, end=20, max_rounds=2, step=3))
    assert session.next_sequence(3) == (2, 5, 8)
    assert session.rounds_played == 1

def test_session_enforces_round_limit():
    session = CountingSession(GameConfig(max_rounds=1))
    session.next_sequence(1)
    with pytest.raises(RuntimeError):
        session.next_sequence(1)
