from homework.pythontutor.string.replacing_substring import substring
import pytest


@pytest.mark.parametrize('word, result', [('1+1=2', 'one+one=2'),
                                          ('1', 'one'),
                                          ('1111111111111111111111111111111111',
                                           'oneoneoneoneoneoneoneoneoneoneoneone'
                                           'oneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneoneone'),
                                          ('1213141516171819101', 'one2one3one4one5one6one7one8one9one0one'),
                                          ('Hello, 2345678990', 'Hello, 2345678990')])
def test_replacing_substring(word, result):
    assert substring(word) == result
