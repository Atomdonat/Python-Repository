modi = int(input("Bin: 1  Hex: 2"))

if modi == 1:
    a = int(input("erste BIN Zahl: "), 2)
    b = int(input("zweite BIN Zahl: "), 2)

    xor = a ^ b

    print(xor)

    for i in range(len(a)):
        k1 = int(a[i], 16) ^ int(b[i], 16)

if modi == 2:
    a = int(input("erste HEX Zahl: "), 16)
    b = int(input("zweite HEX Zahl: "), 16)

    xor = a ^ b
    xor = hex(xor)

    print(xor)

