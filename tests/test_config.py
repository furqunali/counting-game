import pytest

from counting_game_core.config import GameConfig


def test_config_generates_configured_sequence():
    assert GameConfig(start=3, end=20, step=4).sequence(4) == (3, 7, 11, 15)


def test_config_rejects_zero_step():
    with pytest.raises(ValueError):
        GameConfig(step=0)


def test_configured_session_counts_rounds_and_enforces_limit():
    from counting_game_core.config import GameConfig
    from counting_game_core.session import CountingSession
    import pytest
    session = CountingSession(GameConfig(max_rounds=1))
    assert session.next_sequence(2) == (1, 2)
    assert session.rounds_played == 1
    with pytest.raises(RuntimeError):
        session.next_sequence(1)
