def modinv(a):
    for i in range(1, m):
        if((a%m)*(i%m) % m==1):
            return i

m=257
s2 = 19
s3 = 57
s4 = 62

s21 = modinv(s2)
s31 = modinv(s3)
s41 = modinv(s4)


print(s21)
print(s31)
print(s41)
