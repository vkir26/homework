# Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.
import math


def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


print(hypotenuse(3, 4))  # 5.0