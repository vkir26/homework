from training.pythontutor.DataInputAndOutput.hello_name import hello
import pytest


@pytest.mark.parametrize("text, expected", [("Harry", "Hello, Harry!"),
                                            ("Mr. Potter", "Hello, Mr. Potter!"),
                                            ("Lord Voldemort", "Hello, Lord Voldemort!")])
def test_hello(text, expected):
    assert hello(text) == expected
