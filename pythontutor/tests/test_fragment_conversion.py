from homework.pythontutor.string.fragment_conversion import conversion
import pytest


@pytest.mark.parametrize('word, result', [("In the hole in the ground there lived a hobbit",
                                           "In th a devil ereht dnuorg eht ni eloh ehobbit"),
                                          ("qwertyhasdfghzxcvb", "qwertyhgfdsahzxcvb"),
                                          ("asdfghhzxcvb", "asdfghhzxcvb"),
                                          ("ahbhchdheha", "ahehdhchbha"),
                                          ("habcdefgijklmnh", "hnmlkjigfedcbah"),
                                          ("hh", "hh"),
                                          ("hah", "hah"),
                                          ("habh", "hbah"),
                                          ("ahcvbhs", "ahbvchs")])
def test_fragment_conversion(word, result):
    assert conversion(word) == result
