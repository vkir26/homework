from training.pythontutor.cicle_for.factorial import factorial_func
import pytest


@pytest.mark.parametrize("n, expected", [(4, 24),
                                         (1, 1),
                                         (2, 2),
                                         (3, 6),
                                         (5, 120),
                                         (6, 720),
                                         (7, 5040),
                                         (8, 40320),
                                         (9, 362880),
                                         (10, 3628800),
                                         (11, 39916800),
                                         (12, 479001600)])
def test_factorial_func(n, expected):
    assert factorial_func(n) == expected
