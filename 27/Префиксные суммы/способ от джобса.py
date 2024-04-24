from itertools import accumulate

f = open('27A.txt', 'r')

n = int(f.readline())

ls = [int(x) for x in f]

ss = list(accumulate(ls))
