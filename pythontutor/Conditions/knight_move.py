# Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали,
# или наоборот. Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую
# одним ходом.
def knight_func(x1, x2, y1, y2):
    return 'YES' if abs(x1 - y1) == 1 and abs(y2 - x2) == 2 or abs(x1 - y1) == 2 and abs(y2 - x2) == 1 else 'NO'


print(knight_func(4, 7, 6, 6))  # "YES"

