def teiler_von_n(n):
    a = []
    for i in range(1,n+1):
        if n%i == 0:
            a.append(i)
    return a

def primzahltest(n):
    a = teiler_von_n(n)
    if len(a) == 2:
        return True
    else:
         return False

def primfaktorzerlegung(n):
    arr = []
    i = 2
    while n != 1:
        while n%i==0:
            if primzahltest(i) == True:
                arr.append(i)
                n //= i
        i += 1
    return arr


def cardinality(number:int):
    phi = 1
    for i in primfaktorzerlegung(number):
        phi *= (i-1)
    return phi

# print(cardinality(10))