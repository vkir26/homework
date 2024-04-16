# Дано натуральное число. Выведите его последнюю цифру.
def last_func(x: int) -> int:
    # return int(str(x)[-1])
    return x % 10


print(last_func(179))
