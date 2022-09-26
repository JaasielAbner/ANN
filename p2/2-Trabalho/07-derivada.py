import numpy as np
import math

# x0 = ponto onde a função será derivada
# x = lista de coordenadas na proximidade de x0
# y = cálculo da função em todos os pontos x
# k = ordem da derivada


def coeffs_dif_fin(x0, x, k):
    n = len(x)
    A, B = [[1] * n], [0]
    for i in range(1, n):
        # construção da matriz A
        row_i = [xi ** i for xi in x]
        A.append(row_i)
        # construção da matriz B
        if i < k:
            B.append(0)
        elif i == k:
            B.append(math.factorial(k))
        else:
            numer = math.factorial(i)
            denom = math.factorial(i - k)
            el = (numer / denom) * x0 ** (i - k)
            B.append(el)
    return np.linalg.solve(A, B)


def dif_fin(coeffs, y):
    return sum(ci * yi for ci, yi in zip(coeffs, y))


if __name__ == '__main__':
    # exemplo 1:
    def f(x):
        return math.exp(math.cos(x)**2) + math.exp(-x**2) + math.log(x)

    x0 = 1.8724
    x = [1.6242, 1.7439, 1.7896, 1.8437, 1.9131, 1.9688, 2.0318, 2.0607]

    # x0 = 2
    k = 4
    n = 10  # numero de pontos igualmente espaçados
    # queremos pontos no intervalo [x0-e, x0+e]
    # ao diminuir o epsilon (e) os pontos são cada vez mais próximos
    e = 0.1
    # x = np.linspace(x0 - e, x0 + e, n)
    y = [f(xi) for xi in x]

    coeffs = coeffs_dif_fin(x0, x, k)
    aprox = dif_fin(coeffs, y)
    print(f'{coeffs = }')
    print(f'{aprox = }')
