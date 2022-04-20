e = "75 67 4D 4E E6 1B 5F 2F F4 7C 9B 77 FA FB 58 CB CB AA 2C 34 86 67 D2 8D 10"
x = "68 74 74 70 73 3A 2F 2F"

#e = str(input()) #Chiffrat in HEX
#x = str(input()) #Eingabe bekannter Klartext (x1,...,x5)

s = e.split()
t = x.split()

s1 = int(s[0], 16) ^ int(t[0], 16)
s2 = int(s[1], 16) ^ int(t[1], 16)
s3 = int(s[2], 16) ^ int(t[2], 16)
s4 = int(s[3], 16) ^ int(t[3], 16)
s5 = int(s[4], 16) ^ int(t[4], 16)

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

