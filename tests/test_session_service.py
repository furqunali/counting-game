import pytest
from counting_game_core.config import GameConfig
from counting_game_core.session import CountingSession

def test_session_tracks_rounds_and_enforces_limit():
    session = CountingSession(GameConfig(max_rounds=1))
    assert session.next_sequence(3) == (1, 2, 3)
    with pytest.raises(RuntimeError):
        session.next_sequence(3)
