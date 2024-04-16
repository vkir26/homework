# Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
# По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.

def factorial_func(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


print(factorial_func(4))