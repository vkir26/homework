# Дано трехзначное число. Найдите сумму его цифр.
def sum_digits(x: int) -> int:
    return sum(list(map(int, str(x))))


print(sum_digits(179))
