a = 123456789
b = str(a)
if len(b) <= 3:
    print(b)
elif len(b) <= 6:
    print(b[0:len(b)-3] + "." + b[len(b)-3:len(b)])
elif len(b) <= 9:
    print(b[0:len(b)-6] + "." + b[len(b)-6:len(b)-3] + "." + b[len(b)-3:len(b)])