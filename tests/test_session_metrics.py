import pytest

from counting_game_core.session_metrics import session_metrics


def test_session_metrics_counts_rounds():
    assert session_metrics([True, False, True]) == {"correct": 2, "incorrect": 1, "total": 3}


def test_session_metrics_handles_empty_session():
    assert session_metrics([]) == {"correct": 0, "incorrect": 0, "total": 0}


def test_session_metrics_rejects_non_boolean_values():
    with pytest.raises(TypeError):
        session_metrics([True, 1])
