'''
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [18782; 18822],
числа, имеющие ровно три различных нечётных натуральных делителя,
не считая единицы и самого числа (при этом количество чётных делителей может быть любым).
Для каждого найденного числа в порядке возрастания запишите эти три делителя в таблицу на экране с новой строки.
Делители в строке таблицы также должны следовать в порядке возрастания.
'''


def divisors(ch):
    r = set()

    for i in range(2, int(ch**0.5)+1):
        if ch % i == 0:
            r.add(i)
            r.add(ch//i)
    return r


sk = 0
for ch in range(18782, 18822+1):
    d = divisors(ch)
    n_chet_div = [x for x in d if x % 2 != 0]
    if len(n_chet_div) == 3:
        print(sorted(n_chet_div))
