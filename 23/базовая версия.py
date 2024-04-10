def f(x, n):
    if x > n or x == 20:
        return 0
    if x == n:
        return 1
    if x < n:
        return f(x+1, n)+f(x+2, n)+f(x*2, n)


'''
1)+1
2)+2
3)*2
от 5 до 23, включая 13 и не включая 20
'''
print(f(5, 13), f(13, 23))
