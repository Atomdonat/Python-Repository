def ggT(m,n):
    if m < 0:
    a = max(m,n); b = min(m,n)
    while b > 0:
        t = b; b = a%b; a = t
    return a


a = int(input("a = "))
b = int(input("b = "))
print("ggt("+ str(a)+ ",", str(b) + ") =",ggT(a,b))
