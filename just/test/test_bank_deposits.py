from homework.just.bank_deposits import calculation_balance
from homework.just.bank_deposits import ContributionStatus
from decimal import Decimal
import pytest


@pytest.mark.parametrize("status, deposit, bet, term, year, expected",
                         [(1, 50000, 16, 30, 366, 656),
                          (1, 3000, 4.8, 182, 366, 72),
                          (1, 50000, 4, 91, 365, 499),
                          (1, 20000, 4, 730, 365, 1600),
                          (2, 50000, 4, 30, 366, 164),
                          (2, 70000, 4, 91, 366, 699),
                          (2, 100000, 4, 730, 366, 8304)])
def test_calculation_balance(status, deposit, bet: Decimal, term, year, expected):
    assert (calculation_balance(ContributionStatus(status), deposit, bet, term, year) == expected)
