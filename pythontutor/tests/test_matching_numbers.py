from training.pythontutor.Conditions.matching_numbers import matching_func
import pytest


@pytest.mark.parametrize("a, b, c, expected", [(7, 7, 5, 2),
                                               (10, 7, 10, 2),
                                               (-8, -8, -8, 3),
                                               (-15, -8, -15, 2),
                                               (99, 99, 99, 3),
                                               (55, 11, 21, 0)])
def test_min_three(a, b, c, expected):
    assert matching_func(a, b, c) == expected
