'''
Напишите программу, которая принимает строку в формате «php=Rasmus Lerdorf; perl=Larry Wall; python=Guido van Rossum».
Постройте словарь, где ключи — значения слева от «=», а значения — справа от «=». Разделитель — «;». Инвертируйте словарь так,
чтобы значения стали ключами, а ключи — значениями. Выведите получившиеся словари в отсортированном по ключам виде, разделённые 40 решётками.
Гарантируется, что все значения и ключи уникальны.
'''


#line = 'y=f(x)'
#line = 'y=f(x);z=f(x, y)'
line = 'php=Rasmus Lerdorf; perl=Larry Wall; python=Guido van Rossum'
d = {}
for i in line.split(';'):
    divide = i.lstrip().split('=')
    d[divide[0]] = divide[1]
    print(f"{divide[0]} = {divide[1]}")
print('#' * 40)
for key, value in d.items():
    print(f"{value} = {key}")


##############################################
# php=Rasmus Lerdorf; perl=Larry Wall; python=Guido van Rossum

# dict_with_list = {
#     'php': 'Rasmus Lerdorf',
#     'perl': 'Larry Wall',
#     'python': 'Guido van Rossum'
# }
# for key, value in dict_with_list.items():
#     print('{} = {}'.format(key, value))
# print('#'*40)
# for key, value in dict_with_list.items():
#     print('{} = {}'.format(value, key))
##############################################
#
# dict = {}
# s = 'php=Rasmus Lerdorf; perl=Larry Wall; python=Guido van Rossum'.split('; ')
# for i in s:
#     i = i.split('=')
#     key_cut = i[:-1]
#     key = ''.join(str(i) for i in key_cut)
#     value = str(i[1])
#     dict[key] = value
# for key, value in dict.items():
#     print('{} = {}'.format(key, value))
# print('#'*40)
# for key, value in dict.items():
#     print('{} = {}'.format(value, key))
##############################################



'''
dict = {}
dict['php'] = 'Rasmus Lerdorf'
dict['perl'] = 'Larry Wall'
dict['python'] = 'Guido van Rossum'
print(dict)

s = {'dkkdg': 's'}
print(type(s))
'''