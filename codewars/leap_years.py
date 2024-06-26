"""
В этом ката вы должны просто определить, является ли данный год високосным или нет.
В случае, если вы не знаете правил, вот они:

Годы, кратные 4, являются високосными,
но годы, кратные 100, не являются високосными,
но годы, кратные 400, являются високосными годами.
Проверенные годы находятся в диапазоне 1600 ≤ год ≤ 4000.
"""


def is_leap_year(year):
    return year % 4 == 0 if year % 400 == 0 or year % 100 != 0 else False


print(is_leap_year(2012))
