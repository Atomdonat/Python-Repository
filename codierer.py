x = input("Klartext: ")
x = x.replace("ä","ae")\
     .replace("ö","oe")\
     .replace("ü","ue")
b = x.upper()

x = ''.join(char for char in x if char.isalnum())
b = ''.join(char for char in b if char.isalnum())

k = len(x)

y = b.replace("0", "NULL")     \
     .replace("1", "EINS")     \
     .replace("2", "00110010") \
     .replace("3", "00110011") \
     .replace("4", "00110100") \
     .replace("5", "00110101") \
     .replace("6", "00110110") \
     .replace("7", "00110111") \
     .replace("8", "00111000") \
     .replace("9", "00111001") \
     .replace("A", "01000001") \
     .replace("B", "01000010") \
     .replace("C", "01000011") \
     .replace("D", "01000100") \
     .replace("E", "01000101") \
     .replace("F", "01000110") \
     .replace("G", "01000111") \
     .replace("H", "01001000") \
     .replace("I", "01001001") \
     .replace("J", "01001010") \
     .replace("K", "01001011") \
     .replace("L", "01001100") \
     .replace("M", "01001101") \
     .replace("N", "01001110") \
     .replace("O", "01001111") \
     .replace("P", "01010000") \
     .replace("Q", "01010001") \
     .replace("R", "01010010") \
     .replace("S", "01010011") \
     .replace("T", "01010100") \
     .replace("U", "01010101") \
     .replace("V", "01010110") \
     .replace("W", "01010111") \
     .replace("X", "01011000") \
     .replace("Y", "01011001") \
     .replace("Z", "01011010") \

c01 = len(y)

#if c01%k == 0:
print("Chiffrat:\n",y)
#else:
#    print("!!fehlerhafte Eingabe!!")

#f = []

#for e in y:
#    if e == "1": f.append(True)
#    else: f.append(False)
#
#print(f)

