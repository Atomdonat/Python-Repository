def test(e):
    a = 85
    b = 194
    c = 12

    d = [a, b, c]
    return d

e1 = "75 67 4D 4E E6 1B 5F 2F F4 7C 9B 77 FA FB 58 CB CB AA 2C 34 86 67 D2 8D 10" #str(input("Chiffrat in HEX: "))
x1 = "68 74 74 70 73 3A 2F 2F" #str(input("bekannter Klartext (x1,...,x5): "))
m = 257 #int(input("Modulus: "))

s = e1.split()

k = test(1)

s1 = 29
s2 = 19
s3 = 57

key = [s1, s2]

for i in range(2,len(s)): 
    s3 = (k[0]*s2+k[1]*s1+k[2])%257
    s1 = s2
    s2 = s3
    key.append(s3)

j = []
for i in range(0,len(s)):
    j.append(int(s[i], 16))

k = []
for i in range(0,len(key)):
    d = key[i] ^ j[i]
    k.append(d)

l = [chr(x) for x in k]


m = ""
for i in range(0,len(s)): 
    m += l[i]

print(m)


