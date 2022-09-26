import math
import numpy as np

def trapz(f, a, b, n):
    h = (b - a)/n
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += f(a) + f(b)
    soma *= h/2
    return soma

def ajuste_funcao(f, a, b, fs, intervalos=100):
    n = len(fs)

    A = [[0]* n for _ in range(n)]
    B = []
    
    for i in range(n):
        for j in range(n):
            if i >= j: # em baixo da ou na diagonal
                # aij = integral de fj * fi em [a,b]
                def fji(x):
                    return fs[j](x) * fs[i](x)
                aij = trapz(fji, a, b, intervalos)
                A[i][j] = aij
            else: # acima da diagonal
                A[i][j] = A[j][i]

        def ffi(x):
            return f(x) * fs[i](x)
        bi = trapz(ffi, a, b, intervalos)
        B.append(bi)

    coeficientes = np.linalg.solve(A, B)

    return coeficientes

def f(x):
    if x <= 0:
        return 2
    else:
        return 1

def f1(x):
    return 1

def f2(x):
    return math.sin(x)

def f3(x):
    return math.cos(x)

a, b = [-math.pi, math.pi]
fs = [f1, f2, f3] # lista contendo as funções acima
coeficientes = ajuste_funcao(f, a, b, fs)
for xi in coeficientes:
    print(xi)
    
def g(x):
    soma = 0
    for ck, fk in zip(coeficientes, fs):
        soma += ck * fk(x)
    return soma

