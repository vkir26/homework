from homework.codewars.leap_years import is_leap_year
import pytest


@pytest.mark.parametrize("year, expected", [(2023, False),
                                            (2020, True),
                                            (2000, True),
                                            (2015, False),
                                            (2100, False),
                                            (1900, False)])
def test_leap_years(year, expected):
    assert is_leap_year(year) == expected
