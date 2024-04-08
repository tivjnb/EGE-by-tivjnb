f=open('1.txt','r')

znach=[]
for i in f:
    for y in i.split():
        znach.append(float(y.replace(',','.')))

pre=znach[0]
count=0
for zn in znach:
    if zn-pre>=2:
        count+=1
    pre=zn
print(count)
'''
f=open('1.txt','r')

znach=[]
for i in f:
    for y in i.split():
        znach.append(float(y.replace(',','.')))
mn=0
pre=znach[0]
count=0
for zn in znach:
    if pre-zn>mn:
        mn=zn
    pre=zn
print(mn)
'''