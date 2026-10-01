import pytest

from counting_game_core import CountingSession
from counting_game_core.config import GameConfig


def test_session_snapshot_round_trips_state_and_config():
    session = CountingSession(
        results=[True, False, True],
        points=250,
        config=GameConfig(start=2, end=20, max_rounds=5, step=3),
    )

    restored = CountingSession.from_dict(session.to_dict())

    assert restored.results == [True, False, True]
    assert restored.points == 250
    assert restored.config == session.config
    assert restored.stats() == session.stats()


def test_session_snapshot_is_json_compatible():
    session = CountingSession(results=[True], points=100)
    snapshot = session.to_dict()

    assert snapshot == {
        "results": [True],
        "points": 100,
        "config": {"start": 1, "end": 100, "max_rounds": 10, "step": 1},
    }


@pytest.mark.parametrize("data", [None, [], "snapshot"])
def test_session_snapshot_rejects_non_dict(data):
    with pytest.raises(TypeError):
        CountingSession.from_dict(data)


def test_session_snapshot_rejects_missing_config_field():
    with pytest.raises(ValueError, match="missing config field"):
        CountingSession.from_dict(
            {
                "results": [],
                "points": 0,
                "config": {"start": 1, "end": 100, "max_rounds": 10},
            }
        )
