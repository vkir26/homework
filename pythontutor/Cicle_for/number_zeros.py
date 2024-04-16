# Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел.
# Подсчитайте количество нулей среди введенных чисел и выведите это количество.
# Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.
def num_zeros(number):
    result = 0
    for i in number:
        if i == 0:
            result += 1
    return result


if __name__ in "__main__":
    count = int(input())
    print(num_zeros([int(input()) for i in range(count)]))
