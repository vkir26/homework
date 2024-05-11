import random


def fps():
    print(f'Ваш фпс: {random.randint(0, 101)}')


def hello():
    print('Hello!')


def config(func, enabling):
    cfg = {
        hello: True,
        fps: True
    }

    if not enabling:
        cfg[func] = enabling
    if cfg[func]:
        return func()



while True:
    word = input()

    if word == '/fps':
        config(fps, True)

    elif word == '/fps off':
        config(fps, False)

    if word == 'hello':
        config(hello, True)

    elif word == '/hello off':
        config(hello, False)
