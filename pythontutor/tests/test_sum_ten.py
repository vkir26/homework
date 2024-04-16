from training.pythontutor.cicle_for.sum_ten import sum_ten
import pytest


@pytest.mark.parametrize("result, expected", [([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 45),
                                              ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10),
                                              ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 55),
                                              ([8, 4, 5, 3, 9, 2, 3, 4, 5, 1], 44),
                                              ([758, 483, 893, 393, 293, 292, 292, 485, 828, 182], 4899),
                                              ([-1, -2, -3, -4, -5, -6, -7, -8, -9, 0], -45),
                                              ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0)])
def test_sum_ten(result, expected):
    assert sum_ten(result) == expected
