from training.pythontutor.Conditions.rook_move import move_func
import pytest


@pytest.mark.parametrize("x1, y1, x2, y2, expected", [(4, 4, 5, 5, "NO"),
                                                      (4, 4, 5, 4, "YES"),
                                                      (4, 4, 5, 3, "NO"),
                                                      (4, 4, 4, 5, "YES"),
                                                      (4, 4, 3, 5, "NO"),
                                                      (4, 4, 4, 3, "YES"),
                                                      (4, 4, 3, 4, "YES"),
                                                      (4, 4, 3, 3, "NO"),
                                                      (1, 1, 1, 8, "YES"),
                                                      (1, 1, 8, 8, "NO"),
                                                      (1, 1, 8, 1, "YES"),
                                                      (1, 8, 8, 8, "YES"),
                                                      (1, 8, 8, 1, "NO"),
                                                      (1, 8, 1, 1, "YES"),
                                                      (8, 8, 8, 1, "YES"),
                                                      (8, 8, 1, 1, "NO"),
                                                      (8, 8, 1, 8, "YES"),
                                                      (8, 1, 1, 1, "YES"),
                                                      (8, 1, 1, 8, "NO"),
                                                      (8, 1, 8, 8, "YES"),
                                                      (1, 1, 1, 2, "YES"),
                                                      (1, 1, 2, 2, "NO"),
                                                      (1, 1, 2, 1, "YES"),
                                                      (4, 4, 6, 6, "NO"),
                                                      (4, 4, 2, 2, "NO"),
                                                      (4, 4, 6, 2, "NO"),
                                                      (4, 4, 2, 6, "NO"),
                                                      (4, 4, 2, 7, "NO"),
                                                      (4, 4, 4, 6, "YES"),
                                                      (4, 4, 2, 4, "YES"),
                                                      (1, 2, 1, 3, "YES"),
                                                      (1, 2, 3, 1, "NO"),
                                                      (2, 1, 1, 3, "NO")])
def test_min_three(x1, y1, x2, y2, expected):
    assert move_func(x1, y1, x2, y2) == expected
