import math

def modular_inverse(a, m):
    for i in range(1, m):
        if((a%m)*(i%m) % m==1):
            return i

def baby_step(a, m, p):
    a_b = []
    for j in range(m):
        c = a**j % p
        a_b.append(c)
    print("Ergebnis Baby-Step-Phase:", a_b)#list(sorted(a_b)))
    return a_b

def giant_step(a, b, m, p, k):
    a_inv_m = modular_inverse(a**(m),p)
    return b * a_inv_m**k % p

def baby_step_giant_step(a, b, p):
    m = math.ceil(math.sqrt(p-1))
    arr_b = baby_step(a, m, p)
    for k in range(m):
        for i in range(len(arr_b)):
            if giant_step(a, b, m, p, k) == arr_b[i]:
                print("Ergebnis Giant-Step-Phase:",giant_step(a, b, m, p, k), "∈", list(sorted(arr_b)))
                x = k*m+i
                print("Berechnung x:", str(k), "*", str(m),  "+", str(i), "=", str(x))
                return "x = " + str(x), str(a) + "^" + str(x) + " ≡ " + str(b) + " mod " + str(p)
                

a = int(input("Alpha: "))
b = int(input("Beta: "))
p = int(input("Gruppenindex: "))
print("")
print(baby_step_giant_step(a, b, p))