from training.pythontutor.Calculations.car_rally import car_rally
import pytest


@pytest.mark.parametrize("n, m, expected", [(700, 750, 2),
                                            (700, 2100, 3),
                                            (10, 15, 2),
                                            (10, 16, 2),
                                            (10, 19, 2),
                                            (10, 70, 7),
                                            (10, 81, 9),
                                            (10, 1000, 100),
                                            (10, 1001, 101),
                                            (10, 999, 100),
                                            (10, 1, 1),
                                            (10, 9, 1),
                                            (483, 9382, 20),
                                            (123, 234234, 1905)])
def test_purchase_price(n, m, expected):
    assert car_rally(n, m) == expected
