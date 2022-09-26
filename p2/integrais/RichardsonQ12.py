import math
import numpy as np

def richardson(col_1):
    n = len(col_1)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            numer = 2 ** (i + 1) * col_1[j + 1] - col_1[j]
            denom = 2 ** (i + 1) - 1
            value = numer / denom
            col_1[j] = value
    return col_1[0]

if __name__ == '__main__':
    #exemplo 1
    def func(x):
        return np.cos(x)**3 + 2*np.cos(x)**2 + 1
        """return x**x**-x """
        """ return x**2 * np.tan(np.sin(x/np.pi)) """

    x0 = -0.1676
    h = 0.28258
    err_order = 3

    def F1(h):
        return (func(x0 + h) - func(x0)) / h

    hs = [h, h/2, h/4]
    col_F1 = [F1(h/2**i) for i in range(err_order)]

    approx = richardson(col_F1)

    print(f'Aproximação = {approx}')