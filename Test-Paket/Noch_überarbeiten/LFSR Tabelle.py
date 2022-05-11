b = str(input("Initialvector: ")) #Initialvektor Bsp. 1 0 0 0 0

s = b.split()

iv = []
for i in range(0,len(s)):
    iv.append(int(s[i]))

v1 = iv
i = 0

print(v1, i)   
v2 = [0,0,0,0]

while v2 != [0,1,0,1]:  #Initivalvektor per Hand eingeben
    v2[0] = v1[2] ^ v1[3] 
    v2[1] = v1[0]
    v2[2] = v1[1]
    v2[3] = v1[2]
    i += 1                  #Anzahl Zeilen
    print(v2, i) 
    v1[0] = v2[0]
    v1[1] = v2[1]
    v1[2] = v2[2]
    v1[3] = v2[3]
   
    