from training.pythontutor.DataInputAndOutput.next_previous import next_func
import pytest


@pytest.mark.parametrize("digit, expected", [(1534, "The next number for the number 1534 is 1535."
                                                    "\nThe previous number for the number 1534 is 1533."),
                                             (0, "The next number for the number 0 is 1."
                                              "\nThe previous number for the number 0 is -1."),
                                             (2718281828904590, "The next number for the number 2718281828904590 is "
                                              "2718281828904591."
                                              "\nThe previous number for the number 2718281828904590 is "
                                              "2718281828904589.")])
def test_next_func(digit, expected):
    assert next_func(digit) == expected
