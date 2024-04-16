from training.pythontutor.Calculations.time_difference import time_difference
import pytest


@pytest.mark.parametrize("h, m, s, h2, m2, s2, expected", [(1, 1, 1, 2, 2, 2, 3661),
                                                           (1, 2, 30, 1, 3, 20, 50),
                                                           (6, 54, 4, 14, 18, 42, 26678),
                                                           (1, 49, 28, 14, 7, 55, 44307),
                                                           (4, 16, 9, 12, 6, 7, 28198),
                                                           (7, 12, 3, 7, 45, 36, 2013),
                                                           (4, 27, 13, 12, 34, 27, 29234),
                                                           (4, 28, 51, 11, 17, 55, 24544),
                                                           (6, 6, 8, 18, 58, 45, 46357),
                                                           (0, 22, 4, 5, 28, 44, 18400)])
def test_time_difference(h, m, s, h2, m2, s2, expected):
    assert time_difference(h, m, s, h2, m2, s2) == expected
