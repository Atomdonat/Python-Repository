import sympy

def multiplikative_ordnung(a, prime, ran=1):
    arr = []
    for i in range(ran, prime):
        c = pow(a, i) % prime
        d = str(a) + "^" + str(i) + " ≡ " + str(c)  # + " mod " + str(p)
        arr.append(d)

        if c == 1:
            e = len(arr)
            return  arr,"ord(" + str(a) +") = " +  str(e)

def additive_ordnung(a, prime, ran=0):
    arr = []
    for i in range(ran, prime+1):
        c = (a * i) % prime
        d = str(i) + "*" + str(a) + " ≡ " + str(c)  # + " mod " + str(p)
        arr.append(d)

        if c == 0:
            e = len(arr)
            return arr, "ord(" + str(a) +") = " +  str(e)

def ordnung(zahl, prime, m, dic={}, dic2={}):
    if m == "*":
        if sympy.isprime(prime) == False:
            raise ValueError("Number is not a Prime")
        print(multiplikative_ordnung(zahl, prime))
    if m == "+":
        print(additive_ordnung(zahl, prime))
    
x = int(input("Gruppenindex: "))
y = str(input("Verknüpfung (+ oder *): "))
a = int(input("zu berechnende Ordnung: "))
ordnung(a,x,y)
