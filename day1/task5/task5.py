'''
Есть файл task5_data.txt со строкой 12йцas.

Необходимо прочитать его содержимое в простом режиме и вывести.

Затем, необходимо прочитать каждый символ в бинарном режиме и заменить 2-й младший бит у каждого байта, на противоположенный.
(если был 0, заменить на 1. если был 1, заменить на 0). Затем, надо полученные байты записать в бинарном режиме
в файл task5_data_new.txt и вывести содержимое файла в обычном режиме.

Не за путайся, учти что в новом файле, в итоге у тебя получатся какие-то корявые символы, 6ь штук, как и в исходном файле.

В примере (который есть выше) по работе с файлом в бинарном режиме есть все, чтобы считать байт из файла и получить
двоичное представление байта для каждого символа. Ты должен правильно реализовать обратный процесс.

См. «Работа со строками», «Срезы», bin (), hex (), int ()
https://www.bestprog.net/ru/2020/04/30/python-binary-files-examples-of-working-with-binary-files-ru/#:~:text=%D0%92%20%D1%8F%D0%B7%D1%8B%D0%BA%D0%B5%20Python%20%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D1%83%D1%8E%D1%82%20%D1%81%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2%D0%B0,%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D0%BE%D0%B9%20%D1%81%D0%BE%D0%B4%D0%B5%D1%80%D0%B6%D0%B8%D1%82%20%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%20'b'.
'''
byte_list = []
new_list = []
step = 8


def reading():
    global step
    with open('task5_data.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        for symbol in text:
            binary = ''.join(bin(int(symbol.encode().hex(), 16))[2:].zfill(8))
            if len(binary) <= 8:
                byte_list.append(binary)
            else:
                for item in range(0, len(binary), 8):
                    step += 8
                    byte_list.append(binary[item:step][0:8])
        return text


def replace():
    for i in byte_list:
        i = list(i)
        for number in [6]:
            if int(i[number]) == 0:
                i[number] = '1'
            elif int(i[number]) == 1:
                i[number] = '0'
            new_list.append(''.join(i))


def recording():
    with open('task5_data_new.txt', 'w+', encoding='latin-1') as file:
        file.write(''.join(chr(int(byte, 2)) for byte in new_list))
    with open('task5_data_new.txt', 'r', encoding='utf-8') as file:
        return file.read()


if __name__ == "__main__":
    print(reading())
    replace()
    print(recording())