from training.pythontutor.Calculations.number_tens import number_tens
import pytest


@pytest.mark.parametrize("x, expected", [(73, 7),
                                         (10, 1),
                                         (29, 2),
                                         (37, 3),
                                         (48, 4),
                                         (50, 5),
                                         (67, 6),
                                         (81, 8),
                                         (99, 9),
                                         (179, 7),
                                         (100, 0),
                                         (999, 9),
                                         (854345, 4),
                                         (1000000, 0),
                                         (9999, 9),
                                         (9, 0),
                                         (1, 0),
                                         (0, 0)])
def test_digit_func(x, expected):
    assert number_tens(x) == expected
