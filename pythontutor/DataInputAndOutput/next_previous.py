# Напишите программу, которая считывает целое число и выводит текст,
# аналогичный приведенному в примере (пробелы важны!).

def next_func(digit):
    return ("The next number for the number {} is {}."
            "\nThe previous number for the number {} is {}.".format(digit, digit + 1, digit, digit - 1))


print(next_func(1534))
