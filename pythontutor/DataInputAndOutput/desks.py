# В школе решили набрать три новых математических класса.
# Так как занятия по математике у них проходят в одно и то же время,
# было решено выделить кабинет для каждого класса и купить в них новые парты.
# За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов.
# Сколько всего нужно закупить парт чтобы их хватило на всех учеников? Программа получает на вход три натуральных числа:
# количество учащихся в каждом из трех классов.
def desks_func(a, b, c):
    x = a + b + c
    if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
        x = round(x / 2 + 1)
        return x
    else:
        return x // 2


print(desks_func(20, 21, 22))
