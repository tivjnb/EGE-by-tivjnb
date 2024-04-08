from itertools import product,permutations

def f(x,y,z,w):
    return ((x<=y) == (z<=w)) or (x and w)

for a1,a2,a3,a4,a5,a6 in product([0,1]*6):
    print(a1,a2,a3,a4,a5,a6)