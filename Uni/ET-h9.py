def z(r,l):
    c = l/(r*r)
    
    z1 = complex(r,l)
    z2 = r+1/complex(0,c)
    aufgabe = (z1 * z2)/(z1 + z2)

    z3 = complex(0,l)
    z4 = 1/complex(0,c)
    lösung1 = (1/r)
    lösung2 = 1/(r*(1+complex(0,r*c))) + complex(0,c)/(1+complex(0,r*c))
    lösung3 = 1/(2*r + complex(0,r*r) + 1/(complex(c)))
    lösung4 = r
    lösung5 = (2*r*r + r*(z3+z4))/(2*r + z3 + z4)
    lösung6 = 1/(r*(1+complex(0,r*c))) + 1/(r+1/complex(0,c))

    print(aufgabe, "|", lösung4, "|",)

    # if abs(aufgabe - lösung1)>0.5: #print("solution 1 is right")
    #     if abs(aufgabe - lösung2)>0.5: #print("solution 2 is right")
    #         if abs(aufgabe - lösung3)>0.5: #print("solution 3 is right")
    #             if abs(aufgabe - lösung4)<0.5: #print("solution 4 is right")
    #                 if abs(aufgabe - lösung5)<0.5: #print("solution 5 is right")
    #                     if abs(aufgabe - lösung6)>0.5: #print("solution 6 is right")
    #                        return True
    


def test(n):
    for i in range(1,n):
        for j in range(1,n):
            if z(i,j) == True: 
                print("right solution")           
    return "You fucking Donkey"

print(z(2.39, 0.000309))
