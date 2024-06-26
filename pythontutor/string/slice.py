# Дана строка.
# Сначала выведите третий символ этой строки.
# Во второй строке выведите предпоследний символ этой строки.
# В третьей строке выведите первые пять символов этой строки.
# В четвертой строке выведите всю строку, кроме последних двух символов.
# В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0,
# поэтому символы выводятся начиная с первого).

# В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# В седьмой строке выведите все символы в обратном порядке.
# В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# В девятой строке выведите длину данной строки.

def main(value: str) -> list:
    match value:
        case w:
            return [
                one(w), two(w), three(w), four(w), five(w),
                six(w), seven(w), eight(w), nine(w)
            ]


def one(w: str) -> str:  # Сначала выведите третий символ этой строки.
    return w[2]


def two(w: str) -> str:  # Во второй строке выведите предпоследний символ этой строки.
    return w[-2]


def three(w: str) -> str:  # В третьей строке выведите первые пять символов этой строки.
    return w[:5]


def four(w: str) -> str:  # В четвертой строке выведите всю строку, кроме последних двух символов.
    return w[:-2]


def five(w: str) -> str:  # В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0,
    # поэтому символы выводятся начиная с первого.
    return w[::2]


def six(w: str) -> str:  # В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
    return w[1::2]


def seven(w: str) -> str:  # В седьмой строке выведите все символы в обратном порядке.
    return w[::-1]


def eight(w: str) -> str:  # В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
    return w[::-2]


def nine(w: str) -> str:  # В девятой строке выведите длину данной строки.
    return str(len(w))


if __name__ in "__main__":
    word = str(input()).replace(' ', '')
    if len(word) > 2:
        print(main(word))
    else:
        print('Строка должна содержать более 2 символов')
