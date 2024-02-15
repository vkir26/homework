# Сделать счётчик с выбором знака и с возможностью дальнейшего указания числа для счёта, затем программа делает счёт на
# указанное число (в зависимости от знака + - : *) и ждёт ввода следующего
def counter_func(n, sign):
    s = ""
    n = int(n)
    try:
        while True:
            if sign == "+":
                s = input("Что прибавим?: ")
                n += int(s)
            elif sign == "-":
                s = input("Что отнимем?: ")
                n -= int(s)
            elif sign == ":" or sign == "/":
                s = input("Что разделим?: ")
                n /= int(s)
            elif sign == "*":
                s = input("Что умножим?: ")
                n *= int(s)
            else:
                return "Неизвстный знак! Используйте:\nРазделить ':' или '/'\nУмножить '*'\nПрибавить '+'\nОтнять '-'"
            print(f"Ответ: {n}\nДля остановки счётчика используйте: Stop")
    except ValueError:
        if s.lower() == "stop":
            return f'Счётчик остановлен пользователем!\nПоследнее значение: {n}'
        else:
            return "Значение должно быть числом!"
    except ZeroDivisionError:
        return "На '0' делить нельзя!"


a = input("Укажите начальное значение: ")
b = input("Что необходимо сделать?\nУкажите знак: ")
if int(a) == 0 and b == '/':
    print("На '0' делить нельзя!")
else:
    print(counter_func(a, b))