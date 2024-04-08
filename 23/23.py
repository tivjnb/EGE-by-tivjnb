def f(x,n):
    if x>n or x==20:
        return 0
    if x==n:
        return 1
    if x<n:
        return f(x+3,n)+f(x*2,n)+f(x**2,n)

print(f(2,128))