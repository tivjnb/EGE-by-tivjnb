a=('8'*99)+'1'
while '133' in a or '881' in a :
    if '133' in a:
        a=a.replace('133','81',1)
    else:
        a=a.replace('881','13',1)
print(a)