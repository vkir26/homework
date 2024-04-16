from training.pythontutor.cicle_for.sum_n_number import sum_n
import pytest


@pytest.mark.parametrize("result, expected", [([1, 2, 1, 1, 1, 1, 3, 1, 1, 1], 13),
                                              ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 55),
                                              ([8, 4, 5, 3, 9, 2, 3, 4, 5, 1], 44),
                                              ([758, 483, 893, 393, 293, 292, 292, 485, 828, 182], 4899),
                                              ([-1, -2, -3, -4, -5, -6, -7, -8, -9, 0], -45),
                                              ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0),
                                              ([891], 891),
                                              ([235, 56], 291),
                                              ([1, 2, 3], 6),
                                              ([4, 4, 4, 4], 16),
                                              ([0], 0)])
def test_sum_n(result, expected):
    assert sum_n(result) == expected
