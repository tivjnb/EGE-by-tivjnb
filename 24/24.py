f= open('24.txt').read()
chs='1234567890'
alp=set(f)
for i in alp:
    if i not in chs:
        f=f.replace(i,' ')
ls=sorted(list(map(int,f.split())),reverse=True)
for i in ls:
    if i%2==0:
        print(i)
        break