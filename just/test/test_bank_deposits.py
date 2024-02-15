from homework.just.bank_deposits import calculation_balance
import pytest

daily = "Ежедневный остаток"
minimum = "Минимальный остаток"


@pytest.mark.parametrize("on, d, i, t, y, expected", [(minimum, 50000, 16, 30, 366, 'Доход: 656\nОбщий доход: 50656'),
                                                      (minimum, 3000, 4.8, 182, 366, 'Доход: 72\nОбщий доход: 3072'),
                                                      (minimum, 50000, 4, 91, 365, 'Доход: 499\nОбщий доход: 50499'),
                                                      (minimum, 20000, 4, 730, 365, 'Доход: 1600\nОбщий доход: 21600'),
                                                      (daily, 50000, 4, 30, 366, 'Доход: 164\nОбщий доход: 50164'),
                                                      (daily, 70000, 4, 91, 366, 'Доход: 699\nОбщий доход: 70699'),
                                                      (daily, 100000, 4, 730, 366, 'Доход: 8304\nОбщий доход: 108304')])
def test_calculation_balance(on, d, i, t, y, expected):
    if on == minimum or on == daily:
        assert (calculation_balance(on, d, i, t, y) == expected)
