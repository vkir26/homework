from training.pythontutor.cicle_for.row_3 import row3
import pytest


@pytest.mark.parametrize("A, B, expected", [(7, 1, "7 5 3 1"),
                                            (10, 1, "9 7 5 3 1"),
                                            (200, 186, "199 197 195 193 191 189 187"),
                                            (-18, -29, "-19 -21 -23 -25 -27 -29"),
                                            (6, 5, "5"),
                                            (1001, 1000, "1001")])
def test_row1(A, B, expected):
    assert row3(A, B) == expected
