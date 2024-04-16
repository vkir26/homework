from training.pythontutor.DataInputAndOutput.area_triangle import triangle
import pytest


@pytest.mark.parametrize("b, h, expected", [(3, 5, 7.5),
                                            (10, 2, 10.0),
                                            (179, 1534, 137293.0),
                                            (1543, 57, 43975.5)])
def test_triangle(b, h, expected):
    assert triangle(b, h) == expected
