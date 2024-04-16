from training.pythontutor.Conditions.two_minimum import min_two
import pytest


@pytest.mark.parametrize("a, b, expected", [(3, 7, 3),
                                            (2, 2, 2),
                                            (15, -8, -8),
                                            (-15, -8, -15)])
def test_min_two(a, b, expected):
    assert min_two(a, b) == expected
