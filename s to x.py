s = [33, 112, 0,152,82,233,2,152,213,60,174,228,206,74,6,229,81,180,186,113]
y = "75 67 4D 4E E6 1B 5F 2F F4 7C 9B 77 FA FB 58 CB CB AA 2C 34 86 67 D2 8D 10"

z = y.split()

for i in range(0,26):
    xor = hex(s[i] ^ z[i])
    h = xor.strip('0x')
    import codecs
    k = codecs.decode(h, 'hex').decode('utf-8')
    print(k)
