from functools import *
'''
Сколько существует восьмеричных чисел, имеющих ровно 27 значащих разрядов,
 при перестановке цифр которых можно получить палиндром.
 В ответ запишите остаток от деления на 10^9 + 7'''

@cache
def f(s, l):
    if l == 0:
        return f'{s:b}'.count('1') <= 1
    return sum(f(s ^ (1 << x), l-1) for x in range(8))


print((f(0, 27) - f(1, 26)) % (10**9+7))
