import pytest
from counting_game_core.audit import audit_rounds

def test_audit_rounds_summarizes_accuracy_and_streak():
    assert audit_rounds([True, True, False, True]) == {"total": 4, "correct": 3, "incorrect": 1, "accuracy": 0.75, "longest_streak": 2}

def test_audit_rounds_rejects_non_boolean():
    with pytest.raises(TypeError):
        audit_rounds([1])
