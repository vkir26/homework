# Пирожок в столовой стоит a рублей и b копеек. Определите, сколько рублей и копеек нужно заплатить за n пирожков.
# Программа получает на вход три числа: a, b, n, и должна вывести два числа: стоимость покупки в рублях и копейках.
def purchase_price(a: int, b: int, n: int):
    rub = a * n
    cop = b * n / 100
    return rub + cop


print(purchase_price(10, 15, 2))  # 20.30
# a - Рубли
# b - Копейки
# n - Кол-во пирожков
# int(rub + cop), round((rub + cop) % 1 * 100) # pythontutor.ru
