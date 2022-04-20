def ggt(A,B):
    a= A
    b = B
    t = 0
    while b >0:
        t =b
        b= a % b  #6
        a= t      #7
    return a

print(ggt(11,13))