from training.pythontutor.Conditions.leap import leap_func
import pytest


@pytest.mark.parametrize("year, expected", [(2012, "YES"),
                                            (2011, "NO"),
                                            (1492, "YES"),
                                            (1861, "NO"),
                                            (1600, "YES"),
                                            (1700, "NO"),
                                            (1800, "NO"),
                                            (1900, "NO"),
                                            (2000, "YES")])
def test_min_three(year, expected):
    assert leap_func(year) == expected
