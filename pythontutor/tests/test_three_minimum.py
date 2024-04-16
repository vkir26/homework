from training.pythontutor.Conditions.three_minimum import min_three
import pytest


@pytest.mark.parametrize("a, b, c, expected", [(3, 7, 5, 3),
                                               (6, 7, 10, 6),
                                               (15, -8, -8, -8),
                                               (-15, -8, -15, -15),
                                               (99, -5, 50, -5)])
def test_min_three(a, b, c, expected):
    assert min_three(a, b, c) == expected
