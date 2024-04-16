# Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов.
# Используйте для решения задачи метод count.

def count_word(w):
    return w.count(' ') + 1


if __name__ in "__main__":
    word = str(input())
    print(count_word(word))
