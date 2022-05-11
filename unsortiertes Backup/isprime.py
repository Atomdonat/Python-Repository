import sympy

prime = int(input())

if sympy.isprime(prime) == True:
    print("Ist Prime")
else:
    print("nicht Prime")