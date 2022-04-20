def list_reverse(L):
    Lr = []
    length = len(L)
    for i in range(0,length):
        Lr.append(L[length-i-1])
    return Lr

def maximum(L):
    return max(L)

def square_sum(L, a = 0):
    for i in L:
        a += i*i
    return a

def skew_sum(L, a = 0):
    s = len(L)
    for i in range(0,s):
        a += pow(L[i],s-i)
    return a

def sum_of_evens(L,a=0):
    for i in L:
        if i%2 == 0:
            a+=i
    return a

def matrix_transpose(a):
    rows = len(a)
    columns = len(a[0])

    b = []
    for j in range(columns):
        row = []
        for i in range(rows):
           row.append(a[i][j])
        b.append(row)

    return b

def divisors(n):
    a = []
    for i in range(1,n+1):
        if n%i == 0:
            a.append(i)
    return a

def is_prime(n):
    a = divisors(n)
    if len(a) == 2:
        return True
    else:
         return False

def prime_factorization(n):
    arr = []
    i = 2
    while n != 1:
        while n%i==0:
            if is_prime(i) == True:
                arr.append(i)
                n //= i
        i += 1
    return arr


