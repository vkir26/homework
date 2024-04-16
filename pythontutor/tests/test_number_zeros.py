from training.pythontutor.cicle_for.number_zeros import num_zeros
import pytest


@pytest.mark.parametrize("n, expected", [([5, 0, 700, 0, 200, 2], 2),
                                         ([7, 1, 2, 3, 4, 5, 6, 7], 0),
                                         ([1, 0], 1),
                                         ([1, 1], 0),
                                         ([6, 0, 0, 0, 0, 0, 0], 6),
                                         ([3, 0, 1, 2], 1),
                                         ([3, 1, 2, 0], 1),
                                         ([10, 0, 4, 1, -7, 0, 4, 5, 1, 0, 0], 4)])
def test_number_zeros(n, expected):
    assert num_zeros(n) == expected
