from training.codewars.best_friend import best_friend
import pytest


@pytest.mark.parametrize("txt, a, b, expected", [('he headed to the store', 'h', 'e', True),
                                                 ('i found an ounce with my hound', 'o', 'u', True),
                                                 ('those were their thorns they said', 't', 'h', True),
                                                 ('we found your dynamite', 'd', 'y', False),
                                                 ('look they took the cookies', 'o', 'o', False),
                                                 ('a test', 't', 'e', False),
                                                 ('abcdee', 'e', 'e', False),
                                                 ('abcde', 'e', 'e', False),
                                                 ('ucwoo aaim', 'b', 'g', True),
                                                 ('jhbuqa webf vzn', 'j', 't', False),
                                                 ('qqxhb wxhixhhc dsxhdjxh nxhdxhpwxh xxhknxhy exh', 'x', 'h', False),
                                                 ('gz b mrmqb wo dpjnp', 'a', 'j', True),
                                                 ('up scuifh f ui nb foqqu', 'n', 'e', False),
                                                 ('cvxklc lujnt gryr', 'n', 't', True),
                                                 ('cyfkhuv', 'u', 'v', True),
                                                 ('fmubwch ex', 'w', 'c', True)])
def test_best_friend(txt, a, b, expected):
    assert best_friend(txt, a, b) == expected
