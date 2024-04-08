for x in range(1,9):
    for y in range(1,1000):
        a='842'+str(x)+'5'
        b='8'+str(x)+'725'
        if (int(a,9)+y) % int(b,9) ==0:
            print(x,y)