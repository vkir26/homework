from training.pythontutor.Calculations.purchase_price import purchase_price
import pytest


@pytest.mark.parametrize("a, b, n, expected", [(10, 15, 2, 20.30),
                                               (2, 50, 4, 10.0),
                                               (3000, 99, 3000, 9002970.0),
                                               (2029, 34, 1848, 3750220.32),
                                               (1886, 73, 295, 556585.35),
                                               (1069, 40, 1967, 2103509.80),
                                               (905, 79, 496, 449271.84),
                                               (1967, 91, 926, 1822284.66),
                                               (2255, 76, 1090, 2458778.40),
                                               (2435, 6, 1965, 4784892.90)])
def test_purchase_price(a, b, n, expected):
    assert purchase_price(a, b, n) == expected
