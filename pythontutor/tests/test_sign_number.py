from homework.pythontutor.Conditions.sign_number import sign_func
import pytest


@pytest.mark.parametrize("x, expected", [(3, 1),
                                         (6, 1),
                                         (15, 1),
                                         (-15, -1),
                                         (9975, 1),
                                         (-7, -1),
                                         (0, 0)])
def test_min_three(x, expected):
    assert sign_func(x) == expected
