# Дана строка. Удалите из этой строки все символы @
def character(s):
    return s.replace('@', '')


if __name__ in "__main__":
    word = input()
    print(character(word))
