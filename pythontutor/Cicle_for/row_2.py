# Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B,
# или в порядке убывания в противном случае.
def row2(A: int, B: int) -> str:
    if A <= B:
        return ' '.join([str(i) for i in range(A, B+1)])
    else:
        return ' '.join([str(i) for i in range(B, A + 1)][::-1])


print(row2(-3, -7))  # "-3 -4 -5 -6 -7"