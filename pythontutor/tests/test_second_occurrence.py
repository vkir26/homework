from homework.pythontutor.string.second_occurrence import second
import pytest


@pytest.mark.parametrize('word, result', [("comfort", -1),
                                          ("coffee", 3),
                                          ("qwerty", -2),
                                          ("f", -1),
                                          ("oooooooooooooooooof", -1),
                                          ("ff", 1),
                                          ("ffffffffffffffff", 1),
                                          ("foooooooooooooof", 15),
                                          ("oooooooooooooff", 14),
                                          ("ofofofofofofofofo", 3)])
def test_second(word, result):
    count = word.count('f')
    assert second(word, count) == result
