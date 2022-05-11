#Permutationstabelle



#x1,x2,y1,y2: HEX to BIN
x1 = 0xE349EDBF2E8A749D #bin(int(input("Firstplain in hex: "),16))
x2 = 0x1349114115611E91 #bin(int(input("Secondplain in hex: "),16))
y1 = 0x2E8A749D25CAC114 #bin(int(input("Firstcipher in hex: "),16))
y2 = 0x15611E91964296A7 #bin(int(input("Secondcipher in hex: "),16))


l0 = x1[0:32]
r0 = x1[32:64]
l1 = y1[0:32]
r1 = y1[32:64]

h1 = int(l0, 16) ^ int(r1, 16)

print(l1)
print(r0)
print(h1)