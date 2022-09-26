import random
import numpy as np
import math


def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p


def finite_diffs(xs, ordem, x0, f):
    A = []
    B = []
    n = len(xs)
    for i in range(n):
        A.append([0]*n)
        for j in range(n):
            A[i][j] = xs[j] ** i
        potencias = [k + 1 for k in range(i - ordem, i)]
        fatorial = 0 if i < ordem else prod(potencias)
        termo = fatorial * x0 ** (i - ordem)
        B.append(termo)
    A = np.array(A, dtype='float')
    B = np.array(B, dtype='float')
    cs = np.linalg.solve(A, B)
    soma = 0
    for ck, xk in zip(cs, xs):
        soma += ck * f(xk)
    return soma


def f(x):
    return x**2 * math.cos(x - 1) * math.exp(-3 * x ** 2)


x0 = 0.8455
order = 5
x = [0.6189, 0.6461, 0.7158, 0.7785, 0.8273, 0.8579, 0.9437, 0.9556, 1.0229, 1.0477]
values = [0.7904, 0.8192, 0.848, 0.952, 0.9933]

q = 0
n = len(values)
for i in range(n):

    q = f(x0)
    for j in range(1, order+1):
        q += ((finite_diffs(x, j, x0, f) / math.factorial(j))
              * ((values[i] - x0)**j))

    fx_q = math.sqrt(((f(values[i]) - q)**2))
    print(f'{values[i]} = {q} | {fx_q}')
