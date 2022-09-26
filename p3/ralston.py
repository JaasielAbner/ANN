import math
import matplotlib.pyplot as plt
import numpy as np

# exemplo y'= 1 +xy, y(1) = 2

def ralston(f, x0, y0, h, n):
    r = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + (3/4) * h, y0 + (3/4) * h * m1)
        y1 = y0 + h * (m1 + 2 * m2) / 3

        x0 += h
        y0 = y1
        r.append( (x0, y0) )
    return r

if __name__ == '__main__':

    def f(x, y):
        return y*(2-x) + x + 1

    x0 = 1.23866
    y0 = 1.4417
    h  = 0.14901
    n  = 10
    r = ralston(f, x0, y0, h, n)
    print(r)

    # x, y = zip(*resposta)
    # print(x)
    # print(y)
    # plt.scatter(x,y)
    # plt.savefig('euler_half.png')
