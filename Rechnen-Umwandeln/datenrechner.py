def einheit1(einheit):
##Bit or Byte:
    if any(i in einheit for i in("b", "bit")):
        faktor = 1
        faktor1 = 1
    elif any(i in einheit for i in("B", "Byte")):
        faktor = 8
        faktor1 = 8

##Kilo or Kibi:
    if einheit[0] == "k":
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
    #Input will be transformed to bit then to target size/form
    #Output will be a float
    faktor1 = einheit1(einheit_ist); faktor2 = einheit1(einheit_soll)     
    ergebnis = (bit*faktor1)/faktor2
    print(bit, einheit_ist,"=", ergebnis, einheit_soll)
    #  return ergebnis 

                                         ## 68MB -> kib
x = float(input("Paketgröße (float): ")) ## 68
y = str(input("aktuelle Einheit: "))     ## MB
z = str(input("Ziel-Einheit: "))         ## kib
# print(b_in_ib(x,y,z))
datenrechner(x,y,z)
