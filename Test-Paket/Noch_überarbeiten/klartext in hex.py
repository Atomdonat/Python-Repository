
x = str(input("bekannter Klartext: ")).encode('utf-8')
x = x.hex()
print(x)
x = str(x)

n = []
for i in range(0,len(x),2):
    h = x[i:i+2]
    print(h)
    n.append(h)
print(n)
