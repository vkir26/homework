'''
Напишите программу, которая принимает строку цветов, разделённых пробелами. Например: red green blue black.
Выведите первый и последний цвета и общее количество уникальных цветов.

Примеры:

-> red green blue
<- red blue 3

-> red red red red
<- red red 1

-> red green red green black
<- red black 3
'''
color = input()
color = color.split()
print(color[0], color[-1])
print(len(set(color)))
