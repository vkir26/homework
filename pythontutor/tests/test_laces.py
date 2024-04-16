from training.pythontutor.DataInputAndOutput.laces import laces_func
import pytest


@pytest.mark.parametrize("a, b, l, n, expected", [(2, 1, 3, 4, 26),
                                                  (1, 1, 1, 1, 3),
                                                  (10, 20, 30, 40, 2410),
                                                  (4, 3, 2, 1, 8),
                                                  (100, 10, 98, 99, 21856),
                                                  (54, 32, 51, 96, 16496)])
def test_laces_func(a, b, l, n, expected):
    assert laces_func(a, b, l, n) == expected
