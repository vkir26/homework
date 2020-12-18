import os

with open('task2_data_2.txt') as file_2:
    #for line in file_2:
        with open('task2_data_1.txt', 'a+') as file_1:
                line = file_2.readline()
                print(f'\n\n\n{line}', file = file_1, end='')
os.rename('task2_data_1.txt', 'task2_data_all.txt')
os.remove('task2_data_2.txt')