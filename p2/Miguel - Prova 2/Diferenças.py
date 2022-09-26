import matplotlib.pyplot as plt
import numpy as np
import math

def diferencas(x,y):
    Y = [x for x in y] # copiando y em Y para não alterar a lista original
    n = len(y)
    coeficientes = [y[0]] + [0] *(n-1)
    for i in range(n-1): # colunas
        for j in range(n-1-i): # linhas
            numerador   = Y[j+1] - Y[j]
            denominador = x[j+1+i] - x[j]
            Y[j] = numerador / denominador
        coeficientes[i+1] = Y[0]
    return coeficientes

def equacao(x, coeficientes): # constroi a equação do polinomio interpolador
    n = len(x)
    polinomio = ''
    for i in range(n):
        sign = '*' if i!= 0 else ''
        polinomio += f'{coeficientes[i]:+}{sign}'+'*'.join([f'(x{-xj:+})' for j,xj in enumerate(x) if j < i])

    return polinomio

def f(x):
    return x**5 - 4*x**2 + 2*math.sqrt(x+1)+math.cos(x)

x = [-0.292, -0.138, 0.277, 0.489, 0.813, 0.974, 1.357]
y = [f(xi) for xi in x]

coeficientes = diferencas(x,y)
# polinomio = equacao(x,coeficientes)
for x in coeficientes:
    print(x)
# coeficientes = diferencas(x,y)
# polinomio = equacao(x,coeficientes)
# print(coeficientes)
# print(polinomio)

# t = np.linspace(min(x), max(x), 100)

# def p(x):
#     return eval(polinomio)

# plt.plot(t, p(t))
# plt.scatter(x,y, zorder=10)
# plt.savefig("diferenças.png")