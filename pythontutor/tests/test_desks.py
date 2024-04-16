from training.pythontutor.DataInputAndOutput.desks import desks_func
import pytest


@pytest.mark.parametrize("a, b, c, expected", [(20, 21, 22, 32),
                                               (26, 20, 16, 31),
                                               (25, 21, 23, 36),
                                               (17, 19, 18, 28)])
def test_decks(a, b, c, expected):
    assert desks_func(a, b, c) == expected
