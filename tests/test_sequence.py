import pytest

from counting_game_core.sequence import counting_sequence, sequence_until

def test_counting_sequence_builds_arithmetic_values():
    assert counting_sequence(3, 5, 4) == (3, 8, 13, 18)

def test_sequence_until_supports_descending_values():
    assert tuple(sequence_until(10, -2, 4)) == (10, 8, 6, 4)

@pytest.mark.parametrize("args", [(1, 0, 3), (1, 2, 0)])
def test_counting_sequence_rejects_invalid_configuration(args):
    with pytest.raises(ValueError):
        counting_sequence(*args)

def test_sequence_until_rejects_zero_step():
    with pytest.raises(ValueError):
        tuple(sequence_until(1, 0, 5))
