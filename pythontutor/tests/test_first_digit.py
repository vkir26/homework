from training.pythontutor.Calculations.first_digit import digit_func
import math
import pytest


@pytest.mark.parametrize("x, expected", [(1.79, 7),
                                         (10.34, 3),
                                         (0.001, 0),
                                         (179, 0),
                                         (19.99, 9),
                                         (179.12, 1),
                                         (5.29, 2),
                                         (0.31, 3),
                                         (12.45, 4),
                                         (18.58, 5),
                                         (0.83, 8),
                                         (999.99, 9),
                                         (146.67, 6),
                                         (1293.73, 7),
                                         (0.09999, 0),
                                         (312.19999, 1),
                                         (901.29999, 2),
                                         (3.39999, 3),
                                         (2371.49999, 4),
                                         (290.59999, 5),
                                         (90291.69999, 6),
                                         (412.79999, 7),
                                         (1.89999, 8),
                                         (0.999999, 9)])
def test_digit_func(x, expected):
    assert math.isclose(digit_func(x), expected)
