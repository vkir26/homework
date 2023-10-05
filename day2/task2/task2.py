'''
Напишите программу, которая использует список из задачи 1, и складывает все численные данные.
Постарайтесь использовать максимально возможное кол-во элементов.
'''
lst = [1, 5445, 5445.0, 1.56, "1.90", "сорок_два", False, "", True]
list_num = []
for i in lst:
    try:
        num = str(i)
        list_num.append(float(i))
    except ValueError:
        continue
print(sum(list_num))