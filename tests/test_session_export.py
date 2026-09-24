from counting_game_core.session_export import export_session

def test_export_session_returns_stable_summary():
    assert export_session([True, False, True], 25) == {
        "rounds": 3, "correct": 2, "incorrect": 1, "accuracy": 2 / 3, "points": 25
    }

def test_export_session_handles_empty_session():
    assert export_session([]) == {
        "rounds": 0, "correct": 0, "incorrect": 0, "accuracy": 0.0, "points": 0
    }
