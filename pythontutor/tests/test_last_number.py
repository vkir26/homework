from training.pythontutor.Calculations.last_number import last_func
import pytest


@pytest.mark.parametrize("x, expected", [(179, 9),
                                         (40, 0),
                                         (101, 1),
                                         (222, 2),
                                         (1923, 3),
                                         (74, 4),
                                         (505, 5),
                                         (996, 6),
                                         (3487, 7),
                                         (308, 8),
                                         (1, 1),
                                         (2, 2),
                                         (3, 3),
                                         (4, 4),
                                         (5, 5),
                                         (6, 6),
                                         (7, 7),
                                         (9, 9),
                                         (10, 0)])
def test_last_func(x, expected):
    assert last_func(x) == expected
