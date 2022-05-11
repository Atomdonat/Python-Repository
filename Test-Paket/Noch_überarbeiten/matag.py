from matrix_multiplication import *

def ag(g): 
    for a11 in range(0,2):
        for a12 in range(0,2):
            for a13 in range(0,2):
                for a21 in range(0,2):
                    for a22 in range(0,2):
                        for a23 in range(0,2):
                            for a31 in range(0,2):
                                for a32 in range(0,2):
                                    for a33 in range(0,2):
                                        a = [[a11,a12,a13], 
                                             [a21,a22,a23],
                                             [a31,a32,a33]]
                                        multiplyMatrix(len(a), len(a[0]), a, len(g), len(g[0]), g)
                                        print("")


G = [[0,0,1,0,1], 
     [1,1,1,1,0],
     [0,1,0,1,0]]
ag(G)
