## PC-Orientiert:
def badic_to_badic(wert, eingabeformat, ausgabeformat): #für b <= 10
    def badic_to_dec(wert, eingabeformat):
        wert2 = str(wert) 
        arr_wert = []
        for i in range(len(wert2)):
            arr_wert.append(int(wert2[i:i+1]))
        arr_wert.reverse()
        
        a = 0
        for i in range(len(arr_wert)):
            a += arr_wert[i] * eingabeformat**i
        return a

    def dec_to_badic(wert, ausgabeformat):
        ausgabe = ""
        while wert != 0:
            a = wert
            wert = wert//ausgabeformat
            rest = a-wert*ausgabeformat
            ausgabe += str(rest)
        # return list(reversed(arr))
        return ausgabe[::-1]
    return dec_to_badic(badic_to_dec(wert, eingabeformat),ausgabeformat)

def datentypen_ändern(wert, ist_typ, soll_typ):
    ## hex to ...
    def hex_to_bin(hex_zahl):
        hex_zahl = str(hex_zahl)
        return bin(int(hex_zahl))

    def hex_to_int(hex_zahl):
        return int(hex_zahl)

    def hex_to_str(hex_string):
        import codecs
        return str(codecs.decode(hex_string, "hex"),'utf-8')

    ## bin to ...
    def bin_to_hex(bin_zahl):
        return hex(bin_zahl)

    def bin_to_int(bin_zahl):
        return int(bin_zahl)

    def bin_to_str(bin_string):
        return "".join([chr(int(binary, 2)) for binary in bin_string.split(" ")])

    ## int to ...
    def int_to_hex(int_zahl:int):
        return hex(int_zahl)

    def int_to_bin(int_zahl:int):
        return bin(int_zahl)

    def int_to_str(int_zahl:int):
        return chr(int_zahl)

    ## str to ...
    def str_to_hex(string:str):
        return ' '.join(format(ord(x), 'x') for x in string)

    def str_to_bin(string:str):
        return ' '.join(format(ord(x), 'b') for x in string)

    def str_to_int(string:str):
        return ' '.join(format(ord(x), 'd') for x in string)
    
    if ist_typ == "hex":
        if soll_typ == "bin":
            return hex_to_bin(wert)
        elif soll_typ == "int":
            return hex_to_int(wert)
        elif soll_typ == "str":
            return hex_to_str(wert)
    elif ist_typ == "bin":
        if soll_typ == "hex":
            return bin_to_hex(wert)
        elif soll_typ == "int":
            return bin_to_int(wert)
        elif soll_typ == "str":
            return bin_to_str(wert)
    elif ist_typ == "int":
        if soll_typ == "hex":
            return int_to_hex(wert)
        elif soll_typ == "bin":
            return int_to_bin(wert)
        elif soll_typ == "str":
            return int_to_str(wert)
    elif ist_typ == "str":
        if soll_typ == "hex":
            return str_to_hex(wert)
        elif soll_typ == "bin":
            return str_to_bin(wert)
        elif soll_typ == "int":
            return str_to_int(wert)

