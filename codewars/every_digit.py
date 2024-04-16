# возвести в квадрат каждую цифру числа и соединить их.
#
# Например, если мы пропустим через функцию 9119, получится 811181, потому что 9^2 равно 81, а 1^2 равно 1. (81-1-1-81)
#
# Пример №2: Ввод 765 вернет/должен вернуть 493625, потому что 7^2 равно 49, 6^2 равно 36, а 5^2 равно 25. (49-36-25)

def square_digits(num):
    return int(''.join([str(int(i)**2) for i in str(num)]))


print(square_digits(765))