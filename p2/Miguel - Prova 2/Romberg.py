import math

def romberg(col1):
    n = len(col1)
    col1 = [item for item in col1]

    for j in range(n - 1):     # percorrer as colunas
        temp_col = [0] * (n - 1 - j)
        for i in range(n - 1 - j): # percorrer as linhas
            power = j + 1
            temp_col[i] = ((4 ** power) * col1[i + 1] - col1[i]) / (4 ** power - 1)
        col1[:n - 1 - j] = temp_col
        print(f'F_{j+2}',temp_col)
    return col1[0]

def trapz(f, a, b, h):
    n = int((b - a)/h)
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += f(a) + f(b)
    soma *= h/2
    return soma

def f(x):
    return math.exp(-x**2)

a,b = [0,1]
# h = 0.5
# k = 5
# hs = [h / 2 ** i for i in range(k)]
# col1 = [trapz(f, a, b, hi) for hi in hs]
# print('F_1',col1)
col1 = [3.0310524239033874, 3.6293572422069156, 3.6716466952512974, 3.676838347983398, 3.678026112481302]
r = romberg(col1)
print(r)