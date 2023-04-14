from sympy import Symbol
from sympy import div

x = Symbol('x')

def Poly(p,mod):
    q,r = div(p,mod,x) 
    return r


a = [
    x**4,
    x**4+x**3,
    x**4+x**3+x**2
    ]
b = [
    x**4+2*x**3+x**2,
    x**4+2*x**3+2*x**2+x,
    x**4+2*x**3+2*x+1
    ]


p = x**2 + 1
for i in a:
    print(Poly(i, p))
print("")
for i in b:
    print(Poly(i, p))