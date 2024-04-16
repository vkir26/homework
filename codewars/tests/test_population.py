from training.codewars.population import nb_year
import pytest


@pytest.mark.parametrize("p0, percent, aug, p, expected", [(1500, 5, 100, 5000, 15),
                                                           (1500000, 2.5, 10000, 2000000, 10),
                                                           (1500000, 0.25, 1000, 2000000, 94),
                                                           (1000, 2, 50, 1200, 3)])
def test_nb_year(p0, percent, aug, p, expected):
    assert nb_year(p0, percent, aug, p) == expected
