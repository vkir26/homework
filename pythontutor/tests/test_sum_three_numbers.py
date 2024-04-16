from training.pythontutor.DataInputAndOutput.sum_three_numbers import sum_three
import pytest


@pytest.mark.parametrize("a, b, c, expected", [(2, 3, 6, 11),
                                               (0, 20, 300, 320),
                                               (-5, 180, -17, 158)])
def test_sum_three(a, b, c, expected):
    assert sum_three(a, b, c) == expected
