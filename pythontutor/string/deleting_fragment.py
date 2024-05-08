# Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними
def del_fragment(s):
    return s[:s.find("h")] + s[s.rfind("h") + 1:]


if __name__ in "__main__":
    proposal = input()
    print(del_fragment(proposal))
