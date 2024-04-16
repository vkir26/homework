from training.pythontutor.Conditions.knight_move import knight_func
import pytest


@pytest.mark.parametrize("x1, x2, y1, y2, expected", [(1, 1, 1, 4, 'NO'),
                                                      (1, 1, 8, 8, 'NO'),
                                                      (2, 4, 3, 2, 'YES'),
                                                      (5, 2, 4, 4, 'YES'),
                                                      (2, 8, 3, 7, 'NO'),
                                                      (2, 8, 3, 5, 'NO'),
                                                      (5, 5, 3, 7, 'NO'),
                                                      (2, 4, 2, 5, 'NO'),
                                                      (4, 7, 6, 6, 'YES'),
                                                      (4, 5, 2, 4, 'YES'),
                                                      (2, 3, 3, 2, 'NO'),
                                                      (5, 1, 4, 3, 'YES'),
                                                      (6, 2, 8, 3, 'YES')])
def test_knight_func(x1, x2, y1, y2, expected):
    assert knight_func(x1, x2, y1, y2) == expected
