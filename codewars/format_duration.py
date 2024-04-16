"""
Human readable duration format
Ваша задача для выполнения этого Ката — написать функцию, которая форматирует продолжительность, заданную в секундах,
удобным для человека способом.

Функция должна принимать неотрицательное целое число. Если оно равно нулю, оно просто возвращает "now". В противном
случае продолжительность выражается как комбинация years, days, и .hours minutes seconds

Гораздо проще понять на примере:

* For seconds = 62, your function should return
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
Для целей этой Ката год состоит из 365 дней, а день — из 24 часов.

Обратите внимание, что пробелы важны.

Подробные правила
Результирующее выражение состоит из таких компонентов, как 4 seconds, 1 year и т. д. Обычно это положительное целое число
 и одна из допустимых единиц времени, разделенных пробелом. Единица времени используется во множественном числе,
 если целое число больше 1.

Компоненты разделяются запятой и пробелом ( ", "). За исключением последнего компонента, который отделяется " and ",
как если бы он был написан на английском языке.

Более значимые единицы времени наступят раньше, чем наименее значимые. Поэтому 1 second and 1 year это не правильно, но 1
 year and 1 second есть.

Разные компоненты имеют разную единицу измерения времени. Таким образом, здесь нет повторяющихся единиц, как в 5 seconds
 and 1 second.

Компонент вообще не появится, если его значение равно нулю. Следовательно, 1 minute and 0 seconds это недействительно, но
 должно быть справедливо 1 minute.

Единицу времени необходимо использовать «насколько это возможно». Это означает, что функция должна возвращать не 61
seconds, а 1 minute and 1 second вместо этого. Формально длительность, указанная в компоненте,
не должна превышать любую допустимую более значимую единицу времени.

f"{days} day, {hours} hour, {minutes} minute and {seconds} seconds".split(",")
"""


def format_duration(seconds):
    time_min = 60
    time_hour = 3600
    time_day = 86400
    time_year = time_day * 365

    years = seconds // time_year
    seconds = seconds % time_year

    days = seconds // time_day
    seconds = seconds % time_day

    hours = seconds // time_hour
    seconds = seconds % time_hour

    minutes = seconds // time_min
    seconds = seconds % time_min

    designations = f"{years} year:{days} day:{hours} hour:{minutes} minute:{seconds} second".split(":")

    # Главная функция, использует цикл, для вывода отдельных элементов из списка "designations", затем проверяет
    # что число не равно "0" - допустит те числа, которые не равны "0", далее разделяет числа и слова с помощью split -
    # 1 year = [1, year] соответственно i[0] будет равен числу "1", а i[1] будет равен "year".
    # затем сканируем числа, если число > больше 1, значит добавляем окончание "s" к слову, было "year" станет "years",
    # если число не больше 1 или 1, то будет просто year
    func_sorting = [f"{i.split()[0]} {i.split()[1]}{int(i.split()[0]) > 1 and 's' or ''}" if int(i.split()[0]) > 1 else f"{i.split()[0]} {i.split()[1]}" for i in designations if int(i[0]) != 0]
    result = ""
    if len(func_sorting) > 1:
        result += ", ".join(func_sorting[:-1]) + ' and ' + func_sorting[-1]
    else:
        result += "".join(func_sorting)

    if result != '':
        return result
    else:
        return 'now'


print(format_duration(0))


