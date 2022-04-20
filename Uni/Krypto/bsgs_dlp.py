def dlp_bf_x(alpha,beta,mod):
    for i in range(mod):
        if alpha**i%mod == beta:
            return i

def baby_step(alpha,mod):

a = int(input("Alpha: "))
b = int(input("Beta: "))
m = int(input("Gruppenindex: "))
print(dlp_bf_x(a,b,m))