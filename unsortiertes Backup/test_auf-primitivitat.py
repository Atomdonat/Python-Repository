
def primitiveElemente_von_G(group_index:int):
    ## Alle Gruppenelemente (1,2,...,p-1) in eine Liste schreiben
    def elemente_von_G(index:int):
        elemente = []
        for i in range(1,index):
            elemente.append(i)
        return elemente
    
    ## Finden der Ordnungen von G über die Gruppenkardinalität |G| = Phi(p)
    def ordnungen_von_G(prime:int):
        ord = []
        for i in range(1,prime):
            if (prime - 1)%i == 0:
                ord.append(i)
        return ord

    ## Ordnung von einem Element berechnen
    def ordnung_von_alpha(alpha:int, ordnungen:list, modulus:int):
        for i in ordnungen:
            if pow(alpha,i,modulus) == 1:
                return i

    ## Prüfen ob die Ordnung maximal ist <=> ist das Element primitiv
    def ist_primitiv(ordnung:int,modulus:int):
        return ordnung == modulus-1
    
    
    alle_primitiven_elemente = []
    for element in elemente_von_G(group_index):
        ## Sollte ein Element primitiv sein, wird es der Liste aller primitiven Elemente hinzugefügt:
        if ist_primitiv(ordnung_von_alpha(element,ordnungen_von_G(group_index),group_index),group_index) == True:
            alle_primitiven_elemente.append(element)
    
    # print("Primitive Elemente von G sind:", alle_primitiven_elemente)
    return alle_primitiven_elemente

# print(primitiveElemente_von_G(11))