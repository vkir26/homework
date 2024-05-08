# Дана строка, в которой буква h встречается как минимум два раза. Разверните последовательность символов,
# заключенную между первым и последним появлением буквы h, в противоположном порядке.
def conversion(s):
    return s[:s.find("h")+1] + s[s.find("h")+1:s.rfind("h")][::-1] + s[s.rfind("h"):]


if __name__ in "__main__":
    proposal = input()
    print(conversion(proposal))
