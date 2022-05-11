from sympy import Symbol
from sympy import div

x = Symbol('x')

def Poly(p,mod):
    q,r = div(p,mod,x) #quotient and remainder polynomial division by modulus mod
    return r.as_poly(x,domain='GF(2)') #Z_2

k_a = x**15
k_b = x**27

k_aba = x**15+x**13+x**12+x**7+x**5+x**4+x**3+x+1
k_abb = x**36 + x**27 + x**18 + x**9 + 1

p = x**5 + x**2 + 1
print("K_A:",Poly(k_a, p))
print("K_B:",Poly(k_b, p))
print("K_AB:",Poly(k_aba, p))
print("K_BA:",Poly(k_abb, p))