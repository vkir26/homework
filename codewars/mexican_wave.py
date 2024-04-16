# Мексиканская волна
# В этом простом ката ваша задача — создать функцию, которая превращает строку в мексиканскую волну.
# Вам будет передана строка, и вы должны вернуть эту строку в массиве, где заглавная буква — это стоящий человек.

def wave(people):
    text = []
    for count, letter in enumerate(people):
        if letter != ' ':
            people_list = list(people)
            people_list[count] = letter.upper()
            text.append(''.join(people_list))
    return text


print(wave("codewars"))
