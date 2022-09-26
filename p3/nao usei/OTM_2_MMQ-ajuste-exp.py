
import math
import random
import matplotlib.pyplot as plt
import numpy as np


def modelo(x):
    return 2 * math.exp(0.3 * x) + 0.01 * random.random()

a, b = 0, 10
# x = a + (b - a) * np.random.rand(500)
# x.sort()
# y = [ modelo(xi) for xi in x]

n = 5
x = [0.0475, 0.0774, 0.1538, 0.2138, 0.2704, 0.3074, 0.3691, 0.4322, 0.4781, 0.5446, 0.5484, 0.6495, 0.689, 0.7552, 0.802, 0.8407, 0.8841, 0.9575, 1.0149, 1.0444, 1.1311, 1.1702, 1.2493, 1.2694, 1.3305, 1.3742, 1.4687, 1.4836, 1.5694, 1.6292, 1.6583, 1.7117, 1.7503, 1.8032, 1.8664, 1.9263, 1.9691, 2.0529, 2.0866, 2.1365, 2.2306, 2.2634, 2.3113, 2.3773, 2.4415, 2.4743, 2.5634, 2.6029, 2.6433, 2.6947, 2.7757, 2.8091, 2.8588, 2.9201, 2.9989]
y = [2.3691, 2.4637, 2.7381, 2.9119, 2.6205, 3.028, 2.8809, 2.3645, 2.8884, 3.0193, 3.0977, 3.1568, 3.3282, 3.1781, 3.4028, 4.3096, 3.7296, 3.5805, 3.903, 3.5208, 3.8243, 4.0746, 3.8482, 4.1709, 3.9187, 4.1855, 4.1616, 5.1331, 4.3459, 4.6363, 4.8306, 4.769, 5.0246, 5.0486, 5.0923, 4.9617, 5.3938, 5.5702, 5.752, 5.7017, 5.574, 6.5594, 5.7675, 6.2853, 6.5222, 6.7855, 6.5293, 5.9512, 6.1629, 6.1026, 6.947, 7.1432, 6.3696, 7.7164, 7.8672]

def best_exp(x, y):

    sum_x = sum(x)
    sum_x2 = sum(xi**2 for xi in x)

    A = [ [len(x), sum_x], [sum_x, sum_x2]]
    y_ = [math.log(yi) for yi in y]
    sum_xy = sum(xi * yi for xi, yi in zip(x, y_))
    B = [sum(y_), sum_xy]
    a0, a1 = np.linalg.solve(A, B)
    a, b = math.exp(a0), a1
    return a, b

a, b = best_exp(x, y)
print(a, b)

def bexp(x):
    return a * math.exp(b * x)

t = np.linspace(min(x), max(x), 100)
bexpt = [bexp(i) for i in t]
plt.plot(t, bexpt, zorder = 10, color='orange', linewidth = 2)
plt.scatter(x, y, zorder = 1)
plt.savefig('ponto_exp.png')
