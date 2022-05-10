def check(a,b,x,y,mod):
    return (y**2)%mod == (x**3 + a*x+b)%mod

print(check(4,3,12,15,37))