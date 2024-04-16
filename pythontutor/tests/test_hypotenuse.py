from training.pythontutor.Calculations.hypotenuse import hypotenuse
import pytest
import math


@pytest.mark.parametrize("a, b, expected", [(3, 4, 5.0),
                                            (5, 12, 13.0),
                                            (1, 1, 1.41421356237),
                                            (179, 971, 987.361129476),
                                            (26, 89, 92.7200086281)])
def test_lessons_func(a, b, expected):
    assert math.isclose(hypotenuse(a, b), expected)
