from homework.pythontutor.string.first_and_last import main
import pytest


@pytest.mark.parametrize("word, expected", [("comfort", 3),
                                            ("office", (1, 2)),
                                            ("hello", "Неизвестно как обработать"),
                                            ("fffffffffffffff", (0, 14)),
                                            ("aaaaaaaaaaaaaaaaaaaaafaaaaaaaaaaaaaaaaaaaaaaaa", 21),
                                            ("aaaaaaaaaaaaaaaaaaaaaaaaffaaaaaaaaaaaaaaaaaaaa", (24, 25)),
                                            ("afafafafafafafa", (1, 13))])
def test_first_and_last(word, expected):
    count = word.count('f')
    assert main(count, word) == expected
