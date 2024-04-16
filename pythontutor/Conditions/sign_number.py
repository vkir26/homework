# В математике функция sign(x) (знак числа) определена так:
# sign(x) = 1, если x > 0,
# sign(x) = -1, если x < 0,
# sign(x) = 0, если x = 0.
# Для данного числа x выведите значение sign(x).
# Эту задачу желательно решить с использованием каскадных инструкций if... elif... else.
def sign_func(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


print(sign_func(1))
