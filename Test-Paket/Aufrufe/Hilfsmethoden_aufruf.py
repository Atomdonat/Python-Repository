## Square and Multiply
def square_and_multiply():
    def square(s, mod):
        s1 = s
        s = (s*s)%mod
        print("SQ : " + str(s1) + "^2 ≡ " + str(s))
        return s

    def multiply(base, m, mod):
        m1 = m
        m = (base*m)%mod 
        print("Mul: " + str(m1) + " * " + str(base) + " ≡ " + str(m))
        return m

    def sq_mul(base, exponent, mod):
        b = base
        e = bin(exponent)
        e2 = e[3:len(e)]

        print("")
        print("0d" + str(exponent) + " = " + str(e))
        print("")

        for i in e2:
            if i == "1":
                b = multiply(base, square(b, mod), mod)
            if i == "0":
                b = square(b, mod)

        print("")
        print("Ergebnis:", str(base) + "^" + str(exponent), "mod", str(mod), "≡",  str(b))
        print("")

    x1 = int(input("Basis: "))
    x2 = int(input("Exponent: "))
    x3 = int(input("Mod: "))
    sq_mul(x1,x2,x3)

square_and_multiply()