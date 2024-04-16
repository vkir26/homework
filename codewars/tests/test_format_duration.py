from training.codewars.format_duration import format_duration
import pytest


@pytest.mark.parametrize("second, expected", [(1, "1 second"),
                                              (62, "1 minute and 2 seconds"),
                                              (120, "2 minutes"),
                                              (3600, "1 hour"),
                                              (3662, "1 hour, 1 minute and 2 seconds"),
                                              (132030240, "4 years, 68 days, 3 hours and 4 minutes"),
                                              (15731080, "182 days, 1 hour, 44 minutes and 40 seconds"),
                                              (421501, "4 days, 21 hours, 5 minutes and 1 second"),
                                              (0, "now"),
                                              (7077331, "81 days, 21 hours, 55 minutes and 31 seconds")])
def test_format_duration(second, expected):
    assert format_duration(second) == expected
