from training.pythontutor.Conditions.bishop_move import bishop_func
import pytest


@pytest.mark.parametrize("x1, x2, y1, y2, expected", [(4, 4, 5, 5, 'YES'),
                                                      (4, 4, 5, 4, 'NO'),
                                                      (4, 4, 5, 3, 'YES'),
                                                      (4, 4, 4, 5, 'NO'),
                                                      (4, 4, 3, 5, 'YES'),
                                                      (4, 4, 4, 3, 'NO'),
                                                      (4, 4, 3, 4, 'NO'),
                                                      (4, 4, 3, 3, 'YES'),
                                                      (1, 1, 1, 8, 'NO'),
                                                      (1, 1, 8, 8, 'YES'),
                                                      (1, 1, 8, 1, 'NO'),
                                                      (1, 8, 8, 8, 'NO'),
                                                      (1, 8, 8, 1, 'YES'),
                                                      (1, 8, 1, 1, 'NO'),
                                                      (8, 8, 8, 1, 'NO'),
                                                      (8, 8, 1, 1, 'YES'),
                                                      (8, 8, 1, 8, 'NO'),
                                                      (8, 1, 1, 1, 'NO'),
                                                      (8, 1, 1, 8, 'YES'),
                                                      (8, 1, 8, 8, 'NO'),
                                                      (1, 1, 1, 2, 'NO'),
                                                      (1, 1, 2, 2, 'YES'),
                                                      (1, 1, 2, 1, 'NO'),
                                                      (4, 4, 6, 6, 'YES'),
                                                      (4, 4, 2, 2, 'YES'),
                                                      (4, 4, 6, 2, 'YES'),
                                                      (4, 4, 2, 6, 'YES'),
                                                      (4, 4, 2, 7, 'NO'),
                                                      (4, 4, 4, 6, 'NO'),
                                                      (4, 4, 2, 4, 'NO'),
                                                      (7, 4, 2, 5, 'NO'),
                                                      (7, 5, 1, 1, 'NO'),
                                                      (8, 7, 7, 6, 'YES')])
def test_bishop_func(x1, x2, y1, y2, expected):
    assert bishop_func(x1, x2, y1, y2) == expected
