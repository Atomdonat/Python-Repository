import Programmierübung1_def as p

argument_list = [
    [([1, 3, 2], [1, 2, 3]), [1, 3, 2]],
    [([3, 1, 2], [2, 3, 1]), [1, 2, 3]],
    [([2, 1, 3], [3, 2, 1]), [3, 1, 2]],
    [([2, 3, 1], [3, 1, 2]), [1, 2, 3]],
    [([3, 2, 1], [2, 1, 3]), [2, 3, 1]],
    [([6, 1, 2, 3, 5, 4], [6, 2, 1, 4, 3, 5]), [4, 1, 6, 3, 2, 5]],
    [([4, 3, 2, 1], [4, 3, 2, 1]), [1, 2, 3, 4]],
    [([5, 4, 3, 2, 1], [5, 4, 3, 2, 1]), [1, 2, 3, 4, 5]],
]
for args, result in argument_list:
    if not p.multiply_permutations(*args) == result:
        raise AssertionError()

argument_list = [
    [[1, 3, 2], [1, 3, 2]],
    [[1, 2, 3], [1, 2, 3]],
    [[3, 1, 2], [2, 3, 1]],
    [[2, 1, 3, 5, 4], [2, 1, 3, 5, 4]],
    [[4, 1, 3, 2], [2, 4, 3, 1]],
    [[2, 3, 4, 5, 1], [5, 1, 2, 3, 4]],
    [[2, 3, 4, 5, 1, 6], [5, 1, 2, 3, 4, 6]],
]
for arg, result in argument_list:
    if not p.inverse_perm(arg) == result:
        raise AssertionError()

argument_list = [
    [([5, 1, 2, 3, 4], 5), [5, 4, 3, 2, 1]],
    [([5, 1, 2, 3, 4], 1), [1, 5, 4, 3, 2]],
    [([5, 1, 2, 3, 4], 2), [2, 1, 5, 4, 3]],
    [([7, 8, 9, 1, 3, 2, 4, 6, 5], 1), [1, 7, 4]],
    [([7, 8, 9, 1, 3, 2, 4, 6, 5], 3), [3, 9, 5]],
    [([7, 8, 9, 1, 3, 2, 4, 6, 5], 2), [2, 8, 6]],
    [([1, 3, 2, 5, 4], 1), [1]],
    [([1, 3, 2, 5, 4], 2), [2, 3]],
    [([1, 3, 2, 5, 4], 5), [5, 4]],
]
for args, result in argument_list:
    if not p.cycle_containing(*args) == result:
        raise AssertionError()

argument_list = [
    [[1, 3, 2], [[3, 2], [1]]],
    [[1, 2, 3], [[3], [2], [1]]],
    [[3, 1, 2], [[3, 2, 1]]],
    [[2, 3, 1], [[3, 1, 2]]],
    [[2, 1, 3], [[3], [2, 1]]],
    [[3, 2, 1], [[3, 1], [2]]],
    [[7, 8, 9, 1, 3, 2, 4, 6, 5], [[9, 5, 3], [8, 6, 2], [7, 4, 1]]],
    [[2, 3, 4, 5, 1, 6], [[6], [5, 1, 2, 3, 4]]],
    [[7, 8, 9, 1, 3, 2, 4, 6, 5], [[9, 5, 3], [8, 6, 2], [7, 4, 1]]],
    [[9, 1, 2, 3, 4, 5, 6, 7, 8], [[9, 8, 7, 6, 5, 4, 3, 2, 1]]],
]

for arg, result in argument_list:
    if not p.cycle_decomposition(arg) == result:
        raise AssertionError()

argument_list = [
    [[1, 3, 2], True],
    [[1, 2, 3], False],
    [[3, 1, 2], False],
    [[2, 3, 1], False],
    [[7, 8, 9, 1, 3, 2, 4, 6, 5], False],
    [[2, 3, 4, 5, 1, 6], False],
    [[7, 8, 9, 1, 3, 2, 4, 6, 5], False],
]
for arg, result in argument_list:
    if not p.is_even(arg) == result:
        raise AssertionError()

print("Yay no mistake")