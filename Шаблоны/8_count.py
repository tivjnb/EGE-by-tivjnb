from itertools import permutations

a=[''.join(x) for x in permutations('МАТВЕЙ')]

count=0

for i in a:
    if i[0]!='Й' and ('АЕ' not in i):
        count+=1