
def EuklidischerAlgorithmus(a,b):
    n = 1
    
    c = a - n * b  #a%b==c

    if c == 0 :
        return c
    else :
        while c > 0 :
            a = b
            b = c
            c = a - n * b
            return c

a = 9#int(input("a: "))
b = 41#int(input("b: "))

ea = EuklidischerAlgorithmus(a,b)

print(int(ea))     
