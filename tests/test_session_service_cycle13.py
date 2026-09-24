from counting_game_core.config import GameConfig
from counting_game_core.session import CountingSession


def test_session_can_start_respects_round_limit():
    session = CountingSession(config=GameConfig(max_rounds=1))
    assert session.can_start()
    session.record(True)
    assert not session.can_start()
