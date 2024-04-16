from training.codewars.every_digit import square_digits
import pytest


@pytest.mark.parametrize("num, expected", [(765, 493625),
                                           (9119, 811181),
                                           (0, 0)])
def test_square_digits(num, expected):
    assert square_digits(num) == expected
