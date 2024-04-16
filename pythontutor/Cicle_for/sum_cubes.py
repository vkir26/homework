# По данному натуральному n вычислите сумму 1^3+2^3+3^3+...+n^3.
def cubes_func(n: int) -> int:
    return sum([i ** 3 for i in range(n+1)])


if __name__ in "__main__":
    number = int(input("Введите число: "))
    print("Ответ:", cubes_func(number))
