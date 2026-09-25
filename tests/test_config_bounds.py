import pytest
from counting_game_core.config import GameConfig

def test_sequence_rejects_values_outside_configured_bounds():
    with pytest.raises(ValueError):
        GameConfig(start=1, end=5).sequence(6)

def test_descending_config_requires_matching_direction():
    with pytest.raises(ValueError):
        GameConfig(start=1, end=10, step=-1)
