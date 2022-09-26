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
    x = [0.0337, 0.0629, 0.1345, 0.2039, 0.2686, 0.3202, 0.3719, 0.4, 0.4652, 0.5421, 0.5667, 0.6296, 0.6856, 0.7511, 0.8292, 0.8732, 0.9353, 0.9639, 1.0384, 1.0983, 1.1389, 1.2219, 1.2351, 1.2845, 1.3654, 1.4183, 1.4452, 1.5549, 1.6008, 1.6468, 1.6963, 1.7488, 1.8157, 1.874, 1.9075, 1.9506]
    y = [4.1436, 5.5527, 4.8346, 4.8819, 7.3923, 4.9921, 7.6311, 6.0986, 6.8852, 7.759, 7.6247, 8.9873, 9.3642, 9.1618, 10.7255, 12.0542, 12.6848, 13.2367, 17.4725, 14.1757, 15.9303, 16.5795, 18.103, 16.944, 20.8833, 23.099, 24.3142, 24.6994, 27.2817, 31.2491, 32.1001, 35.4563, 38.5143, 40.724, 41.4794, 47.5809]
    y_ = np.log(y)
 
    grau = 1

    a0, a1 =  best_poly(x, y_, grau)

    print(f'{a0 = } e {a1 = }')

    a = np.exp(a0)
    b = a1/np.log(2)

    print(f'{a = } e {b = }')

    p = build_func(a, b)

    x_values =  [0.4147, 0.8501, 1.5436, 1.7388, 1.7819]

    
    for xi_v in x_values:
        print(p(xi_v))
