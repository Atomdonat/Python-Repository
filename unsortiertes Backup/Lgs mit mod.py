def lgs(m, s1, s2, s3, s4, s5):
    def modinv(a):
        for i in range(1, m):
            if((a%m)*(i%m) % m==1):
                return i

    s21 = modinv(s2)
    s31 = modinv(s3)
    s41 = modinv(s4)
    
    sh1 = (s3 * s21 - s4 * s31) % m
    sh2 = (s1 * s21 - s2 * s31) % m
    sh3 = (s21 - s31) % m
    sh4 = (s3 * s21 - s5 * s41) % m
    sh5 = (s1 * s21 - s3 * s41) % m
    sh6 = (s21 - s41) % m
    
    sh21 = modinv(sh2)
    sh51 = modinv(sh5)

    sh7 = (sh1 * sh21 - sh4 * sh51) % m
    sh8 = (sh3 * sh21 - sh6 * sh51) % m

    sh81 = modinv(sh8)

    c = (sh7 * sh81) % m
    b = (sh1 * sh21 - c * sh3 * sh21) % m
    a = (s3  * s21 - b * s1 * s21 - c * s21) % m

    #print("a          :", a)
    #print("b          :", b)
    #print("c          :", c)

    d = [a, b, c]
    return d

e = lgs(257, 29, 19, 57, 62, 149)

print(e[0])
print(e[1])
print(e[2])

