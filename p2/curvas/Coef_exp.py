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
    return a * 2 ** (b * x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [0.0424, 0.0871, 0.1246, 0.1808, 0.232, 0.3289, 0.3574, 0.4353, 0.4515, 0.5087, 0.5621, 0.6306, 0.7152, 0.7629, 0.8329, 0.8449, 0.9221, 0.9836, 1.0263, 1.0819, 1.1257, 1.1963, 1.2267, 1.3057, 1.3701, 1.404, 1.4954, 1.5383, 1.5884, 1.6154, 1.7123, 1.7603, 1.7962, 1.8417, 1.9421, 1.9894]
    y = [4.6213, 5.3712, 5.1022, 6.2105, 8.2946, 7.4742, 6.5595, 7.7767, 8.9832, 8.9925, 9.6492, 12.0801, 9.1451, 12.2032, 13.0815, 13.7245, 14.3237, 14.5612, 16.9913, 18.8946, 19.6462, 20.5339, 22.6135, 23.5968, 27.1833, 28.0036, 31.29, 32.043, 34.0712, 35.3686, 40.1991, 43.5968, 41.9984, 47.9516, 53.6748, 59.0406]
    y_ = np.log(y)
 
    grau = 1

    a0, a1 =  best_poly(x, y_, grau)

    print(f'{a0 } e {a1}')

    a = np.exp(a0)
    b = a1/np.log(2)

    print(f'{a} e {b}')

    p = build_func(a, b)

    x_values =  [0.3715, 0.6443, 0.6519, 0.7439, 1.6755]

    
    for xi_v in x_values:
        print(p(xi_v))