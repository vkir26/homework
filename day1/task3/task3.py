"""
Программа принимает на вход строку. Эта строка — путь к файлу.

В случае существования файла:

1) проверить возможна ли в него запись.

2) удалить, и закончить работу.

Если файла нет:

1) создать,

2) записать строку c латинскими и кириллическими буквами в кодировке UTF-8

3) прочитать и вывести содержимое в кодировке WINDOWS-1251 и в кодировке UTF-8

4) удалить, и закончить работу.
"""
import os

file = ('task3_data.txt')

if os.access('task3_data.txt', os.W_OK):
    print("В файл можно писать")
    os.remove('task3_data.txt')
else:
    print("Писать в файл запрещено")
    file = open('task3_data.txt', 'w')
    file.write('Привет, Мир!!!')
    file = open('task3_data.txt', 'r')
    encoding_1 = file.read()
    file = open('task3_data.txt', 'r', encoding='LATIN-1')
    encoding_2 = file.read()
    print(f'Кодировка 1: {encoding_1}\nКодировка 2: {encoding_2}')
    file.close()
    os.remove('task3_data.txt')


# Актуально:
# ѭѯѵѩѥ Hello, World! // task_data3.txt
# path = str(input('Введите путь до файла: '))
# if os.access(path, os.W_OK):
#     print("В файл можно писать!")
# else:
#     with open(path, 'a+', encoding='UTF-8') as file:
#         file.write(str(input("Введите что записать в файл: ")))
#     with open(path, 'r') as encoding_one:
#         print(encoding_one.read())
#     with open(path, 'r', encoding='UTF-8') as encoding_two:
#         print(encoding_two.read())
#     os.remove(path)
