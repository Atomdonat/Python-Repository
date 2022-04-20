from sympy import *
r = limit(m, m, oo)

for m in range(1,r):
    if m != 3:
        rest = (4 * m * m * m + 11 * m)%3
        print(rest)
