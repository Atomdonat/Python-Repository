import math

def primfaktorzerlegung_4(a,b1,b2,b3,b4):
    h1 = int(math.log(a,b1))
    h2 = int(math.log(a,b2))
    h3 = int(math.log(a,b3))
    h4 = int(math.log(a,b4))
    
    for p1 in range(0, h1):
        for p2 in range(0, h2):
            for p3 in range(0, h3):
                for p4 in range(0, h4):
                    c = (b1**p1) * (b2**p2) * (b3**p3) * (b4**p4)
                    if c == a:
                        print(a, "-", c, "=", a - c)
                        print("Primfaktorzerlegung (", a, ") =", b1,"^",p1,"*",b2,"^",p2,"*",b3,"^",p3,"*",b4,"^",p4,)
                        # return p1,p2,p3,p4
    
                        phi1 = b1**p1 - b1**(p1-1)
                        phi2 = b2**p2 - b2**(p2-1)
                        phi3 = b3**p3 - b3**(p3-1)
                        phi4 = b4**p4 - b4**(p4-1)
                        print("ϕ(n) =", phi1 * phi2 * phi3 * phi4)
                        
# print(primfaktorzerlegung_4(14151123772686459831257,19,37,53,101))
primfaktorzerlegung_4(14151123772686459831257,19,37,53,101)