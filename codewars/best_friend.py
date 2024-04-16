# Задана строка, возвращает True, если данная буква всегда появляется непосредственно перед другой заданной буквой.
def best_friend(txt, a, b):
    return txt.count(a) == txt.count(a + b)


# print(best_friend("he headed to the store", "h", "e"))  # True
# print(best_friend('qqxhb wxhixhhc dsxhdjxh nxhdxhpwxh xxhknxhy exh', 'x', 'h'))  # False
# «Каждый раз, когда в строке появляется первая буква, рядом с ней должна идти вторая буква. Если нет, то верните «False»».
# Если после a следует b, значит True
# Всегда ли b идет после a? - нужно чтобы программа спросила
