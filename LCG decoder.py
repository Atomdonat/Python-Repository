def ge(m, k1, k2, k3, k4, k5):      # function of gaussian elimination
    def modinv(a):                  # modular inverse
        for i in range(1, m):
            if((a%m)*(i%m) % m==1):
                return i
    
    k21 = modinv(k2)                # modular inverse of 1. key
    k31 = modinv(k3)                # modular inverse of 2. key
    k41 = modinv(k4)                # modular inverse of 3. key
        
    #shortcuts of longer terms
    kh1 = (k3 * k21 - k4 * k31) % m 
    kh2 = (k1 * k21 - k2 * k31) % m
    kh3 = (k21 - k31) % m
    kh4 = (k3 * k21 - k5 * k41) % m
    kh5 = (k1 * k21 - k3 * k41) % m
    kh6 = (k21 - k41) % m
        
    kh21 = modinv(kh2)
    kh51 = modinv(kh5)

    kh7 = (kh1 * kh21 - kh4 * kh51) % m
    kh8 = (kh3 * kh21 - kh6 * kh51) % m
    
    kh81 = modinv(kh8)
    
    # parameter a to c 
    c = (kh7 * kh81) % m
    b = (kh1 * kh21 - c * kh3 * kh21) % m
    a = (k3  * k21 - b * k1 * k21 - c * k21) % m

    # array of all parameters for easier usage
    d = [a, b, c]
    return d
        

e = str(input("Cipher in hex: "))                   #e.g. 2D 5E 6B E8 1 58 E1 EC C4 C9 3C 95 FB 9 D2 65 FE 24 B1 A6 9B 46 9C D 11 EF F C1
x = str(input("Known-Plaintext: ")).encode('utf-8') #e.g. https://
m = int(input("Modulus: "))                         #e.g. 257 for utf-8

x = x.hex()                                         # Plaintext from UTF-8/ASCII to HEX
x = str(x)                                          #     "     from HEX         to String
n = []                                              # empty array for every pair of hex code 
for i in range(0,len(x),2):
    h = x[i:i+2]                                    # pairs of hex Code
    n.append(h)     
x = n                                               # Plaintext is now hex in an array

s = e.split()                                       # split the whole Cipher into pairs of two chars per string

# key 1-5  (Plaintext XOR Cipher)
k1 = int(s[0], 16) ^ int(x[0], 16)
k2 = int(s[1], 16) ^ int(x[1], 16)
k3 = int(s[2], 16) ^ int(x[2], 16)
k4 = int(s[3], 16) ^ int(x[3], 16)
k5 = int(s[4], 16) ^ int(x[4], 16)

k = ge(m, k1, k2, k3, k4, k5)                       # k = d[a,b,c] => k[0] = a, k[1] = b, k[2] = c

key = [k1, k2]                                      # array for every key

for i in range(2,len(s)):                           # adding next keys to key[]
    k3 = (k[0]*k2+k[1]*k1+k[2])%m   
    k1 = k2
    k2 = k3
    key.append(k3)              

j = []                                              # Cipher into array in hex values i.e. j=['0x2D', '0x5E',..., '0xC1']
for i in range(0,len(s)):
    j.append(int(s[i], 16))

k = []                                              # whole Plaintext in hex (Keys XOR Cipher)
for i in range(0,len(key)):
    f = key[i] ^ j[i]
    k.append(f)

l = [chr(x) for x in k]                             # whole PLaintext in UTF-8 characters
plain = ""                          
for i in range(0,len(s)): 
    plain += l[i]

print("whole Plaintext: ", plain)   


'''
declaration of used parameters:

a               = Parameter a in Gaussian Elimination
b               = Parameter a in Gaussian Elimination
c               = Parameter a in Gaussian Elimination
d               = array of all Parameter in Gaussian Elimination
e               = Ciphertext
f               = 
h               = 
i               = 
j               = 
k               = 
k1, k2, ...     = keys
kh1, kh2, ...   = helping variables (shorter terms) in Gaussian Elimination
m               = Modulus for Gaussian Elimination, etc.
n               = 
plain           = whole Plaintext
s               = 
x               = known Plaintext
'''