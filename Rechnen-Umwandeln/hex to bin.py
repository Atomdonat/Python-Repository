bin1 = int("0x7B1D2DAE2BDB396131DB5785D50E1C25", 2)
bin2 = int("0x8959856823008387754762d8476741e8", 2)

'''
n = []
for i in range(0,len(bin1),4):
    h = bin1[i:i+4]
    n.append(h)
bin1 = n


n = []
for i in range(0,len(bin2),4):
    h = bin2[i:i+4]
    n.append(h)
bin2 = n
'''

xor = bin1 ^ bin2

print(bin1)
print(bin2)
print(xor)