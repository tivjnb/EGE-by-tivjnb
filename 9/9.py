#  Для начала выделяем все столбцы, копируем и вставляем в новый файл
f = open('table_for_9.txt', 'r')
table = [list(map(int, x.split())) for x in f]  # Построчно разбиваем числа и преобразуем в int


# В данной задаче нам нужно определить тройки, которые могут быть сторонами треугольника
def is_triangle(a, b, c):  # Функция, которая определяет, может ли быть тройка сторонами треугольника
    return (a + b) > c and (a + c) > b and (b + c) > a


count = 0
for row in table:
    a = row[0]
    b = row[1]
    c = row[2]
    if is_triangle(a, b, c):
        count += 1
print(count)
