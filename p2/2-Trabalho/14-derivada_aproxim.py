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
    approximations = [6.649229394274858, 6.898304178773781, 6.929288092976677, 6.9191375663494625, 6.907440080149172, 6.899914582338738]

    new_value = richardson(approximations.copy())
    aprox = richardson(approximations + [new_value])
    print(aprox)
