from training.pythontutor.Calculations.fractional_part import fractional_part
import pytest
import math


@pytest.mark.parametrize("x, expected", [(17.9, 0.9),
                                         (10.34, 0.34),
                                         (0.001, 0.001),
                                         (179, 0),
                                         (19.99, 0.99)])
def test_fractional_part(x, expected):
    assert math.isclose(fractional_part(x), expected)
