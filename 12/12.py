a = '9' * 127  # Строка
while '333' in a or '999' in a:  # 'подстрока' нашлось в строке
    if '333' in a:
        a = a.replace('333', '9')
    else:
        a = a.replace('999', '3')
print(a)
'''
Если А другой длины
'''
for x in range(20, 200):
    a = '9' * x
    while '333' in a or '999' in a:  # 'подстрока' нашлось в строке
        if '333' in a:
            a = a.replace('333', '9')
        else:
            a = a.replace('999', '3')

'''
Если разное количесво a и b, при этом без упомнания порядка, то можно ставить просто подряд
'''
for x in range(20, 200):
    for y in range(20, 200):
        a = ('9' * x) + ('3' * y)
        while '333' in a or '999' in a:
            pass
