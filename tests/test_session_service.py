import pytest

from counting_game_core.config import GameConfig
from counting_game_core.session import CountingSession


def test_session_previews_sequence_without_recording():
    session = CountingSession(GameConfig(start=2, end=20, max_rounds=2, step=3))
    assert session.next_sequence(3) == (2, 5, 8)
    assert session.rounds_played == 0


def test_session_enforces_round_limit():
    session = CountingSession(config=GameConfig(max_rounds=1))
    session.record(True)
    with pytest.raises(RuntimeError):
        session.record(False)
