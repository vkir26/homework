from training.pythontutor.Conditions.chessboard import chessboard_func
import pytest


@pytest.mark.parametrize("x1, y1, x2, y2, expected", [(1, 1, 2, 6, "YES"),
                                                      (2, 2, 2, 5, "NO"),
                                                      (3, 2, 2, 3, "YES"),
                                                      (2, 2, 2, 5, "NO"),
                                                      (8, 7, 8, 8, "NO")])
def test_min_three(x1, y1, x2, y2, expected):
    assert chessboard_func(x1, y1, x2, y2) == expected
