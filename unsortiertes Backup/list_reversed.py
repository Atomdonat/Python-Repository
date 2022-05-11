def list_reverse(L, Lr = []):
    length = len(L)
    for i in range(0,length):
        Lr.append(L[length-i-1])
    return Lr

argument_list = [
    [[1,2,3], [3,2,1]],
    [[1,2,3,4], [4,3,2,1]]
]
for (arg, ergebnis) in argument_list:
    if not list_reverse(arg) == ergebnis:
        raise AssertionError("")
    