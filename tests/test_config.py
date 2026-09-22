import pytest
from counting_game_core.config import GameConfig

def test_config_defaults_are_valid():
    assert GameConfig() == GameConfig(1, 100, 10)

def test_config_rejects_invalid_range():
    with pytest.raises(ValueError): GameConfig(start=5, end=5)

def test_config_rejects_invalid_rounds():
    with pytest.raises(ValueError): GameConfig(max_rounds=0)
