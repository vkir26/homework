# Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.
def row1(A, B):
    return ' '.join([str(i) for i in range(A, B+1)])


print(row1(1, 10))
