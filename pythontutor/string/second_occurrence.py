# Дана строка. Найдите в этой строке второе вхождение буквы f, и выведите индекс этого вхождения.
# Если буква f в данной строке встречается только один раз, выведите число -1,
# а если не встречается ни разу, выведите число -2

def second(s, f):
    if f > 1:
        return s.find('f', s.find('f') + 1)
    elif f == 1:
        return -1
    else:
        return -2


if __name__ in "__main__":
    word = input()
    count = word.count("f")
    print(second(word, count))
