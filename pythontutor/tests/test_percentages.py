from training.pythontutor.Calculations.percentages import percentages_func
import pytest


@pytest.mark.parametrize("P, X, Y, expected", [(12, 179, 0, 200.48),
                                               (13, 179, 0, 202.27),
                                               (10, 100, 0, 110.0),
                                               (100, 100, 0, 200.0),
                                               (100, 17, 34, 34.68),
                                               (17, 94, 41, 110.45),
                                               (23, 19382, 23, 23840.14),
                                               (17, 35, 87, 41.96),
                                               (1, 1, 99, 2.0)])
def test_digit_func(P, X, Y, expected):
    assert percentages_func(P, X, Y) == expected
