f=open('1.txt','r')
table=[list(map(int,x.split())) for x in f]


count=0
for stroka in table:
    a=stroka[0]**2
    b=stroka[1]**2
    c=stroka[2]**2
    ss=sorted(stroka)
    if ss[1]+ss[0] >ss[2] :
        print(stroka)
        count+=1
print(count)