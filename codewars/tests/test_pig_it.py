from training.codewars.simple_pig_latin import pig_it
import pytest


@pytest.mark.parametrize("text, expected", [('Pig latin is cool', 'igPay atinlay siay oolcay'),
                                            ('Hello world !', 'elloHay orldway !'),
                                            ('This is my string', 'hisTay siay ymay tringsay'),
                                            ('Hello , World ! My name is Vanya !', 'elloHay , orldWay ! yMay amenay siay anyaVay !'),
                                            ("O tempora o mores !", "Oay emporatay oay oresmay !")])
def test_pig_it(text, expected):
    assert pig_it(text) == expected
