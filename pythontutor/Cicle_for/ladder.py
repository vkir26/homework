# По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.
def ladder_func(n):
    result = []
    for i in range(1, n + 1):
        result.append(list(range(1, i + 1)))
    return result


if __name__ in "__main__":
    print(ladder_func(int(input())))
