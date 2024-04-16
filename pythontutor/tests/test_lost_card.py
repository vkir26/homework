from training.pythontutor.cicle_for.lost_card import lost_card
import pytest


@pytest.mark.parametrize("n, number_list, expected", [(5, [1, 2, 3, 4], 5),
                                                      (5, [3, 5, 2, 1], 4),
                                                      (4, [3, 2, 4], 1),
                                                      (3, [1, 2], 3),
                                                      (3, [3, 2], 1),
                                                      (3, [3, 1], 2),
                                                      (1, [0], 1),
                                                      (10, [4, 1, 7, 8, 3, 5, 9, 10, 6], 2)])
def test_lost_card(n, number_list, expected):
    assert lost_card(n, number_list) == expected
