# Помогает собрать тесты из сайта https://pythontutor.ru/, которые будут использоваться в написании своих тестов
text = """4
4
5
5
YES
4
4
5
4
YES
4
4
5
3
YES
4
4
4
5
YES
4
4
3
5
YES
4
4
4
3
YES
4
4
3
4
YES
4
4
3
3
YES
1
1
1
8
NO
1
1
8
8
NO
1
1
8
1
NO
1
8
8
8
NO
1
8
8
1
NO
1
8
1
1
NO
8
8
8
1
NO
8
8
1
1
NO
8
8
1
8
NO
8
1
1
1
NO
8
1
1
8
NO
8
1
8
8
NO
1
1
1
2
YES
1
1
2
2
YES
1
1
2
1
YES
4
4
6
6
NO
4
4
2
2
NO
4
4
6
2
NO
4
4
2
6
NO
4
4
2
7
NO
4
4
4
6
NO
4
4
2
4
NO
4
4
5
6
NO
1
7
1
8
YES
4
3
2
2
NO"""


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
