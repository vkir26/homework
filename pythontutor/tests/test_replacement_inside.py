from homework.pythontutor.string.replacement_inside import replacement
import pytest


@pytest.mark.parametrize('word, result', [('qwertyhahsdhfghzxcvb', 'qwertyhaHsdHfghzxcvb'),
                                          ('asdfghhzxcvb', 'asdfghhzxcvb'),
                                          ('ahbhchdheha', 'ahbHcHdHeha'),
                                          ('habcdefgijklmnh', 'habcdefgijklmnh'),
                                          ('hh', 'hh'),
                                          ('hah', 'hah'),
                                          ('hhh', 'hHh'),
                                          ('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh',
                                           'hHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh'),
                                          ('In the hole in the ground there lived a hobbit',
                                           'In the Hole in tHe ground tHere lived a hobbit')])
def test_replacement_inside(word, result):
    assert replacement(word) == result
