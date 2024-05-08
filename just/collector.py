# Помогает собрать тесты из сайта https://pythontutor.ru/, которые будут использоваться в написании своих тестов
# Необходимо чтобы программа читала текст, а затем в зависимости от указанного значения, выводила всё до этого значения,
# например: 012345678901234, значение = 5,
# вывод:
# (0, 1, 2, 3, 4),
# (5, 6, 7, 8, 9)
import pyperclip

text = pyperclip.paste().replace('\r', '')

# text = """"""  # - Для самостоятельной(CTRL+C, CTRL+V) вставки


def collector(limit, num):
    for i in range(0, len(limit), num):
        result = "', '".join(limit[i:i + num])
        if i != len(limit) - num:
            print(f"('{result}'),")
        else:
            print(f"('{result}')")


def main_collector(before):
    text_list = text.replace(' ', '\n').split('\n')
    return collector(text_list, before)


if __name__ == "__main__":
    if len(text) != 0 and text.replace(' ', ''):
        number = input("Диапазон чисел до ")
        try:
            main_collector(int(number))
        except ValueError:
            print(f"Диапазон не может быть равен {number}")
    else:
        print('Скопированный Текст из тестов не найден')
