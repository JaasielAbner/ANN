import math
import matplotlib.pyplot as plt
import numpy as np

# exemplo y'= 1 +xy, y(1) = 2

def rk4(f, x0, y0, h, n):
    r = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h / 2) * m1)
        m3 = f(x0 + h / 2, y0 + (h / 2) * m2)
        m4 = f(x0 + h, y0 + h * m3)
        yk = y0 + h * (m1 + 2 * m2 + 2 * m3 + m4) / 6

        x0 += h
        y0 = yk
        r.append( (x0, y0) )
    return r

if __name__ == '__main__':

    def f(x, y):
        return ra*l * (1-y)

    x0 = 0.00174
    y0 = 1.287
    h  = 0.14
    n  = 150
    ra = 0.19919
    r = rk4(f, x0, y0, h, n)
    print(r)

    # x, y = zip(*resposta)
    # print(x)
    # print(y)
    # plt.scatter(x,y)
    # plt.savefig('euler_half.png')
