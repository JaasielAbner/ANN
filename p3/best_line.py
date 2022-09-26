import random
import matplotlib.pyplot as plt
import numpy as np


# vamos gerar uma lista de pontos no plano
def model(x):

    a, b = -1, 1
    erro = a + (b - a) * random.random()
    return 2 + 0.5 * x + erro

p, q = 0, 10
# x = [ p+i*(q-p)/(n-1) for i in range(n) ]
# y = [ model(xi) for xi in x ]

n = 50  # número de pontos do eixo x
x = [0.0882, 0.319, 0.4971, 0.6611, 0.9899, 1.1233, 1.2787, 1.5283, 1.6587, 1.9591, 2.1595, 2.2826, 2.4357, 2.7116, 2.8848, 3.1977, 3.3079, 3.5469, 3.7733, 3.8218, 4.0287, 4.3522, 4.4681, 4.7207, 4.854, 5.0903, 5.2733, 5.4291, 5.76, 5.9356, 6.108, 6.2003, 6.4845, 6.7301, 6.9845, 7.0124, 7.2941, 7.5617, 7.7048, 7.8949, 8.1959, 8.2731, 8.4055, 8.6167, 8.8515, 9.1468, 9.2139, 9.422, 9.7002, 9.9832]
y = [2.3918, 2.0614, 2.0014, 1.9074, 0.8968, 0.8855, 0.6385, -0.4408, 0.3817, 0.1145, -0.4003, -0.4128, -0.626, -1.0177, -1.3607, -1.9801, -1.8412, -2.1646, -2.4716, -2.9065, -3.1789, -3.2913, -3.7357, -3.7489, -4.0556, -4.1311, -4.5885, -4.7112, -5.4773, -5.6506, -7.636, -5.6237, -6.3284, -6.609, -7.032, -7.0625, -7.1001, -7.8231, -7.7139, -9.1281, -8.4861, -8.8225, -9.8034, -8.25, -9.5981, -9.8553, -9.6461, -10.3204, -10.6886, -10.7997]
print(x)
print(y)

def best_line(x: list[float], y: list[float]) -> list[float]:
    n = len(x)
    sum_x   = sum(x)
    sum_x2  = sum(xi**2 for xi in x)
    sum_y   = sum(y)
    sum_xy  = sum(xi * yi for xi, yi in zip(x, y))
    A = [[n, sum_x], [sum_x, sum_x2]]
    B = [sum_y, sum_xy]
    a0, a1 = np.linalg.solve(A, B)
    return a0, a1

a0, a1 = best_line(x, y)

def reta(x):
    return a0 + a1 * x

def erro():
    e = sum( (yk - reta(xk)) ** 2 for xk, yk in zip(x, y) )
    return e

print('Resultado\/\n')
print(f'a0 = {a0}, a1 = {a1} -> reta = {a0}{a1:+}x')
print('erro ->', erro())

t = np.linspace(p, q, 200)
rt = reta(t)
plt.scatter(x, y)
plt.plot(t, rt)
plt.savefig('best_line.png')
