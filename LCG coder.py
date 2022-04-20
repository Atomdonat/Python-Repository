x = str(input("Known-Plaintext: ")).encode('utf-8')
m = int(input("Modulus: "))

x = x.hex()
x = str(x)
n = []
for i in range(0,len(x),2):
    h = int(x[i:i+2],16)
    n.append(h)
x = n
print(x)

s1 = 69
s2 = 42
s3 = 59

a = 10
b = 20
c = 30

key = [s1, s2]

for i in range(2,len(x)): 
    s3 = (a*s2+b*s1+c)%m
    s1 = s2
    s2 = s3
    key.append(s3)
print(key)

e = []
for i in range(0,len(key)):
    d = key[i] ^ x[i]
    e.append(d)

f = []
for i in range(0,len(key)):
    g = hex(e[i])
    g = g.strip('0x')
    f.append(g)

print(f)

m = ""
for i in range(0,len(key)):
    m += " " + f[i]

print(m.upper())
