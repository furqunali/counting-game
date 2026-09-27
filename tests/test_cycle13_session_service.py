import pytest
from counting_game_core.config import GameConfig
from counting_game_core.session import CountingSession

def test_session_rejects_recording_beyond_configured_rounds():
    session = CountingSession(config=GameConfig(max_rounds=1))
    session.record(True)
    with pytest.raises(RuntimeError):
        session.record(False)
