# Программа делает расчёт суммы начисленных процентов с минимального остатка и ежедневного остатка
# Инструкция которой пользовался: https://www.mtsbank.ru/articles/kak-rasschitat-protsenty-po-vkladu/
# % годовых - это процент от суммы вклада, который банк начисляет клиенту раз в год, квартал или месяц
import math


daily = "Ежедневный остаток"
minimum = "Минимальный остаток"


def calculation_balance(on, d: int, i: float, t: int, y: int) -> str:
    percent = i / 100
    income = 0

    # Минимальный остаток
    if on == minimum:
        income = math.ceil(d * percent * t / y)

    # Ежедневный остаток
    elif on == daily:
        income = math.floor(d * math.pow(1 + percent / y, t) - d)
    return f"Доход: {income}\nОбщий доход: {d + income}"


if __name__ == "__main__":
    button = input(f"Что необходимо сделать?\n1. Рассчитать '{daily}'\n2. Рассчитать '{minimum}'\nВыберете цифрой: ")

    try:
        if int(button) == 1 or int(button) == 2:
            deposit_amount = int(input("Укажите начальную сумма вклада: "))  # ― начальная сумма вклада, пример: 50000
            interest_rate = float(input("Укажите процентную ставку: "))  # ― процентная ставка, пример: 6.8
            term = int(input("Укажите срок вклада в днях: "))  # ― срок вклада в днях, пример: 30
            year = int(input("Укажите количество дней в году: "))  # ― количество дней в году (Банк), пример: 365

            if int(button) == 1:
                print(calculation_balance(daily, deposit_amount, interest_rate, term, year))
            elif int(button) == 2:
                print(calculation_balance(minimum, deposit_amount, interest_rate, term, year))
        else:
            print(f"Не найдено: {button}, укажите цифрой что необходимо сделать")
    except ValueError:
        print("Значение должно быть указано числом")
