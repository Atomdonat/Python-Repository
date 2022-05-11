import sympy as sp
import numpy as np

def a_hoch_kardinalität(ran, prime, op):
    kard = prime - ran
    if op == "*":
        for i in range(ran,prime):
            erg = pow(i,kard)%prime
            print("Ergebnis:", str(i) + "^" + str(kard), "mod", str(prime), "≡", str(erg))
    if op == "+":
        for i in range(ran,prime):
            erg = (kard * i)%prime
            print("Ergebnis:", str(kard) + "*" + str(i), "mod", str(prime), "≡", str(erg))

x = int(input("kleinste Zahl der Gruppe: "))
y = int(input("Gruppenindex: "))
z = str(input("Gruppenoperator (+ oder *): "))
a_hoch_kardinalität(x,y,z)