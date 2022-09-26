
import math
import random
import matplotlib.pyplot as plt
import numpy as np

def modelo(x):
    return 2 * x ** 2.43 + 1.3 * random.random()

x0, x1 = 0, 10
n = 100
x = x0 + (x1 - x0) * np.random.rand(n)
x.sort()
y = [ modelo(xi) for xi in x]

def best_pow(x, y):
    new_x = [math.log(xi) for xi in x]
    new_y = [math.log(yi) for yi in y]

    sum_x = sum(new_x)
    sum_x2 = sum(xi ** 2 for xi in new_x)

    A = [ [len(x), sum_x], [sum_x, sum_x2] ]
    sum_new_y = sum(new_y)
    sum_new_xy = sum(xi * yi for xi, yi in zip(new_x, new_y))
    B = [sum_new_y, sum_new_xy]

    a0,a1 = np.linalg.solve(A, B)
    a, b = math.exp(a0), a1
    return a, b

a, b = best_pow(x, y)
print(a, b)

def bpow(x):
    return a * x ** b

t = np.linspace(x0, x1, 100)
bpowt = [ bpow(i) for i in t]
plt.plot(t, bpowt, color='orange', linewidth=3, zorder=10)
plt.scatter(x, y, zorder=1)
plt.savefig('best_pow.png')
# if __name__ == '__main__':

#     pass
