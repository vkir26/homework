# По данному натуральном n вычислите сумму 1!+2!+3!+...+n!.
# В решении этой задачи можно использовать только один цикл.
# Пользоваться математической библиотекой math в этой задаче запрещено.

def factorial_sum(n):
    factorial = 1
    result = 0
    for i in range(1, n + 1):
        factorial *= i  # Для начала программа находит факториал
        result += factorial  # Затем выполняет операцию сложения
    return result


print(factorial_sum(3))  # (1 * 1) + (1 * 2) + (1 * 2 * 3) = 1 + 2 + 6 = 9
print(factorial_sum(4))  # (1 * 1) + (1 * 2) + (1 * 2 * 3) + (1 * 2 * 3 * 4) = 1 + 2 + 6 + 24 = 33
# Работа программы, число (факториал) = 3:
# factorial * 1 = 1 (factorial = 1)
# result + factorial = 1 (result = 1)
# factorial * 2 = 2 (factorial = 2)
# result + factorial = 3 (result = 3)
# factorial * 3 = 6 (factorial = 6)
# result + factorial = 9 (result = 9)