import numpy as np
# import scipy as sp

def best_poly (x, y, k):
    n = len(x)
    if n <= k:
        raise ValueError('O número de pontos deve ser maior que k (o grau do polinônmio)')

    somas = {}
    somas[0] = n
    for n in range(1, 2*k + 1):
        somas[n] = sum(xi ** n for xi in x)
    A = []
    B = []
    for i in range (k + 1):
        row = []
        for j in range(k + 1):
            row.append(somas[i + j])
        A.append(row)
        if i == 0:
            B.append(sum(y))
        else:
            B.append(sum(xi ** i * yi for xi, yi in zip(x,y)))
    return np.linalg.solve(A, B)

x = [0.172, 0.4447, 0.8782, 1.2611, 1.4287, 1.9023, 2.0768, 2.5507, 2.8843, 2.96, 3.3481, 3.6181, 4.0255, 4.3039, 4.7566, 5.0826, 5.4682, 5.5283, 6.0943, 6.305, 6.6194, 6.9382, 7.217, 7.4655, 7.8717, 8.3231, 8.3876, 8.7386, 9.042, 9.6591, 9.8847]
y = [4.9228, 4.7881, 4.4061, 3.4862, 4.1208, 4.5826, 3.6677, 3.6203, 3.5556, 3.669, 3.5534, 3.4717, 3.1603, 3.567, 3.3037, 3.449, 3.2668, 3.4287, 3.6711, 3.436, 3.5307, 3.7188, 3.9502, 4.2304, 4.596, 4.2731, 6.3566, 4.7261, 4.8108, 5.6502, 5.4597]

a0, a1 = best_poly(x, y, 1)

print(f'{a0 = } e {a1 = }')