from itertools import permutations
from functools import lru_cache
'''
Автомат получает на вход трёхзначное число. По этому числу строится новое число по следующим правилам:
1) Из цифр, образующих десятичную запись N, строятся все возможные двузначные числа (числа не могут начинаться с нуля).
2) Из получившихся двузначных чисел выбираются только те, которые являются простыми.
Для какого наибольшего N количество выбранных простых чисел будет максимальным?'''


@lru_cache(None)
def is_simple(ch):
    for y in range(2, int(ch**0.5)+1):
        if ch % y == 0:
            return False
    return True


m = 0
m_ch = 0
for i in range(100, 1000):
    per = set()
    for x in [''.join(x) for x in permutations(str(i), r=2)]:
        if x[0] != '0':
            per.add(int(x))
    simples = len([x for x in per if is_simple(x)])

    if simples >= m:
        m = simples
        m_ch = i

print(m, m_ch)
