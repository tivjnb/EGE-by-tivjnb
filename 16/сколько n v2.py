from functools import lru_cache
'''
f(n) = n n<10
f(n) = f(n%10) + f(n//10) n>=10
Определите количество натуральных значений n, меньших 2^63, для которых F(n)=159



@lru_cache(None)
def f(n):
    if n < 10:
        return n
    return f(n % 10) + f(n//10)


count = 0
for i in range(1, 2**63 + 1):
    if f(i) == 159:
        count += 1
print(count)
'''