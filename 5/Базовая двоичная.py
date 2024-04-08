for n in range(1, 100):
    b = bin(n)[2:]
    '''
    Операции с числом
    '''
    r = int(b, 2)
    if r > 144:
        print(r)
        break
