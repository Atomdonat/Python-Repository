def modular_inverse(a, m):
    for i in range(1, m):
        if((a%m)*(i%m) % m==1):
            return i

