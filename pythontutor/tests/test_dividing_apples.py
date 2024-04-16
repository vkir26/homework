from training.pythontutor.DataInputAndOutput.dividing_apples import apples_func
import pytest


@pytest.mark.parametrize("n, k, expected", [(6, 50, "8\n2"),
                                            (1, 10, "10\n0"),
                                            (5, 25, "5\n0"),
                                            (4, 2, "0\n2")])
def test_apples(n, k, expected):
    assert apples_func(n, k) == expected
