def multiply_permutations(pi,sigma):  ##pi != π
    arr = []
    for i in range(len(pi)):
        arr.append(pi[sigma[i]-1])
    return arr

def inverse_perm(pi):
    arr = []
    for i in range(0,len(pi)):
        for j in range(0,len(pi)):
            if (pi[j] == i + 1):
                arr.append(j+ 1)
    return arr

def cycle_containing(pi, k):
    arr = [k]
    k_temp = k
    while pi[k_temp-1]!=k: 
        k_temp = pi[k_temp-1]
        if k_temp not in arr:
            arr.append(k_temp)
    return arr
    
def cycle_decomposition(pi):
    arr = []
    for i in range(len(pi),0,-1):
        if not any(i in j for j in arr):
            arr.append(cycle_containing(pi,i))
    return arr

def kgv(a,b):
    for i in range(1,min(a,b)+1):
        if i*max(a,b)%min(a,b) == 0:
            return i*max(a,b)

def is_even(pi):
    a = multiply_permutations(pi,pi)
    b = 1
    while a != pi:
        a = kgv(a, pi[b])
        b += 1
    c = b%2 == 0
    return c



