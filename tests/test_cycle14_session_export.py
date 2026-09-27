import pytest
from counting_game_core.export import session_record

def test_session_record_counts_rounds():
    assert session_record([True, False], 12) == {"rounds": 2, "correct": 1, "incorrect": 1, "accuracy": 0.5, "points": 12}

def test_session_record_rejects_non_boolean():
    with pytest.raises(TypeError):
        session_record([1])
