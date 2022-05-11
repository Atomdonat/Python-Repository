## benötigte Python-Imports:
import math
import Hilfsmethoden


## ist die Kurve E: y² ≡ x³ + a * x + b eine Elliptischen Kurve
def gültige_Kurve(Koeffizient_a_von_E, Koeffizient_b_von_E, mod):
    # 4 * a³ + 27 * b² !≡ 0 % mod
    return (4 * Koeffizient_a_von_E**3 + 27 * Koeffizient_b_von_E**2) % mod != 0

## ist der Punkt auf der Elliptischen Kurve E: y² ≡ x³ + a * x + b
def gültiger_Punkt(Koeffizient_a_von_E, Koeffizient_b_von_E, Punkt, mod):
    # y² ≡ x³ + a * x + b
    return Punkt[1]**2 % mod == Punkt[0]**3 + Koeffizient_a_von_E * Punkt[0] + Koeffizient_b_von_E % mod

## findet iterativ heraus, welche Punkte Elemente der Elliptischen Kurve E: y² ≡ x³ + a * x + b sind
def alle_Punkte_auf_E(Koeffizient_a_von_E,Koeffizient_b_von_E,mod):
    Punkte_auf_E = []
    for x in range(mod):
        for y in range(mod):
            if gültiger_Punkt(Koeffizient_a_von_E,Koeffizient_b_von_E,(x,y),mod) == True:
                Punkte_auf_E.append((x,y))
    Punkte_auf_E.append("O") # O ist hier das neutrale Element
    return Punkte_auf_E

## Baby-Step Giant-Step Quadratwurzelangriffs
def babystep_giantstep(Koeffizient_a_von_E, Koeffizient_b_von_E, mod):
    def baby_step(Koeffizient_a_von_E, Anzahl_Schritte, mod):
        # Ergebnis Baby-Step Phase = {a^i % mod}
        arr_baby_step = []
        for i in range(Anzahl_Schritte):
            ai = Koeffizient_a_von_E**i % mod
            arr_baby_step.append(ai)
        print("Ergebnis Baby-Step-Phase:", arr_baby_step)
        return arr_baby_step

    def giant_step(Koeffizient_a_von_E, Koeffizient_b_von_E, Anzahl_Schritte, mod, xg):
        # Ergebnis Giant-Step Phase = {b * inv(a^m)^xg}
        inv_am = Hilfsmethoden.modulare_inverse(Koeffizient_a_von_E**(Anzahl_Schritte),mod)
        return Koeffizient_b_von_E * inv_am**xg % mod

    def baby_step_giant_step(Koeffizient_a_von_E, Koeffizient_b_von_E, mod):
        # Anzahl Schritte = ⌈√X⌉
        Anzahl_Schritte = math.ceil(math.sqrt(mod-1))
        arr_baby_step = baby_step(Koeffizient_a_von_E, Anzahl_Schritte, mod)
        for aktuelles_xg in range(Anzahl_Schritte):
            for aktuelles_xb in range(len(arr_baby_step)):
                if giant_step(Koeffizient_a_von_E, Koeffizient_b_von_E, Anzahl_Schritte, mod, aktuelles_xg) == arr_baby_step[aktuelles_xb]:
                    print("Ergebnis Giant-Step-Phase:",giant_step(Koeffizient_a_von_E, Koeffizient_b_von_E, Anzahl_Schritte, mod, aktuelles_xg), "∈", list(sorted(arr_baby_step)))
                    x = aktuelles_xg * Anzahl_Schritte + aktuelles_xb
                    print("Berechnung x:", str(aktuelles_xg), "*", str(Anzahl_Schritte),  "+", str(aktuelles_xb), "=", str(x))
                    return "x = " + str(x), str(Koeffizient_a_von_E) + "^" + str(x) + " ≡ " + str(Koeffizient_b_von_E) + " mod " + str(mod)
    return baby_step_giant_step(Koeffizient_a_von_E, Koeffizient_b_von_E, mod)

