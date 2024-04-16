# Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс.
# Если она встречается два и более раз, выведите индекс её первого и последнего появления.
# Если буква f в данной строке не встречается, ничего не выводите.

def main(value: int, w: str):
    if value >= 2:
        return count_two(w)
    match value:
        case 1:
            return count_one(w)
        case _:
            return "Неизвестно как обработать"


def count_one(s):
    return s.find("f")


def count_two(s):
    return s.find("f"), s.rfind("f")


if __name__ in "__main__":
    word = str(input())
    count = word.count("f")
    print(main(count, word))
