# Помогает собрать тесты из сайта https://pythontutor.ru/, которые будут использоваться в написании своих тестов
text = """1
1
1
4
NO
1
1
8
8
NO
2
4
3
2
YES
5
2
4
4
YES
2
8
3
7
NO
2
8
3
5
NO
5
5
3
7
NO
2
4
2
5
NO
4
7
6
6
YES
4
5
2
4
YES
2
3
3
2
NO
5
1
4
3
YES
6
2
8
3
YES"""


def collector_func(n):
    if 'YES' in text or 'NO' in text:
        text_breakdown = text.replace('\n', '').replace('NO', 'NO\n').replace('YES', 'YES\n')
        for i in text_breakdown.strip().split('\n'):
            print(f"({', '.join(i[:n])}, '{i[n:]}'),")
    else:
        text_list = list(text.split('\n'))
        for i in range(0, len(text_list), n):
            print(f"({', '.join(text_list[i:i + n])}),")


collector_func(int(input("Диапазон чисел до ")))

# Необходимо чтобы программа читала текст, а затем в зависимости от указанного значения, выводила всё до этого значения,
# например: 012345678901234, значение = 5, вывод: (0, 1, 2, 3, 4), (5, 6, 7, 8, 9)
