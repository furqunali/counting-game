import pytest
from counting_game_core.session_lifecycle import session_outcome

def test_session_outcome_counts_results():
    assert session_outcome([True, False, True]) == {"rounds": 3, "correct": 2, "incorrect": 1, "completion_rate": 2 / 3}

def test_session_outcome_rejects_non_boolean():
    with pytest.raises(TypeError):
        session_outcome([1, False])