def datenumrechner(bit:int, einheit_ist:str, einheit_soll:str):
    def einheit1(einheit):
    ##Bit or Byte:
        if any(i in einheit for i in("b", "bit")):
            faktor = 1
            faktor1 = 1
        elif any(i in einheit for i in("B", "Byte")):
            faktor = 8
            faktor1 = 8

    ##Kilo or Kibi:
        if einheit[0] == "k" or einheit[0] == "K":
            if einheit[1] == "i":
                faktor = pow(2,10)*faktor1 
            else: 
                faktor = (1e3)*faktor1
    ##Mega or Mebi:
        elif einheit[0] == "M":
            if einheit[1] == "i":
                faktor = pow(2,20)*faktor1 
            else: 
                faktor = (1e6)*faktor1
    ##Giga or Gibi:
        elif einheit[0] == "G":
            if einheit[1] == "i":
                faktor = pow(2,30)*faktor1 
            else: 
                faktor = (1e9)*faktor1
    ##Tera or Tebi:
        elif einheit[0] == "T":
            if einheit[1] == "i":
                faktor = pow(2,40)*faktor1 
            else: 
                faktor = (1e12)*faktor1
    ##Peta or Pebi:
        elif einheit[0] == "P":
            if einheit[1] == "i":
                faktor = pow(2,50)*faktor1 
            else: 
                faktor = (1e15)*faktor1
            
    ##Exa or Exbi:
        elif einheit[0] == "E":
            if einheit[1] == "i":
                faktor = pow(2,60)*faktor1 
            else: 
                faktor = (1e18)*faktor1
            
    ##Zetta or Zebi:
        elif einheit[0] == "Z":
            if einheit[1] == "i":
                faktor = pow(2,70)*faktor1 
            else: 
                faktor = (1e21)*faktor1
            
    ##Yotta or Yobi:
        elif einheit[0] == "Y":
            if einheit[1] == "i":
                faktor = pow(2,80)*faktor1 
            else: 
                faktor = (1e24)*faktor1
            
        return faktor

    def datenrechner(bit, einheit_ist="", einheit_soll=""):
        ## Input will be transformed to bit then to target size/form
        ## Output will be a float
        faktor1 = einheit1(einheit_ist); faktor2 = einheit1(einheit_soll)     
        ergebnis = (bit*faktor1)/faktor2
        print(bit, einheit_ist,"=", ergebnis, einheit_soll)
        #  return ergebnis 

    return datenrechner(bit, einheit_ist, einheit_soll)

def dotted_number(zahl):
    dotted_zahl = str(zahl)
    if len(dotted_zahl) <= 3:
        return dotted_zahl
    elif len(dotted_zahl) <= 6:
        return str(dotted_zahl[0:len(dotted_zahl)-3] + "." + dotted_zahl[len(dotted_zahl)-3:len(dotted_zahl)])
    elif len(dotted_zahl) <= 9:
        return str(dotted_zahl[0:len(dotted_zahl)-6] + "." + dotted_zahl[len(dotted_zahl)-6:len(dotted_zahl)-3] + "." + dotted_zahl[len(dotted_zahl)-3:len(dotted_zahl)])
    
def list_reverse(L, Lr):
    length = len(L)
    for i in range(0,length):
        Lr.append(L[length-i-1])
    return Lr

'''
▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰
'''

## Inverse und ggT:
def ggT(Zahl1, Zahl2):
    while Zahl2 != 0:
        Zahl1,Zahl2 = Zahl2, Zahl1%Zahl2
    return Zahl1

def kgv(a, b):
    for i in range(1,min(a,b)+1):
        if i*max(a,b)%min(a,b) == 0:
            return i*max(a,b)

def modulare_inverse(zahl, mod):
    # alt
    # for inverse in range(1, mod):
    #     if zahl * inverse % mod == 1:
    #         return inverse
    
    return pow(zahl,-1,mod)

def erweiterter_euklid(zahl, mod):
    q = [0,0]
    s = [1,0]
    t = [0,1]
    r = [zahl, mod]
    i = 2
    while r[i-1] > 1: # >= 1 für formale Abbruchbedingung
        r.append(r[i-2]%r[i-1])
        q.append(int((r[i-2]-r[i])/r[i-1]))
        s.append(s[i-2]-q[i]*s[i-1])
        t.append(t[i-2]-q[i]*t[i-1])
        i += 1
    return s[i-1],t[i-1]

def chinesischer_restsatz(a, m):
    a0, m0 = a[0], m[0]
    for i in range(1, len(a)):
        ai, mi = a[i], m[i]
        q = m0 * mi
        x, y = erweiterter_euklid(m0, mi)
        r = (a0 + (ai - a0) * x * m0) % q
        a0, m0 = r, q
    return a0

'''
▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰
'''

## Primzahlen:
def teiler_von_n(n):
    a = []
    for i in range(1,n+1):
        if n%i == 0:
            a.append(i)
    return a

