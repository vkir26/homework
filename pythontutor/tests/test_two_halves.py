from training.pythontutor.string.two_halves import halves
import pytest


@pytest.mark.parametrize("line, expected", [('Hi', 'iH'),
                                            ('Hello', 'loHel'),
                                            ('Qwerty', 'rtyQwe'),
                                            ('Z', 'Z'),
                                            ('asdfghj', 'ghjasdf'),
                                            ('asdfghjzxc', 'hjzxcasdfg')])
def test_two_halves(line, expected):
    assert halves(line) == expected
