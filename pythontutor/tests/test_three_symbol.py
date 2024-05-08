from homework.pythontutor.string.three_symbol import three
import pytest


@pytest.mark.parametrize('word, result', [('ab', 'b'),
                                          ('abc', 'bc'),
                                          ('abcdefg', 'bcef'),
                                          ('abcdefgh', 'bcefh'),
                                          ('abcdefghi', 'bcefhi'),
                                          ('abcdefghij', 'bcefhi'),
                                          ('abcdefghijk', 'bcefhik'),
                                          ('abcdefghijkl', 'bcefhikl'),
                                          ('qwertyuiopasdfghjklzxcvbnm', 'wetyioasfgjkzxvbm'),
                                          ('Python', 'yton'),
                                          ('Hello', 'elo'),
                                          ('qwer', 'we'),
                                          ('a', '')])
def test_three_symbol(word, result):
    assert three(word) == result
