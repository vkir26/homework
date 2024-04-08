# Помогает собрать тесты из сайта https://pythontutor.ru/, которые будут использоваться в написании своих тестов
text = """Hi
iH
Hello
loHel
Qwerty
rtyQwe
Z
Z
asdfghj
ghjasdf
asdfghjzxc
hjzxcasdfg"""


def collector_func(n):
    if 'YES' in text or 'NO' in text:
        text_breakdown = text.replace('\n', '').replace('NO', 'NO\n').replace('YES', 'YES\n')
        for i in text_breakdown.strip().split('\n'):
            print(f"({', '.join(i[:n])}, '{i[n:]}'),")
    else:
        text_list = list(text.split('\n'))
        for i in range(0, len(text_list), n):
            print(f"({', '.join(text_list[i:i + n])}),")


if __name__ == "__main__":
    try:
        collector_func(int(input("Диапазон чисел до ")))
    except ValueError:
        print("Диапазон не может быть равен '0'")

# def collector_func(number):
#     if 'YES' in text or 'NO' in text:
#         text_breakdown = text.replace('\n', '').replace('NO', 'NO\n').replace('YES', 'YES\n')
#         for i in text_breakdown.strip().split('\n'):
#             print(f"({', '.join(i[:number])}, '{i[number:]}'),")
#     else:
#         text_list = list(text.split('\n'))
#         print(text_list)
#
#
# if __name__ == "__main__":
#     try:
#         collector_func(int(input("Диапазон чисел до ")))
#     except ValueError:
#         print("Диапазон не может быть равен '0'")

# Необходимо чтобы программа читала текст, а затем в зависимости от указанного значения, выводила всё до этого значения,
# например: 012345678901234, значение = 5, вывод: (0, 1, 2, 3, 4), (5, 6, 7, 8, 9)
