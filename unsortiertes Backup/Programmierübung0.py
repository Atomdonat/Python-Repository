
def list_reverse(L, Lr = []):
    length = len(L)
    for i in range(0,length):
        Lr.append(L[length-i-1])
    return Lr

def maximum(L):
    return max(L)

def square_sum(L, a = 0):
    for i in L:
        a += i*i
    return a

def skew_sum(L, a = 0):
    s = len(L)
    for i in range(0,s):
        a += pow(L[i],s-i)
    return a

# argument_list = [
#     [[1,2,3], [3,2,1]],
#     [[1,2,3,4], [4,3,2,1]]
# ]
# for (arg, ergebnis) in argument_list:
#     if not list_reverse(arg) == ergebnis:
#         raise AssertionError("")


argument_list = [
    [[0, -1, 0.5, 0.75], 0.75],
    [[4, 5, 4, 5, 4, 5, 4, 5, 4], 5],
    [[3, -6, 45, 9, 12], 45],
    [[1.01, 0.99, 1.02, 0.989, 0.998], 1.02],
    [[1, 2, 3, 6, 7, 14, 21, 42], 42],
]
for arg, result in argument_list:
    if not maximum(arg) == result:
        raise AssertionError()

argument_list = [
    [[1, 2, 3], 14],
    [[1, 2, 3, 4], 30],
    [[-1, 2, -3, -4], 30],
    [[0, 0, 0], 0],
    [[2, 2, 2, 2], 16],
    [[1.5, 2.5, 3.5], 20.75],
]
for arg, result in argument_list:
    if not square_sum(arg) == result:
        raise AssertionError()

argument_list = [
    [[1, 2, 3], 8],
    [[1, 2, 3, 4], 22],
    [[-1, 2, -3, -4], 14],
    [[0, 0, 0], 0],
    [[2, 2, 2, 2], 30],
    [[1.5, 2.5, 3.5], 13.125],
]
for arg, result in argument_list:
    if not skew_sum(arg) == result:
        raise AssertionError()

print("No mistake so far")
# L = [1,2,3,4]
# print(square_sum(L))
