"""
В небольшом городе численность населения p0 = 1000 на начало года. Население регулярно увеличивается на 2% в год,
причем 50 каждый год в город приезжают новые жители. Сколько лет нужно городу,
чтобы его население превысило или сравнялось с p = 1200 жителями?

В конце первого года будет:
1000 + 1000 * 0.02 + 50 => 1070 inhabitants

В конце 2-го года будет:
1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

В конце 3-го года будет:
1141 + 1141 * 0.02 + 50 => 1213

На это потребуется целых 3 года.
Более общие параметры:

p0, percent, aug (жители приезжают или уезжают каждый год), p (численность населения, равная или превосходящая)

функция nb_year должна возвращать n количество целых лет, необходимых для получения численности населения,
большей или равной p.

aug — целое число, процент — положительное или нулевое плавающее число, p0 и p — положительные целые числа (> 0)

Examples:
nb_year(1500, 5, 100, 5000) -> 15
nb_year(1500000, 2.5, 10000, 2000000) -> 10
Примечание:
Не забудьте преобразовать процентный параметр в процентное значение в теле вашей функции: если процентный параметр равен
 2, вам необходимо преобразовать его в 0,02.

Нет никаких фракций людей. В конце каждого года численность населения представляет собой целое число: 252.8 число людей
 округляется до 252 числа человек.

p0 = численность населения на начало года
percent = регулярное увеличение населения на "число%" в год
aug = жители приезжают или уезжают каждый год
p = численность населения, равная или превосходящая
"""


# Мне необходимо посчитать сколько лет требуется чтобы p0 превысило или достигло p

def nb_year(p0, percent, aug, p):
    count = 0
    percent = percent / 100
    while p0 < p:
        p0 = int(p0 + p0 * percent + aug)
        count += 1
    return count


print(nb_year(1000, 2, 50, 1200))
