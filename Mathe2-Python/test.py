def kgv(a,b):
    for i in range(1,min(a,b)+1):
        if i*max(a,b)%min(a,b) == 0:
            return i*max(a,b)

print(kgv(6,12))