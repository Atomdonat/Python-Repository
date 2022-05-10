import check

def in_E(a,b,p):
    E = []
    for x in range(p):
        for y in range(p):
            if check.check(a,b,x,y,p) == True:
                E.append((x,y))
    E.append("O")
    return E

