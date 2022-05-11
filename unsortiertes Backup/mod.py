
# def dlog_bf(p,a,b):
#     arr = []
#     a2 = a
#     for x in range(1,p):
#         c = (pow(a,x))%p
#         if c == b:
#             arr.append(x)
#         # a = c
#     return arr

# print(dlog_bf(107,5,91))

import numpy


arr = []
for x in range(1,107):
    c = (5**x)%107
    arr.append(c)
arr = numpy.sort(arr)
print(arr)