def f(s, hod):
    if s >= 93:
        return hod % 2 == 0
    if hod == 0:
        return 0

    variants = [f(s+1, hod-1), f(s+2, hod-1), f(s*10, hod-1)]
    return any(variants) if hod % 2 !=0 else all(variants)
#  Если в каком-то задании нужен неудачный ход, то мы заменяем второй all на any


print('19', [x for x in range(1, 92) if f(x, 2)])  # Ваня первым ходом
print('20', [x for x in range(1, 92) if not (f(x, 1)) and f(x, 3)])  # Петя вторым ходом
print('20', [x for x in range(1, 92) if not (f(x, 2)) and f(x, 4)])  # Ваня вторым ходом
