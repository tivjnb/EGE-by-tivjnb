'''
for i in range(500,2001):
    b=bin(i)[2:]

    r=int(b,2)
 '''

'''for i in range(1000,10000):
    si=str(i)
    ra=int(si[0])+int(si[2])
    rb=int(si[1])+int(si[3])
    r=str(min(rb,ra))+str(max(rb,ra))
    if r=='1114':
        print(i,r)'''

'''for i in range(10,1000):
    ls=[int(str(i)[y:y+2]) for y in range(0,len(str(i))-1)]
    r=max(ls)-min(ls)
    if r== 25:
        print(i,r)'''