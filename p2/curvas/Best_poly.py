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

x = [0.2831, 0.346, 0.8306, 1.2144, 1.4075, 1.6265, 2.0329, 2.3511, 2.6058, 3.0663, 3.3313, 3.5875, 4.0398, 4.2776, 4.5773, 5.1146, 5.4683, 5.72, 5.8935, 6.2048, 6.6525, 6.803, 7.3495, 7.4632, 7.7635, 8.2741, 8.5341, 8.8439, 9.1641, 9.5393, 9.8424]
y = [5.2236, 5.3295, 4.2165, 4.5307, 4.5557, 4.3459, 3.8454, 4.0468, 3.7137, 3.5423, 3.6365, 3.6328, 4.2515, 3.5408, 4.8843, 3.5213, 4.9448, 3.6983, 3.7496, 3.5377, 3.6143, 3.5784, 3.1663, 3.827, 4.2697, 4.5441, 4.6563, 4.8766, 5.0423, 5.1909, 4.5759]

a0, a1 = best_poly(x, y, 1)

print(f'{a0} e {a1}')