import os

if os.access('task1_data.txt', os.F_OK):
    file = open('task1_data.txt', 'r')
    print('Файл существует')
    text = file.readline()
    print('Общее количество символов в файле:', len(text))
    symbol = input('Введите символ для поиска: ')
    print(f'Символ встречается: {text.count(symbol)} раз(а)')
else:
    file = open('task1_data.txt', 'a+')
    file.write(input('Введите текст для записи в файл: '))
    file = open('task1_data.txt', 'r')
    text = file.readline()
    print('Файл не существует, поэтому он будет создан, и в него будет записана строка', text, '\nОбщее количество символов', len(text))
    symbol = input('Введите символ для поиска: ')
    print(f'Символ встречается: {text.count(symbol)} раз(а)')