from training.pythontutor.cicle_for.row_1 import row1
import pytest


@pytest.mark.parametrize("A, B, expected", [(1, 10, "1 2 3 4 5 6 7 8 9 10"),
                                            (-3, 14, "-3 -2 -1 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14"),
                                            (0, 0, "0"),
                                            (20, 20, "20")])
def test_row1(A, B, expected):
    assert row1(A, B) == expected
