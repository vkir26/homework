# Дана строка. Замените в этой строке все цифры 1 на слово one

def substring(s):
    return s.replace('1', 'one')


if __name__ in "__main__":
    word = input()
    print(substring(word))