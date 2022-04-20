import sympy

def multiplikative_ordnung(a, prime, ran=1):
    arr = []
    for i in range(ran, prime):
        c = pow(a, i) % prime
        d = str(a) + "^" + str(i) + " ≡ " + str(c)  # + " mod " + str(p)
        arr.append(d)

        if c == 1:
            e = len(arr)
            return  "ord(" + str(a) +") = " +  str(e)

def additive_ordnung(a, prime, ran=0):
    arr = []
    for i in range(ran, prime+1):
        c = (a * i) % prime
        d = str(i) + "*" + str(a) + " ≡ " + str(c)  # + " mod " + str(p)
        arr.append(d)

        if c == 0:
            e = len(arr)
            return arr, "ord(" + str(a) +") = " +  str(e)

def ordnung(prime, m, dic={}, dic2={}):
    if m == "*":
        if sympy.isprime(prime) == False:
            raise ValueError("Number is not a Prime")

        for j in range(1, prime):
            print(multiplikative_ordnung(j, prime))
        #   dic[j] = multiplikative_ordnung(j,prime)
        # return dic
        return "ヾ(⌐■_■)ノ♪"
    
    if m == "+":
        for j in range(0, prime):
            print(additive_ordnung(j, prime))
        #   dic2[j] = additive_ordnung(j,prime)
        # return dic2
        return "ヾ(⌐■_■)ノ♪"
    
x = input("Gruppenindex: ")
y = input("Verknüpfung (+ oder *): ")
print(ordnung(int(x),y))
