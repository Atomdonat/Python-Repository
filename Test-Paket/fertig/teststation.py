def ordnung_Punkt(Koeffizient_a_von_E, Punkt, mod):
    from Elliptische_Kurven import Punktoperationen_auf_E
    arr_punkte = []
    Punkt2 = Punkt
    while not Punkt in arr_punkte:
        Punkt2 = Punktoperationen_auf_E(Koeffizient_a_von_E, "*", mod, Punkt2)
        arr_punkte.append(Punkt2)
    arr_punkte.append([Punkt[0], float('inf')])
    return arr_punkte, len(arr_punkte)
    
print(ordnung_Punkt(2,[4,8],13))