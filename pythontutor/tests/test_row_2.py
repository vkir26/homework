from training.pythontutor.cicle_for.row_2 import row2
import pytest


@pytest.mark.parametrize("A, B, expected", [(1, 10, "1 2 3 4 5 6 7 8 9 10"),
                                            (10, 1, "10 9 8 7 6 5 4 3 2 1"),
                                            (179, 179, "179"),
                                            (-14, 21,
                                             "-14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 "
                                             "11 12 13 14 15 16 17 18 19 20 21"),
                                            (12, -5, "12 11 10 9 8 7 6 5 4 3 2 1 0 -1 -2 -3 -4 -5"),
                                            (-3, -7, "-3 -4 -5 -6 -7")])
def test_row1(A, B, expected):
    assert row2(A, B) == expected
