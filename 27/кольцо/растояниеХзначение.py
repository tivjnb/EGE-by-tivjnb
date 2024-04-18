f = open('27_B.txt', 'r')
forge_count, perimetr = map(int, f.readline().split())

'''
Основной принцип
1)Мы рассчитываем расстояния для одного места в круге
2)Делим круг на 2 части и считаем количество кабелей для них:
В одной при сдвиге вправо все кабели удлиняться
Во второй укоротятся
3)Начинаем двигать опорный элемент, прибавляя значения удаляющихся кабелей и вычитая приближающиеся
4)Перекидываем крайний элемент одной половины круга в другую половину
'''


ls = [0]*perimetr

for i in f:
    kilometer, need_energy = map(int, i.split())
    ls[kilometer] = need_energy//2 + (need_energy % 2 != 0)

p2 = perimetr//2

back = sum(ls[:p2+1])
forward = sum(ls[p2+1:])
print(len(ls[p2+1:]), len(ls[:p2+1]))
s = 0
for ind, i in enumerate(ls, 0):
    s += i*abs(p2-ind)

m = s

for turn in range(p2+1, p2 + perimetr + 100):
    from_back_to_forward = ls[(turn - p2 - 1) % perimetr]

    back -= from_back_to_forward  # Тут длина круга нечетная, поэтому расстояние до этого элемента сохранится
    s = s + back - forward
    m = min(m, s)

    back = back + ls[turn % perimetr]
    forward = forward - ls[turn % perimetr] + from_back_to_forward


print(m)


'''
2756671544224
'''