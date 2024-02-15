# Программа делает расчёт суммы начисленных процентов с минимального остатка и ежедневного остатка
# Инструкция которой пользовался: https://www.mtsbank.ru/articles/kak-rasschitat-protsenty-po-vkladu/
# % годовых - это процент от суммы вклада, который банк начисляет клиенту раз в год, квартал или месяц
#     daily = "Ежедневный остаток"
#     minimum = "Минимальный остаток"
import math
from enum import Enum


class ContributionStatus(Enum):
    minimum = 1
    daily = 2
    not_found = "Значение не найдено"
    not_number = "Значение должно быть указано числом"


def calculation_balance(status: int, deposit: int, bet: float, term: int, year: int) -> str:
    try:
        # Минимальный остаток
        if status == ContributionStatus.minimum.value:
            income = math.ceil(deposit * (bet / 100) * term / year)

        # Ежедневный остаток
        elif status == ContributionStatus.daily.value:
            income = math.floor(deposit * math.pow(1 + (bet / 100) / year, term) - deposit)

        else:
            return f"{ContributionStatus.not_found.value}"

        return f"Доход: {income}\nОбщий доход: {deposit + income}"

    except TypeError:
        return f"{ContributionStatus.not_number.value}"


if __name__ == "__main__":
    try:
        button = int(input(f"Что необходимо сделать?"
                           f"\n1. Рассчитать 'Минимальный остаток'"
                           f"\n2. Рассчитать 'Ежедневный остаток'"
                           f"\nВыберете цифрой: "))

        if button in [i.value for i in ContributionStatus]:
            print(calculation_balance(button,
                                      int(input("Укажите начальную сумма вклада: ")),  # ― пример: 50000
                                      float(input("Укажите процентную ставку: ")),  # ― пример: 6.8
                                      int(input("Укажите срок вклада в днях: ")),  # ― пример: 30
                                      int(input("Укажите количество дней в году: "))))  # ― пример: 365
        else:
            print(ContributionStatus.not_found.value)

    except ValueError:
        print(ContributionStatus.not_number.value)
