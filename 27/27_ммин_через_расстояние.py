from time import time
t1=time()
f=open('27_B.txt','r')

k=int(f.readline())
n=int(f.readline())

ls=[int(x) for x in f.readlines()]
l=len(ls)
m=100_000_000
for x in range(0,l-(2*k)-2):
    s1=ls[x]
    if s1>=m:
        continue
    for y in range(x+k,l-k-1):
        s2=s1+ls[y]
        if s2>=m:
            continue
        for z in range(y+k,l):
            s3=s2+ls[z]
            m=min(s3,m)
print(m)
print(time()-t1)
#166998