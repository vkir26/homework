from training.pythontutor.Calculations.mkad import mkad
import pytest


@pytest.mark.parametrize("v, t, expected", [(60, 2, 11),
                                            (-1, 1, 108),
                                            (100, 10, 19),
                                            (-108, 109, 0),
                                            (-60, 4, 87),
                                            (73, 28, 82)])
def test_lessons_func(v, t, expected):
    assert mkad(v, t) == expected
