from training.pythontutor.DataInputAndOutput.electronic_clock import clock_func
import pytest


@pytest.mark.parametrize("n, hour, minute", [(150, 2, 30),
                                             (1441, 0, 1),
                                             (444, 7, 24),
                                             (180, 3, 0),
                                             (1439, 23, 59),
                                             (1440, 0, 0),
                                             (2000, 9, 20),
                                             (3456, 9, 36),
                                             (5678, 22, 38),
                                             (9876, 20, 36)])
def test_best_friend(n, hour, minute):
    assert clock_func(n) == (hour, minute)
