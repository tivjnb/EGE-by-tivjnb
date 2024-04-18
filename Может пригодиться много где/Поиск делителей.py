def divisors(ch):  # Все делители числа
    d = set()
    d.add(1)  # Если включаем еденицу
    d.add(ch)  # Если включаем само число
    for i in range(2, int(ch**0.5)+1):
        if ch % i == 0:
            d.add(i)
            d.add(ch // i)
    return list(d)


def is_simple(ch):  # Проверка, является ли число простым
    for i in range(2, int(ch**0.5)+1):
        if ch % i == 0:
            return False
    return True
