import math
import matplotlib.pyplot as plt
import numpy as np

# exemplo y'= 1 +xy, y(1) = 2

def ralston(f, x0, y0, h, n, x_values):
    r = []
    for _ in range(n):
        h = x_values[_] - x0
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

    x0 = 0.425
    y0 = 1.774
    x_values = [0.62, 0.837, 1.02, 1.43, 1.688, 1.843, 2.109, 2.3, 2.547, 2.858]
    h = any(x_values) - x0
    n  = 10
    r = ralston(f, x0, y0, h, n, x_values)
    print(r)

    # x, y = zip(*resposta)
    # print(x)
    # print(y)
    # plt.scatter(x,y)
    # plt.savefig('euler_half.png')
