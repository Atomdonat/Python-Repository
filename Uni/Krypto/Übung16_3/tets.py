import math

def modular_inverse(a, m):
    for i in range(1, m):
        if((a%m)*(i%m) % m==1):
            print(i)
            return i

def baby_step(a, m, p):
    a_b = []
    for j in range(m):
        c = a**j % p
        a_b.append(c)
    # print("Ergebnis Baby-Step-Phase:", a_b)#list(sorted(a_b)))
    return a_b

def giant_step(a, b, p):
    m = math.ceil(math.sqrt(p-1))
    a_inv_m = modular_inverse(a**(m),p)
    
    a_b = []
    for k in range(m):
        c = b * a_inv_m**k % p
        a_b.append(c)
    return a_b

print(giant_step(34,181,233))
arr = baby_step(34,16,233)
barr = []
for i in range(len(arr)):
    barr.append([i,arr[i]])
print(barr)