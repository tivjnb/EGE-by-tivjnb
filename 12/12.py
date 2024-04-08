a = '9' * 127  # Строка
while '333' in a or '999' in a:  # 'подстрока' нашлось в строке
    if '333' in a:
        a = a.replace('333', '9')
    else:
        a = a.replace('999', '3')
print(a)
