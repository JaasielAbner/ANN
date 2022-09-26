import numpy as np

def best_poly(x, y, grau = 1):
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
    return a * np.exp(b * x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':

    x = [0.0002, 0.2662, 0.3985, 0.5738, 0.7829, 0.9648, 1.0205, 1.2178, 1.4909, 1.6213, 1.7607, 1.8625]
    y = [2.1083, 8.0737, 8.0362, 12.0345, 16.1407, 24.9392, 22.5032, 32.3087, 50.3369, 60.3648, 76.9175, 91.3091]
    y_ = np.log(y)

    grau = 1

    a0, a1 = best_poly(x, y_, grau)

    print(f'{a0 = } e {a1 = }')

    a = np.exp(a0)
    b = a1

    print(f'{a = } e {b = }')

    p = build_func(a, b)
    
    x_values = [0.1435, 1.1136, 1.1948]
    
    for xi_v in x_values:
        print(p(xi_v))
