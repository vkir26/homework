from training.pythontutor.Calculations.end_lessons import lessons_func
import pytest


@pytest.mark.parametrize("n, hour, minute", [(3, 11, 35),
                                             (2, 10, 35),
                                             (1, 9, 45),
                                             (4, 12, 25),
                                             (5, 13, 25),
                                             (6, 14, 15),
                                             (7, 15, 15),
                                             (8, 16, 5),
                                             (9, 17, 5),
                                             (10, 17, 55)])
def test_lessons_func(n, hour, minute):
    assert lessons_func(n) == hour, minute
