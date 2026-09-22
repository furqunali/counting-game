import pytest
from counting_game_core.config import GameConfig

def test_config_generates_configured_sequence():
    assert GameConfig(start=3, end=20, step=4).sequence(4) == (3, 7, 11, 15)

def test_config_rejects_zero_step():
    with pytest.raises(ValueError):
        GameConfig(step=0)
