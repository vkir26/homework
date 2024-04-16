# Дано несколько чисел. Вычислите их сумму. Сначала вводите количество чисел N, затем вводится ровно N целых чисел.
# Какое наименьшее число переменных нужно для решения этой задачи?
def sum_n(result: list) -> int:
    return sum(result)


if __name__ in "__main__":
    n = int(input("Введите количество чисел: ")) + 1
    x = [int(input(f"Введите число №{numering}: ")) for numering, i in enumerate(range(1, n), 1)]
    print("Ответ:", sum_n(x))
