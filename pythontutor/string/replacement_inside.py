# Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.
def replacement(s):
    return s[:s.find('h')+1] + s[s.find('h')+1:s.rfind('h')].replace('h', 'H') + s[s.rfind('h'):]


if __name__ in "__main__":
    word = input()
    print(replacement(word))
