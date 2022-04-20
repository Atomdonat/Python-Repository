import sympy as s
import time

def ordnung_primes(prime, op):
    if op != "*":
        raise ValueError("Addition not implemented yet")
    else:
        if s.isprime(prime) != True:
            raise ValueError("Number is not Prime")
        else: 
            b = []
            for i in range(1, prime):
                c = pow(prime-1, i) % prime
                b.append(c)

                if c == 1:
                    e = len(b)
                    return e,"ord(" + str(a) +") = " +  str(e)
    raise ValueError("not sure what happened")

a = 3
print(ordnung_primes(a, "*"))


## while True
# ord2 = True
# a = 3
# timeout = 3600   # [seconds]
# timeout_start = time.time()
# while time.time() < timeout_start + timeout:
#     if ord2 == True: 
#         if s.isprime(a) == True:
#             if ordnung_primes(a, "*")!= 2:
#                 print("!!! ord(" + a + ") ≠ 2")
#                 ord2 = False
#             b = str(a)
#             if len(b) <= 3:
#                 print(b)
#             elif len(b) <= 6:
#                 print(b[0:len(b)-3] + "." + b[len(b)-3:len(b)])
#             elif len(b) <= 9:
#                 print(b[0:len(b)-6] + "." + b[len(b)-6:len(b)-3] + "." + b[len(b)-3:len(b)])
#             # etwa 72.000 tests pro Sekunde
#         a+=1
# print(a)
# print(timeout_start)
# print(time.time())