# Напишите программу, которая приветствует пользователя, выводя слово Hello,
# введенное имя и знаки препинания по образцу: Hello, Harry!
def hello(text):
    return "Hello, {}!".format(text)


print(hello("Ivan"))