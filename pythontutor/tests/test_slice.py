from homework.pythontutor.string.slice import main
import pytest


@pytest.mark.parametrize("s, expected", [('Hello', ['l', 'l', 'Hello', 'Hel', 'Hlo', 'el', 'olleH', 'olH', '5']),
                                         ('Abrakadabra', ['r', 'r', 'Abrak', 'Abrakadab', 'Arkdba', 'baaar', 'arbadakarbA', 'abdkrA', '11']),
                                         ('qwertyuiop', ['e', 'o', 'qwert', 'qwertyui', 'qetuo', 'wryip', 'poiuytrewq', 'piyrw', '10']),
                                         ('asdfghjklzxcv', ['d', 'c', 'asdfg', 'asdfghjklzx', 'adgjlxv', 'sfhkzc', 'vcxzlkjhgfdsa', 'vxljgda', '13'])])
def test_slice(s, expected):
    assert main(s) == expected
