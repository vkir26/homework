from training.pythontutor.cicle_for.ladder import ladder_func
import pytest


@pytest.mark.parametrize("n, expected", [(1, [[1]]),
                                         (2, [[1],
                                              [1, 2]]),
                                         (3, [[1],
                                              [1, 2],
                                              [1, 2, 3]]),
                                         (4, [[1],
                                              [1, 2],
                                              [1, 2, 3],
                                              [1, 2, 3, 4]]),
                                         (5, [[1],
                                              [1, 2],
                                              [1, 2, 3],
                                              [1, 2, 3, 4],
                                              [1, 2, 3, 4, 5]]),
                                         (6, [[1],
                                              [1, 2],
                                              [1, 2, 3],
                                              [1, 2, 3, 4],
                                              [1, 2, 3, 4, 5],
                                              [1, 2, 3, 4, 5, 6]]),
                                         (7, [[1],
                                              [1, 2],
                                              [1, 2, 3],
                                              [1, 2, 3, 4],
                                              [1, 2, 3, 4, 5],
                                              [1, 2, 3, 4, 5, 6],
                                              [1, 2, 3, 4, 5, 6, 7]]),
                                         (8, [[1],
                                              [1, 2],
                                              [1, 2, 3],
                                              [1, 2, 3, 4],
                                              [1, 2, 3, 4, 5],
                                              [1, 2, 3, 4, 5, 6],
                                              [1, 2, 3, 4, 5, 6, 7],
                                              [1, 2, 3, 4, 5, 6, 7, 8]]),
                                         (9, [[1],
                                              [1, 2],
                                              [1, 2, 3],
                                              [1, 2, 3, 4],
                                              [1, 2, 3, 4, 5],
                                              [1, 2, 3, 4, 5, 6],
                                              [1, 2, 3, 4, 5, 6, 7],
                                              [1, 2, 3, 4, 5, 6, 7, 8],
                                              [1, 2, 3, 4, 5, 6, 7, 8, 9]])])
def test_ladder_func(n, expected):
    assert ladder_func(n) == expected
