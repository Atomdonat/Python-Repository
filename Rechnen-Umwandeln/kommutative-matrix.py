from matrix_multiplication import *

MatA = [[  1,  2,  3,  4,  5,  6],
        [  7,  8,  9, 10, 11, 12],
        [ 13, 14, 15, 16, 17, 18],
        [ 19, 20, 21, 22, 23, 24],
        [ 25, 26, 27, 28, 29, 30],
        [ 31, 32, 33, 34, 35, 36]]

MatB = [[ 1,  7, 13, 19, 25, 31],
        [ 2,  8, 14, 20, 26, 32],
        [ 3,  9, 15, 21, 27, 33],
        [ 4, 10, 16, 22, 28, 34],
        [ 5, 11, 17, 23, 29, 35],
        [ 6, 12, 18, 24, 30, 36]]

multiplyMatrix(len(MatA), len(MatA[0]), MatA,
               len(MatB), len(MatB[0]), MatB)
multiplyMatrix(len(MatB), len(MatB[0]), MatB,
               len(MatA), len(MatA[0]), MatA)