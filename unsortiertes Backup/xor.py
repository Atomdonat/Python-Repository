# modi = int(input("Bin: 1  Hex: 2"))

# if modi == 1:
#     a = int(input("erste BIN Zahl: "), 2)
#     b = int(input("zweite BIN Zahl: "), 2)

#     xor = a ^ b

#     print(xor)

#     for i in range(len(a)):
#         k1 = int(a[i], 16) ^ int(b[i], 16)

# if modi == 2:

#a = int(input("erste HEX Zahl: "), 16)
#b = int(input("zweite HEX Zahl: "), 16)

input = 0x7b1d2dae2bdb396131db5785e3547013
key   = 0x7b1d2dae2bdb396131db5785d50e1c25


xor = input ^ key
xor = bin(xor)
#xor = str(xor)
#n = []
# for i in range(0,len(xor),2):
#     h = xor[i:i+2]
#     n.append(h)
print(xor)

