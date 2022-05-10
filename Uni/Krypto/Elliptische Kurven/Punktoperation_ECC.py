## Inversen Berechnung mit Modular Arithmetik
def modulare_inverse(zahl, mod):
    for inverse in range(1, mod):
        if (zahl % mod) * (inverse % mod) % mod == 1:
            return inverse

## Punktaddition
def P_plus_Q(punkt_P, punkt_Q, mod, neutrales_Element):
    ## Addition mit neutralem Element P + O:
    if punkt_Q[1] == neutrales_Element:
        return punkt_P[0],punkt_P[1]      
    
    ## Addition mit neutralem Element O + Q:
    elif punkt_P[1] == neutrales_Element:
        return punkt_Q[0],punkt_Q[1]      
    
    ## normale Addition zweier Punkte P + Q:
    elif punkt_Q[1] != neutrales_Element and punkt_P[1] != neutrales_Element:
        ## Sonderfall: wenn x von P gleich mit x von Q ist
        if punkt_P[0] == punkt_Q[0]:
            return punkt_P[0],neutrales_Element
        else:
            inverse = modulare_inverse(punkt_Q[0] - punkt_P[0], mod)

        s_addition = (punkt_Q[1] - punkt_P[1]) * inverse % mod
        x_addition = (s_addition**2 - punkt_P[0] - punkt_Q[0]) % mod
        y_addition = (s_addition * (punkt_P[0] - x_addition) - punkt_P[1]) % mod
        return x_addition, y_addition
        
    ## zur Sicherheit 
    else:
        raise Exception("\"What the hell happened here?\" \n - Antman") 

## Punktverdopplung
def P_mal_P(a, punkt_P, mod):
    s_verdopplung = ((3 * punkt_P[0]**2 + a) * modulare_inverse(2 * punkt_P[1], mod)) % mod
    x_verdopplung = (s_verdopplung**2 - 2 * punkt_P[0]) % mod
    y_verdopplung = (s_verdopplung * (punkt_P[0] - x_verdopplung) - punkt_P[1]) % mod
    return x_verdopplung, y_verdopplung

## Punktinversion
def P_inverse(punkt_P, mod):
    x_inversion = punkt_P[0]
    y_inversion = -punkt_P[1] % mod
    return x_inversion, y_inversion



