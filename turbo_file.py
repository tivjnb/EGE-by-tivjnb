def f(n):
    total_ways=0
    for x in range(1,n//3):
        total_ways+=(((n-x)//2)-x )
    return total_ways
print(f(992538))