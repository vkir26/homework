from homework.pythontutor.string.deleting_character import character
import pytest


@pytest.mark.parametrize('word, result',
                         [('Bilbo.Baggins@bagend.hobbiton.shire.me', 'Bilbo.Bagginsbagend.hobbiton.shire.me'),
                          ("dfa;sdkfj;ajva;bvna'sdasdfasdglJLHJKFHLDKJFh",
                           "dfa;sdkfj;ajva;bvna'sdasdfasdglJLHJKFHLDKJFh"),
                          ('@', ''),
                          ('@@@@@@@@@@', ''),
                          ('@W@E@E@E@R', 'WEEER'),
                          ('H@K@M@J@M@L', 'HKMJML'),
                          ('@@@@@F@@@@KL@@@@@J@J@J@JJJH@JJKK@JJJ@JJ', 'FKLJJJJJJHJJKKJJJJJ')])
def test_deleting_character(word, result):
    assert character(word) == result
