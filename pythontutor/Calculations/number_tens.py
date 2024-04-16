# Дано натуральное число. Найдите число десятков в его десятичной записи.
def number_tens(x: int) -> int:
    return x // 10 % 10


print(number_tens(9999))