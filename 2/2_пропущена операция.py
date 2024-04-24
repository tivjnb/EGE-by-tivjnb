#   Логическая функция F задаётся выражением (a∧b≡¬c)∧(b ? d).
#   На месте ? пропущена логическая операция.


def f(c, a, d, b):
    v1 = (a & b == (not(c))) and (b and d)
    v2 = (a & b == (not(c))) and (b == d)
    v3 = (a & b == (not(c))) and (b <= d)
    v4 = (a & b == (not(c))) and (b or d)
    return v1, v2, v3, v4

table = (
    [1, 0, 0, 0],
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0]
)

for i in table:
    print(f(*i))