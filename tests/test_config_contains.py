import pytest
from counting_game_core.config import GameConfig

def test_contains_checks_inclusive_bounds():
    config = GameConfig(start=2, end=8, step=2)
    assert config.contains(2)
    assert config.contains(8)
    assert not config.contains(9)

def test_contains_rejects_non_integer_values():
    with pytest.raises(TypeError):
        GameConfig().contains(True)
