y = input("Chiffrat: ")
k2 = ''.join(char for char in y if char.isalnum())
k = len(k2)
n = 0

x = y.replace("00110010", "2") \
     .replace("00110011", "3") \
     .replace("00110100", "4") \
     .replace("00110101", "5") \
     .replace("00110110", "6") \
     .replace("00110111", "7") \
     .replace("00111000", "8") \
     .replace("00111001", "9") \
     .replace("01000001", "A") \
     .replace("01000010", "B") \
     .replace("01000011", "C") \
     .replace("01000100", "D") \
     .replace("01000101", "E") \
     .replace("01000110", "F") \
     .replace("01000111", "G") \
     .replace("01001000", "H") \
     .replace("01001001", "I") \
     .replace("01001010", "J") \
     .replace("01001011", "K") \
     .replace("01001100", "L") \
     .replace("01001101", "M") \
     .replace("01001110", "N") \
     .replace("01001111", "O") \
     .replace("01010000", "P") \
     .replace("01010001", "Q") \
     .replace("01010010", "R") \
     .replace("01010011", "S") \
     .replace("01010100", "T") \
     .replace("01010101", "U") \
     .replace("01010110", "V") \
     .replace("01010111", "W") \
     .replace("01011000", "X") \
     .replace("01011001", "Y") \
     .replace("01011010", "Z") \
     .replace("NULL",     "0") \
     .replace("EINS",     "1") \

x = ''.join(char for char in x if char.isalnum())

c01 = len(x)

#if k%c01 == 0:
print("Klartext:\n",x)
#else:
#    print("!!fehlerhafte Eingabe!!")
