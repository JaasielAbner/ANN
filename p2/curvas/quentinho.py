import numpy as np

def best_poly(x, y, grau = 2):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i + j
            if (p == 0):
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)

def poly(x, a, b):
    return a * 2 ** (b * x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [0.6553, 0.7157, 0.9677, 1.2246, 1.3563, 1.6922, 1.8713, 2.1114, 2.2801, 2.4031, 2.5918, 2.9451]
    y = [0.8323, 0.1131, 1.3164, 3.7026, 4.3807, 9.6732, 14.3237, 20.821, 26.5062, 32.5631, 40.4272, 64.4698]
    y_ = np.log(y)
    
    grau = 1

    a0, a1 =  best_poly(x, y_, grau)

    print(f'{a0 = } e {a1 = }')

    a = np.exp(a0)
    b = a1/np.log(2)

    print(f'{a = } e {b = }')

    p = build_func(a, b)

    x_values =  [0.8374, 1.2691, 2.3882]

    
    for xi_v in x_values:
        print(p(xi_v))