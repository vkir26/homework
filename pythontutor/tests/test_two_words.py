from homework.pythontutor.string.two_words import permutation
import pytest


@pytest.mark.parametrize("line, expected", [('Hello, world!', 'world! Hello,'),
                                            ('A B', 'B A'),
                                            ('Q WERRTYUIOP', 'WERRTYUIOP Q'),
                                            ('QWERTYUIOP M', 'M QWERTYUIOP'),
                                            ('sadfahsjkldfhasjkdfhaklsjdfhjkl asdlkfhasdjklfhaslkdfjhalskdfgalsdf',
                                             'asdlkfhasdjklfhaslkdfjhalskdfgalsdf sadfahsjkldfhasjkdfhaklsjdfhjkl')])
def test_two_words(line, expected):
    assert permutation(line) == expected
