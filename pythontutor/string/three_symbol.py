# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.

def three(s):
    new_string = ''
    for i in range(len(s)):
        if i % 3 != 0:
            new_string += s[i]
    return new_string


if __name__ in "__main__":
    word = input()
    print(three(word))
