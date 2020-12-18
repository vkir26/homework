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