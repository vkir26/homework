from homework.pythontutor.string.deleting_fragment import del_fragment
import pytest


@pytest.mark.parametrize('proposal, result', [("In the hole in the ground there lived a hobbit", "In tobbit"),
                                              ("qwertyhasdfghzxcvb", "qwertyzxcvb"),
                                              ("asdfghhzxcvb", "asdfgzxcvb"),
                                              ("ahahahahaha", "aa"),
                                              ("haaaaaaaaaaaaaaaaaah", ""),
                                              ("hh", ""),
                                              ("ahaha", "aa")])
def test_del_fragment(proposal, result):
    assert del_fragment(proposal) == result
