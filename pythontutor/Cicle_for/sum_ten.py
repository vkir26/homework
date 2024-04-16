# Дано 10 целых чисел. Вычислите их сумму. Напишите программу, использующую наименьшее число переменных.
def sum_ten(result: list) -> int:
    return sum(result)


if __name__ in "__main__":
    x = [int(input()) for i in range(1, 11)]
    print(sum_ten(x))