## berechnet Punkt 1 + Punkt 2; 2 * Punkt 1; - Punkt 1 auf der Elliptischen Kurve E: y² ≡ x³ + a * x + b
def Punktoperationen_auf_E(Koeffizient_a_von_E, operator, mod, punkt_1 = [0,"inf"], punkt_2 = [0,"inf"]):
    ## Punktaddition
    def P_plus_Q(punkt_P, punkt_Q, mod, neutrales_Element):
        ## Addition mit neutralem Element P + O:
        if punkt_Q[1] == neutrales_Element:
            return [punkt_P[0],punkt_P[1]]      
        
        ## Addition mit neutralem Element O + Q:
        elif punkt_P[1] == neutrales_Element:
            return [punkt_Q[0],punkt_Q[1]]      
        
        ## normale Addition zweier Punkte P + Q:
        elif punkt_Q[1] != neutrales_Element and punkt_P[1] != neutrales_Element:
            ## Sonderfall: wenn x von P gleich mit x von Q ist
            if punkt_P[0] == punkt_Q[0]:
                return [punkt_P[0],neutrales_Element]
            else:
                inverse = Hilfsmethoden.modulare_inverse(punkt_Q[0] - punkt_P[0], mod)

            s_addition = (punkt_Q[1] - punkt_P[1]) * inverse % mod
            x_addition = (s_addition**2 - punkt_P[0] - punkt_Q[0]) % mod
            y_addition = (s_addition * (punkt_P[0] - x_addition) - punkt_P[1]) % mod
            return [x_addition, y_addition]
            
        ## zur Sicherheit 
        else:
            raise Exception("\"What the hell happened here?\" \n - Antman") 

    ## Punktverdopplung
    def P_mal_P(a, punkt_P, mod):
        s_verdopplung = ((3 * punkt_P[0]**2 + a) * Hilfsmethoden.modulare_inverse(2 * punkt_P[1], mod)) % mod
        x_verdopplung = (s_verdopplung**2 - 2 * punkt_P[0]) % mod
        y_verdopplung = (s_verdopplung * (punkt_P[0] - x_verdopplung) - punkt_P[1]) % mod
        return [x_verdopplung, y_verdopplung]

    ## Punktinversion
    def P_inverse(punkt_P, mod):
        x_inversion = punkt_P[0]
        y_inversion = -punkt_P[1] % mod
        return [x_inversion, y_inversion]
    
    neutrales_Element = float('inf')

    #ist Punkt 1 das neutrale Element?
    p1 = str(punkt_1[1])
    if p1 == "inf": 
        punkt_1[1] = str(neutrales_Element)
    else: 
        punkt_1[1] = int(punkt_1[1])

    #ist Punkt 2 das neutrale Element?
    p2 = str(punkt_2[1])
    if p2 == "inf": 
        punkt_2[1] = str(neutrales_Element)
    else: 
        punkt_2[1] = int(punkt_2[1])

    if operator == "+": 
        return P_plus_Q(punkt_1, punkt_2, mod, neutrales_Element)
    elif operator == "*": 
        return P_mal_P(Koeffizient_a_von_E, punkt_1, mod)
    elif operator == "-": 
        return P_inverse(punkt_1, mod)

## Effizientes multiplizieren mit Punkten auf der Elliptischen Kurve E: y² ≡ x³ + a * x + b
def double_and_add(Koeffizient_a_von_E, Punkt, Exponent, mod):
    def double(Koeffizient_a_von_E, mod, Punkt):
        return Punktoperationen_auf_E(Koeffizient_a_von_E, "*", mod, Punkt)

    def add(punkt_1, punkt_2, mod, Koeffizient_a_von_E):
        return Punktoperationen_auf_E(Koeffizient_a_von_E, "+", mod, punkt_1, punkt_2)

    def double_add(a_E, Punkt_alt, Exponent, mod):
        Punkt_neu = Punkt_alt
        k_bin = bin(Exponent)
        k_bin2 = k_bin[3:len(k_bin)]

        for i in k_bin2:
            if i == "1":
                Punkt_neu = add(Punkt_alt, double(a_E, Punkt_neu, mod), mod)
            if i == "0":
                Punkt_neu = double(a_E, Punkt_neu, mod)
        return Punkt_neu
    return double_add(Koeffizient_a_von_E, Punkt, Exponent, mod)