import Punktoperation_ECC as pop

def double(a_E, Punkt, mod):
    double_Punkt = pop.P_mal_P(a_E, Punkt, mod)
    print("D: 2 * (" + str(Punkt[0]) + "," + str(Punkt[1]) + ") ≡", str(double_Punkt), "mod", str(mod))
    return double_Punkt

def add(Punkt_Q, Punkt_P, mod):
    P_add_Q = pop.P_plus_Q(Punkt_P, Punkt_Q, mod, pop.modulare_inverse(Punkt_Q[0] - Punkt_P[0], mod))
    print("A: (" + str(Punkt_Q[0]) + ",", str(Punkt_Q[1]) + ")", "+", str(Punkt_P), "≡", str(P_add_Q), "mod", str(mod))
    return P_add_Q

def double_and_add(a_E, Punkt_alt, k_pr, mod):
    Punkt_neu = Punkt_alt
    k_bin = bin(k_pr)
    k_bin2 = k_bin[3:len(k_bin)]

    print("")
    print("0d" + str(k_pr) + " = " + str(k_bin))
    print("")

    for i in k_bin2:
        if i == "1":
            Punkt_neu = add(Punkt_alt, double(a_E, Punkt_neu, mod), mod)
        if i == "0":
            Punkt_neu = double(a_E, Punkt_neu, mod)

    print("")
    print("Ergebnis:", str(k_pr), "* (" + str(Punkt_alt[0]) + ",", str(Punkt_alt[1]) + ") mod", str(mod), "≡",  str(Punkt_neu))
    print("")

# input("Was wird berechnet: ")

a_E = int(input("(a_E) Koeffizient von x¹: "))
mod = int(input("(mod) Gruppenindex: "))
P   = [int(input("(x) Punkt, x: ")),int(input("(y) Punkt, y: "))]
a   = int(input("(a) privater Schlüssel: ")) 
double_and_add(a_E,P,a,mod)

