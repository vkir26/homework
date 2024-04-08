# # Программа делает расчёт суммы начисленных процентов с минимального остатка и ежедневного остатка
# # Инструкция которой пользовался: https://www.mtsbank.ru/articles/kak-rasschitat-protsenty-po-vkladu/
# # % годовых - это процент от суммы вклада, который банк начисляет клиенту раз в год, квартал или месяц
# #     DAILY = "Ежедневный остаток"
# #     MINIMUM = "Минимальный остаток"
import math
from enum import IntEnum
from decimal import Decimal


class ContributionStatus(IntEnum):
    MINIMUM = 1
    DAILY = 2


def calculation_balance(status: ContributionStatus, deposit: int, bet: Decimal, term: int, year: int) -> Decimal:
    if status is ContributionStatus.MINIMUM:
        result = Decimal(deposit * (bet / 100) * term / year)
        return result.quantize(Decimal(1), rounding='ROUND_CEILING')
        # return math.ceil(deposit * (bet / 100) * term / year)
    elif status is ContributionStatus.DAILY:
        result = Decimal(deposit * math.pow(1 + (bet / 100) / year, term) - deposit)
        return result.quantize(Decimal(1), rounding='ROUND_FLOOR')
        # return math.floor(deposit * math.pow(1 + (bet / 100) / year, term) - deposit)


if __name__ == "__main__":
    text = (f"Что необходимо сделать?"
            f"\n1. Рассчитать 'Минимальный остаток'"
            f"\n2. Рассчитать 'Ежедневный остаток'"
            f"\nВыберете цифрой: ")
    try:
        button = int(input(text))
        d = int(input("Укажите начальную сумма вклада: "))  # ― пример: 50000

        income = (calculation_balance(ContributionStatus(button),
                                      d,
                                      Decimal(input("Укажите процентную ставку: ")),  # ― пример: 6.8
                                      int(input("Укажите срок вклада в днях: ")),  # ― пример: 30
                                      int(input("Периодичность процентной ставки в днях: "))))  # ― пример: 365

        print(f"Доход: {income}\nОбщий доход: {d + income}")

    except ValueError:
        print("Некорректное значение")
