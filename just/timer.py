import time


def timer_func(message):
    sec = int(''.join(x for x in message if x.isdigit()))
    if sec > 86400:
        return 'Слишком большой диапазон времени!'
    minute = sec // 60
    hour = sec // 3600
    if hour != 0 and hour <= 24:
        print(f'Таймер был установлен на {hour} ч')
    elif sec > 59:
        print(f'Таймер был установлен на {minute} м')
    else:
        print(f'Таймер был установлен на {sec} с')
    time.sleep(sec)
    return 'Таймер: Время вышло!'


print(timer_func('8'))
