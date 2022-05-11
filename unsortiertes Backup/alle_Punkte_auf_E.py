def check(a,b,x,y,mod):
    return (y**2)%mod == (x**3 + a*x+b)%mod

def alle_Punkte_auf_E(Koeffizient_a_von_E,Koeffizient_b_von_E,mod):
    Punkte_auf_E = []
    for x in range(mod):
        for y in range(mod):
            if check(Koeffizient_a_von_E,Koeffizient_b_von_E,x,y,mod) == True:
                Punkte_auf_E.append((x,y))
    Punkte_auf_E.append("O") # O ist hier das neutrale Element
    return Punkte_auf_E
