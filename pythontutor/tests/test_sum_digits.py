from training.pythontutor.Calculations.sum_digits import sum_digits
import pytest


@pytest.mark.parametrize("x, expected", [(179, 17),
                                         (829, 19),
                                         (204, 6),
                                         (100, 1),
                                         (999, 27),
                                         (483, 15)])
def test_sum_digits(x, expected):
    assert sum_digits(x) == expected
