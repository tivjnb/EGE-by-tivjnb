
def deliteli(ch):
    r=set()
    for i in range(2,int(ch**0.5)+1):
        if ch%i==0:
            r.add(i)
            r.add(ch//i)
    r.add(ch)
    return sorted(r)
sk=0
for x in range(800_000,100_000_000):
    for z in deliteli(x):
        if str(z)[-2:]=='14' and z!=14 and z!=x:
            print(z)
            sk+=1
            break

    if sk==5:
        break