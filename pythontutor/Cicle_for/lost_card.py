# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
# Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.
#
# Для самых умных: массивами и аналогичными структурами данных пользоваться нельзя.
def lost_card(n, nl):
    result = 0
    for i in range(1, n + 1):
        result += i
    for k in nl:
        result -= k
    return result


if __name__ in "__main__":
    number = int(input())
    number_list = [int(input()) for _ in range(number - 1)]
    print(lost_card(number, number_list))
