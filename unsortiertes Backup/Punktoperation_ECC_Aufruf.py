from Punktoperation_ECC import P_plus_Q, P_mal_P, P_inverse

## Initialiesieren der Funktion mit Eingabe über Terminal

neutrales_Element = float('inf') # float besitzt einen Wert "im Unendlichen"
print("") # für bessere Ausgabe Optik
print("Eingabe:") # für bessere Ausgabe Optik

## Eingabe der Elliptischen Kurven Parameter
function_E = [int(input("(a) Koeffizient von x¹: ")),int(input("(b) Koeffizient von x⁰: "))]
mod = int(input("(mod) Gruppenindex: "))
operator = str(input("Gruppenoperation (+ für Punktaddition || * für Punktverdopplung || - für Punktinversion): "))
if not any(i in operator for i in("+","*","-")): raise ValueError("Ihre Eingabe ist kein Gruppenoperator") 

## Eingabe der Punkte P und Q als punkt_1 und punkt_2
print("(das neutrale Element O ist (0," , str(neutrales_Element) + "))") 
punkt_1 = [int(input("(x1) Punkt 1, x: ")),input("(y1) Punkt 1, y: ")]

## Wenn P das neutrale Element ist
if punkt_1[1] == "inf": 
    punkt_1[1] = neutrales_Element
else: 
    punkt_1[1] = int(punkt_1[1]) 

## zu rechnende Operation: Punktaddition
if operator == "+": 
    print("(das neutrale Element O ist (0," , str(neutrales_Element) + "))") 
    punkt_2 = [int(input("(x2) Punkt 2, x: ")),input("(y2) Punkt 2, y: ")]

    ## Wenn Q das neutrale Element ist
    if punkt_2[1] == "inf": 
        punkt_2[1] = neutrales_Element
    else: 
        punkt_2[1] = int(punkt_2[1])

    print("") # für bessere Ausgabe Optik
    print("Ausgabe:") # für bessere Ausgabe Optik
    
    if punkt_1[0] == punkt_2[0]:
        print("(R) Punkt 1 + Punkt 2 = O (Punkt im Unendlichen)")
    else:
        print("(R) Punkt 1 + Punkt 2 =", P_plus_Q(punkt_1, punkt_2, mod, neutrales_Element))

## zu rechnende Operation: Punktverdopplung
elif operator == "*":
    print("") # für bessere Ausgabe Optik
    print("Ausgabe:") # für bessere Ausgabe Optik
    print("(R) 2 * Punkt 1 =", P_mal_P(function_E[0],punkt_1, mod))

## zu rechnende Operation: Punktinversion
elif operator == "-":
    print("") # für bessere Ausgabe Optik
    print("Ausgabe:") # für bessere Ausgabe Optik
    print("(R) -Punkt 1 =", P_inverse(punkt_1, mod))

print("") # für bessere Ausgabe Optik