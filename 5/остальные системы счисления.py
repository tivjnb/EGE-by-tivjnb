#  Если нужна восьмиричная или шеснадцатиричная то
o = oct(123)
h = hex(123)
# Теоретически может понадобиться и другая

alp = '0123456789ABCDEFGHIJKL'
old_ch = 123
new_ch = ''
s_s = 16  # Основание системы счисления

while old_ch > 0:
    new_ch = alp[old_ch % s_s] + new_ch
    old_ch = old_ch // s_s


