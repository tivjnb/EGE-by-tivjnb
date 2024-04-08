import time
#k=0
a=int(input())
def r_del(ch):
    ls=[]
    for i in range(2,ch//2+1):
        if ch%i==0:
            ls.append(i)
    return ls

def find_divisors(number):
    divisors = [1]
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    divisors.append(number)
    return divisors
def y_del(ch):
    #global ##k
    n=ch
    i=2
    while i<=n:
        #k+=1
        if n%i==0:
            yield i
            n//=i
            i=2
        else:
            i+=1
t0=time.time()
print(find_divisors(a))
t1 = time.time()
deliteli=set([1])
for e2add in y_del(a):
    nl=[]
    for i in deliteli:
        #k+=1
        nl.append(i*e2add)
    for i in nl:
        #k+=1
        deliteli.add(i)
print(deliteli)
t2= time.time()
x=r_del(a)
t3= time.time()
x2=find_divisors(a)
print(x2)
t4=time.time()
print(t1-t0,t2-t1,t3-t2,t4-t3)
