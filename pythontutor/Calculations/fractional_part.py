# Дано положительное действительное число X. Выведите его дробную часть.
def fractional_part(x: float):
    return x % 1


print(fractional_part(10.34))
