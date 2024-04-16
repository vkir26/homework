from training.pythontutor.Conditions.king_move import king_move
import pytest


@pytest.mark.parametrize("x1, x2, y1, y2, expected", [(4, 4, 5, 5, 'YES'),
                                                      (4, 4, 5, 4, 'YES'),
                                                      (4, 4, 5, 3, 'YES'),
                                                      (4, 4, 4, 5, 'YES'),
                                                      (4, 4, 3, 5, 'YES'),
                                                      (4, 4, 4, 3, 'YES'),
                                                      (4, 4, 3, 4, 'YES'),
                                                      (4, 4, 3, 3, 'YES'),
                                                      (1, 1, 1, 8, 'NO'),
                                                      (1, 1, 8, 8, 'NO'),
                                                      (1, 1, 8, 1, 'NO'),
                                                      (1, 8, 8, 8, 'NO'),
                                                      (1, 8, 8, 1, 'NO'),
                                                      (1, 8, 1, 1, 'NO'),
                                                      (8, 8, 8, 1, 'NO'),
                                                      (8, 8, 1, 1, 'NO'),
                                                      (8, 8, 1, 8, 'NO'),
                                                      (8, 1, 1, 1, 'NO'),
                                                      (8, 1, 1, 8, 'NO'),
                                                      (8, 1, 8, 8, 'NO'),
                                                      (1, 1, 1, 2, 'YES'),
                                                      (1, 1, 2, 2, 'YES'),
                                                      (1, 1, 2, 1, 'YES'),
                                                      (4, 4, 6, 6, 'NO'),
                                                      (4, 4, 2, 2, 'NO'),
                                                      (4, 4, 6, 2, 'NO'),
                                                      (4, 4, 2, 6, 'NO'),
                                                      (4, 4, 2, 7, 'NO'),
                                                      (4, 4, 4, 6, 'NO'),
                                                      (4, 4, 2, 4, 'NO'),
                                                      (4, 4, 5, 6, 'NO'),
                                                      (1, 7, 1, 8, 'YES'),
                                                      (4, 3, 2, 2, 'NO')])
def test_king_move(x1, x2, y1, y2, expected):
    assert king_move(x1, x2, y1, y2) == expected
