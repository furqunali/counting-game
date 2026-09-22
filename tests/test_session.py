from counting_game_core.session import CountingSession

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
