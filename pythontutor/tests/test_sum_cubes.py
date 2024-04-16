from training.pythontutor.cicle_for.sum_cubes import cubes_func
import pytest


@pytest.mark.parametrize("n, expected", [(3, 36),
                                         (1, 1),
                                         (2, 9),
                                         (4, 100),
                                         (5, 225),
                                         (6, 441),
                                         (7, 784),
                                         (8, 1296),
                                         (9, 2025),
                                         (20, 44100),
                                         (30, 216225)])
def test_cubes_func(n, expected):
    assert cubes_func(n) == expected