def primzahltest(n):
    a = teiler_von_n(n)
    if len(a) == 2:
        return True
    else:
         return False

def primfaktorzerlegung(n):
    arr = []
    i = 2
    while n != 1:
        while n%i==0:
            if primzahltest(i) == True:
                arr.append(i)
                n //= i
        i += 1
    return arr

def kardinalitat(number:int):
    phi = 1
    for i in primfaktorzerlegung(number):
        phi *= (i-1)
    return phi

'''
▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰
'''

## mögliche Ordnungen:
def ordnung_Liste(index):
    primfac = primfaktorzerlegung(index)
    ordnungen = [1]
    for i in primfac:
        ordnungen.append(i)
        for j in primfac:
            if not j*i in ordnungen and j != i:
                ordnungen.append(j*i)
    ordnungen.sort()
    return ordnungen

def ordnung_ElliptischeKurve(Koeffizient_a_von_E, Koeffizient_b_von_E, mod):
    from Elliptische_Kurven import alle_Punkte_auf_E as ap
    return len(ap(Koeffizient_a_von_E,Koeffizient_b_von_E,mod))

def ordnung_Punkt(Koeffizient_a_von_E, Punkt, mod):
    from Elliptische_Kurven import Punktoperationen_auf_E
    arr_punkte = []
    Punkt2 = Punkt
    while not Punkt in arr_punkte:
        Punkt2 = Punktoperationen_auf_E(Koeffizient_a_von_E, "*", mod, Punkt2)
        arr_punkte.append(Punkt2)
    arr_punkte.append([Punkt[0], float('inf')]) ## neutrales Element
    return len(arr_punkte)

'''
▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰
'''

## Polynome:
def eval_poly(f, x):
    grad, f_x = len(f), 0
    for i in range(grad):
        f_x += f[i] * x**i
    return f_x

def Polynome_addieren(f,g):
    while len(g) < len(f):
        g.append(0)
    while len(f) < len(g):
        f.append(0)

    f_add_g_x = []
    for i in range(len(f)):
        f_add_g_x.append(f[i] + g[i])

    s = set(f_add_g_x)
    if len(s)==1 and 0 in s:
        return []
    else:
        return f_add_g_x

def Polynome_multiplizieren(f,g):
    f_mul_g_x = [0]*(len(f)+len(g)-1)
    for o1,i1 in enumerate(f):
        for o2,i2 in enumerate(g):
            f_mul_g_x[o1+o2] += i1*i2
    
    s = set(f_mul_g_x)
    if len(s)==1 and 0 in s:
        return []
    else:
        return f_mul_g_x

'''
▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰
'''

## effizientes Rechnen:
def square_and_multiply(base, exponent, mod):
    def square(s, mod):
        return (s*s)%mod

    def multiply(base, m, mod):
        return (base*m)%mod 

    def sq_mul(base, exponent, mod):
        b = base
        e = bin(exponent)
        e2 = e[3:len(e)]

        for i in e2:
            if i == "1":
                b = multiply(base, square(b, mod), mod)
            if i == "0":
                b = square(b, mod)
        return b
    return sq_mul(base, exponent, mod)

def double_and_add(base, koeffizient, mod):
    def double(base, mod):
        return 2 * base % mod

    def add(base_new, base_old, mod):
        return (base_new + base_old) % mod

    def double_and_add(base_alt, koeffizient, mod):
        base_neu = base_alt
        k_bin = bin(koeffizient)
        k_bin2 = k_bin[3:len(k_bin)]

        for i in k_bin2:
            if i == "1":
                base_neu = add(base_alt, double(base_neu, mod), mod)
            if i == "0":
                base_neu = double(base_neu, mod)
        return base_neu
    return double_and_add(base, koeffizient, mod)

'''
▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰
'''

## Primititive Elemente einer zyklischen Gruppe:
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
        for i in range(1,kardinalitat(prime)+1):
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