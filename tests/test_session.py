import json

import pytest

from counting_game_core.session import CountingSession
from counting_game_core.persistence import session_from_json, session_to_json


def test_session_records_results_and_points():
    session = CountingSession()
    session.record(True, 100)
    session.record(False, 0)
    stats = session.stats()
    assert stats.rounds == 2
    assert stats.correct == 1
    assert stats.accuracy == 0.5
    assert stats.points == 100


def test_session_limits_rounds():
    session = CountingSession()
    session.record(True)
    assert session.can_start(2)


def test_session_completion_tracks_configured_limit():
    session = CountingSession()
    assert not session.is_complete
    for _ in range(session.config.max_rounds):
        session.record(False)
    assert session.rounds_remaining == 0
    assert session.is_complete


def test_session_json_round_trip_preserves_state():
    session = CountingSession()
    session.record(True, 125)
    session.record(False, 10)

    restored = session_from_json(session_to_json(session))

    assert restored.results == session.results
    assert restored.points == session.points
    assert restored.config == session.config


def test_session_json_rejects_non_object_payload():
    with pytest.raises(ValueError, match="session payload must contain an object"):
        session_from_json(json.dumps([]))
