import sympy
##alt
def multiplikative_ordnung(a, prime, i=1):
    arr = []
    for i in range(1, prime):
        c = pow(a, i) % prime
        d = str(a) + "^" + str(i) + " ≡ " + str(c)  # + " mod " + str(p)
        arr.append(d)

        if c == 1:
            e = len(arr)
            return  e#"ord(" + str(a) +") = " +  str(e)

def additive_ordnung(a, prime, i=0):
    arr = []
    for i in range(1, prime+1):
        c = (a * i) % prime
        d = str(i) + "*" + str(a) + " ≡ " + str(c)  # + " mod " + str(p)
        arr.append(d)

        if c == 0:
            e = len(arr)
            return arr, "ord(" + str(a) +") = " +  str(e)

def primitiv_ordnung(prime, m, dic={}, dic2={}, arr = []):
    if m == "*":
        if sympy.isprime(prime) == False:
            raise ValueError("Number is not a Prime")

        for j in range(1, prime):
            if not multiplikative_ordnung(j, prime) in arr:
                arr.append(multiplikative_ordnung(j, prime))
            
            if j%4 == 0:
                print("/")
            if j%4 == 1:
                print("-")
            if j%4 == 2:
                print("\\")
            if j%4 == 3:
                print("|")
            if j%4 == 0:
                print("/")
            if j%4 == 1:
                print("-")
            if j%4 == 2:
                print("\\")
            if j%4 == 3:
                print("|")
            
            
            # print(multiplikative_ordnung(j, prime))
        #   dic[j] = multiplikative_ordnung(j,prime)
        # return dic
        return arr#"ヾ(⌐■_■)ノ♪"
    
    if m == "+":
        for j in range(0, prime):
            if not additive_ordnung(j, prime) in arr:
                arr.append(additive_ordnung(j, prime))
            # print(additive_ordnung(j, prime))
        #   dic2[j] = additive_ordnung(j,prime)
        # return dic2
        return arr#"ヾ(⌐■_■)ノ♪"

#\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//
def prime_factorization(n):
    arr = []
    i = 2
    while n != 1:
        while n%i==0:
            if sympy.isprime(i) == True:
                arr.append(i)
                n //= i
        i += 1
    return arr

def ord_effizient(index):
    primfac = prime_factorization(index)
    ordnungen = [1]
    for i in primfac:
        ordnungen.append(i)
        for j in primfac:
            if not j*i in ordnungen and j != i:
                ordnungen.append(j*i)
    ordnungen.sort()
    return ordnungen
    
# x = int(input("Gruppenindex: "))
# y = input("Verknüpfung (+ oder *): ")
# z = int(input("kleinste Zahl: "))
# print(primitiv_ordnung(z,x,y))

x = int(input("Gruppenindex: "))
y = input("Verknüpfung (+ oder *): ")
z = int(input("kleinste Zahl: "))
print(ord_effizient(x))
