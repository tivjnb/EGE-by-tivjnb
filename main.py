from itertools import permutations

a=permutations('КУПЧИХА')
s=0
for i in a:
    aa=''.join(i)
    if aa[0]!='Ч' and not('УИА'  in aa       or 'УАИ'  in aa       or 'ИУА'  in aa or 'ИАУ'  in aa or 'АУИ'  in aa or 'АИУ'  in aa ):
        s+=1
print(s)