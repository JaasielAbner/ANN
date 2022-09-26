import math
import numpy as np

def richardson(col_1):
    n = len(col_1) - 1
    for i in range(n - 1):
        for j in range(n - 1 - i):
            numer = 2 ** (i + 1) * col_1[j + 1] - col_1[j]
            denom = 2 ** (i + 1) - 1
            value = numer / denom
            col_1[j] = value
    return col_1[0]

if __name__ == '__main__':
    approximations = [-6.581137114696718, -6.889528429506235, -6.881861580963175, -6.839566224662931, -6.809254769034709, -6.791874805587611]

    new_value = richardson(approximations.copy())
    aprox = richardson(approximations + [new_value])
    print(aprox)
