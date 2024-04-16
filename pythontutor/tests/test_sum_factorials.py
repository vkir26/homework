from training.pythontutor.cicle_for.sum_factorials import factorial_sum
import pytest


@pytest.mark.parametrize("n, expected", [(1, 1),
                                         (2, 3),
                                         (3, 9),
                                         (4, 33),
                                         (5, 153),
                                         (6, 873),
                                         (7, 5913),
                                         (8, 46233),
                                         (9, 409113),
                                         (10, 4037913), ])
def test_factorial_sum(n, expected):
    assert factorial_sum(n) == expected
