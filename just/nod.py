import pytest

# Найти наибольший общий делитель

error = 'Ошибка, значение должно быть целым числом!'


def nod(a, b):
    try:
        a = int(a)
        b = int(b)
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        return a + b
    except ValueError:
        return error


if __name__ == "__main__":
    print(nod(input('Введите значение 1: '), input("Введите значение 2: ")))


@pytest.mark.parametrize("a, b, expected", [(204, 136, 68),
                                            (140, 280, 140),
                                            (12, 36, 12),
                                            (16, 28, 4),
                                            ("Error", 5, error),
                                            (34, "Error", error)])
def test_nod(a, b, expected):
    assert nod(a, b) == expected
