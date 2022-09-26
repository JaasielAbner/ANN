import numpy as np
import math

def prod(xs):
    p = 1
    for i in xs:
        p *= i
    return p

def finite_diffs(xs, ordem, x0, f):
    A = []
    B = []
    n = len(xs)

    for i in range(n):
        A.append([0] * n)
        for j in range(n):
            A[i][j] = xs[j] ** i
        potencias = [k+1 for k in range(i - ordem, i)]
        fatorial = 0 if i < ordem else prod(potencias)
        termo = fatorial * x0 ** (i - ordem)
        B.append(termo)

    A = np.array(A, dtype='float')
    B = np.array(B, dtype='float')
    cs = np.linalg.solve(A, B)

    soma = 0
    for c, x in zip(cs, xs):
        soma += c * f(x)
    
    return soma


def f(x):
    return math.exp(math.cos(x)**2)+math.exp(-2*x**2)+math.log(x)

ordem = 2
x0 = 6.1669406
x = [5.1669406, 5.4169406, 5.6669406, 5.9169406, 6.1669406, 6.4169406, 6.6669406, 6.9169406]
print(finite_diffs(x, ordem, x0, f))
