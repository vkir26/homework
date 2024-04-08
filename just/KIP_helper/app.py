import math
from enum import IntEnum


class ContributionStatus(IntEnum):
    MINIMUM = 1
    DAILY = 2


def calculation_balance(status: ContributionStatus, deposit: int, bet: float, term: int, year: int) -> int:
    match status:
        case ContributionStatus.MINIMUM:
            return math.ceil(deposit * (bet / 100) * term / year)
        case ContributionStatus.DAILY:
            return math.floor(deposit * math.pow(1 + (bet / 100) / year, term) - deposit)


if __name__ == "__main__":
    helo_text = (
        f"Что необходимо сделать?\n1. Рассчитать 'Минимальный остаток'\n2. Рассчитать 'Ежедневный "
        f"остаток'\nВыберете цифрой:"
    )
    try:
        s = ContributionStatus(input(helo_text))
        d = int(input("Укажите начальную сумма вклада: "))
        b = float(input("Укажите процентную ставку: "))
        t = int(input("Укажите срок вклада в днях: "))
        y = int(input("Укажите количество дней в году: "))
    except ValueError:
        raise ValueError("Выбран некорректный вариант")

    income = calculation_balance(s, d, b, t, y)

    print(f"Доход: {income}\nОбщий доход: {d + income}")