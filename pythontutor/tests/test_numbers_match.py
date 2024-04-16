from training.pythontutor.Conditions.numbers_match import match_func
import pytest


@pytest.mark.parametrize("a, b, c, expected", [(10, 5, 10, 2),
                                               (17, 17, -9, 2),
                                               (4, -82, -82, 2),
                                               (5, 2, 4, 0),
                                               (-149, -146, -142, 0),
                                               (666, 666, 666, 3)])
def test_match(a, b, c, expected):
    assert match_func(a, b, c) == expected
