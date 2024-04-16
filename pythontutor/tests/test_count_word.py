from training.pythontutor.string.count_word import count_word
import pytest


@pytest.mark.parametrize("word, expected", [('Hello world', 2),
                                            ('Hello', 1),
                                            ('q w e', 3),
                                            ('In the hole in the ground there lived a hobbit', 10),
                                            ('One two three four five', 5)])
def test_count_word(word, expected):
    assert count_word(word) == expected
