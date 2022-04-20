def modular_inverse(a, m):
    for i in range(1, m):
        if((a%m)*(i%m) % m==1):
            # return i
            print("Inverse von", str(a), "ist:", str(i))

## bislang nur in Multiplikativer Gruppe

## eingabe Element parallel zu Inverse (input,print,input,print,...)
# mod = int(input("Gruppenindex: "))
# elemente = int(input("Anzahl gesuchter Inversen: "))
# for i in range(elemente):
#     zahl = int(input("Element: "))
#     # print(modular_inverse(i, mod))
#     modular_inverse(zahl,mod)

## erst eingabe der Elemente, dann Inverse
mod = int(input("Gruppenindex: "))
arr_elemente = []
elemente = int(input("Anzahl gesuchter Inversen: "))
for i in range(elemente):
    arr_elemente.append(int(input("Element: ")))

print("")

for i in arr_elemente:
    # print(modular_inverse(i, mod))
    modular_inverse(i,mod)
