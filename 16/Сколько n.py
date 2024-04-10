'''
F(0) = 0;

F(n) = F(n / 2), если n > 0 и при этом чётно;

F(n) = 1 + F(n − 1), если n нечётно.


Сколько существует таких чисел n, что 1 ≤ n ≤ 1000 и F(n)=3?
'''


def f(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return f(n//2)
    if n % 2 != 0:
        return 1 + f(n-1)


count = 0
for n in range(1, 1000+1):
    if f(n) == 3:
        count += 1
print(count)
'''
Ну можно еще по приколу вторую часть написать вот так:
print( len([ x for x in range(1, 1001) if f(x) == 3]))
'''
