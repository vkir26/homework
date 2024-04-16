from training.pythontutor.Conditions.queen_move import queen_func
import pytest


@pytest.mark.parametrize("x1, x2, y1, y2, expected", [(1, 1, 2, 2, 'YES'),
                                                      (1, 1, 2, 3, 'NO'),
                                                      (5, 6, 3, 3, 'NO'),
                                                      (3, 3, 1, 1, 'YES'),
                                                      (6, 5, 2, 5, 'YES'),
                                                      (7, 6, 5, 2, 'NO'),
                                                      (2, 7, 6, 7, 'YES'),
                                                      (2, 7, 4, 6, 'NO'),
                                                      (7, 4, 2, 5, 'NO'),
                                                      (7, 5, 1, 1, 'NO'),
                                                      (2, 4, 5, 7, 'YES'),
                                                      (3, 5, 7, 1, 'YES'),
                                                      (5, 2, 5, 8, 'YES'),
                                                      (1, 2, 3, 1, 'NO'),
                                                      (2, 1, 1, 3, 'NO'),
                                                      (4, 5, 6, 7, 'YES')])
def test_queen_func(x1, x2, y1, y2, expected):
    assert queen_func(x1, x2, y1, y2) == expected
