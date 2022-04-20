import Programmierübung0_def as p

argument_list = [
    [[1,2,3], [3,2,1]],
    [[1,2,3,4], [4,3,2,1]]
]
# for (arg, ergebnis) in argument_list:
#     if not p.list_reverse(arg) == ergebnis:
#         raise AssertionError("")

argument_list = [
    [[0, -1, 0.5, 0.75], 0.75],
    [[4, 5, 4, 5, 4, 5, 4, 5, 4], 5],
    [[3, -6, 45, 9, 12], 45],
    [[1.01, 0.99, 1.02, 0.989, 0.998], 1.02],
    [[1, 2, 3, 6, 7, 14, 21, 42], 42],
]
for arg, result in argument_list:
    if not p.maximum(arg) == result:
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
    if not p.square_sum(arg) == result:
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
    if not p.skew_sum(arg) == result:
        raise AssertionError()

argument_list = [
    [[1, 2, 3], 2],
    [[2, 2, 2], 6],
    [[3, 3, 3], 0],
    [[6, 8, 9, 10, 11], 24],
]
for arg, result in argument_list:
    if not p.sum_of_evens(arg) == result:
        raise AssertionError()

argument_list = [
    [[[1, 2], [2, 3]], [[1, 2], [2, 3]]],
    [[[1]], [[1]]],
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 4, 7], [2, 5, 8], [3, 6, 9]]],
    [[[0, 1, 0], [0, 1, 1], [1, 1, 1], [0, 0, 0]], [[0, 0, 1, 0], [1, 1, 1, 0], [0, 1, 1, 0]]],
    [[[1], [2], [3], [4]], [[1, 2, 3, 4]]],
]
for arg, result in argument_list:
    if not p.matrix_transpose(arg) == result:
        raise AssertionError()

argument_list = [
    [2, [1, 2]],
    [42, [1, 2, 3, 6, 7, 14, 21, 42]],
    [16, [1, 2, 4, 8, 16]],
    [13, [1, 13]],
]
for arg, result in argument_list:
    if not p.divisors(arg) == result:
        raise AssertionError()

argument_list = [
    [1, False],
    [2, True],
    [3, True],
    [4, False],
    [5, True],
    [6, False],
    [7, True],
    [8, False],
    [9, False],
]
for arg, result in argument_list:
    if not p.is_prime(arg) == result:
        raise AssertionError()

argument_list = [
    [4, [2, 2]],
    [8, [2, 2, 2]],
    [15, [3, 5]],
    [16, [2, 2, 2, 2]],
    [23, [23]],
    [42, [2, 3, 7]],
]
for arg, result in argument_list:
    if not p.prime_factorization(arg) == result:
        raise AssertionError()

print("No mistake so far")
