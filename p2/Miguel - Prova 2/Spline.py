import matplotlib.pyplot as plt
import numpy as np
import math

def spline(x,y):
    # retorna todos os coeficientes de todos os polinomios
    # ie todos os ak,bk,ck,dk
    n = len(x)
    a = {k: v for k, v in enumerate(y)}
    h = {k: x[k+1]-x[k] for k in range(n-1)}

    A = [[1] + [0] * (n-1)]

    for i in range(1,n-1):
        zeros = [0] * n
        zeros[i-1] = h[i-1]
        zeros[i]   = 2*(h[i-1] + h[i])
        zeros[i+1] = h[i]
        A.append(zeros)
        
    A.append([0] * (n-1) + [1])

    B = [0]
    for k in range(1, n-1):
        row = 3 * (a[k+1] - a[k]) / h[k] - 3 * (a[k] - a[k-1]) / h[k-1]
        B.append(row)
        
    B.append(0)
    
    C = dict(zip(range(n), np.linalg.solve(A, B)))
    
    b = {}
    d = {}
    for k in range(n-1):
        b[k] = (1/h[k]) * (a[k+1] - a[k]) - (h[k]/3) * (2*C[k]+C[k+1])
        d[k] = (C[k+1] - C[k]) / (3 * h[k])
    
    s = {}
    for k in range(n-1):
        eq = f'{a[k]}{b[k]:+}*(x{-x[k]:+}){C[k]:+}*(x{-x[k]:+})**2{d[k]:+}*(x{-x[k]:+})**3'
        s[k] = {'eq':eq, 'domain':[x[k], x[k+1]]}

    for k,v in s.items():
        print(f'S{k}', v)

    return s

x = [0.546, 1.326, 2.199, 3.033, 3.687, 4.6, 5.645, 6.677]
y = [4.597, 3.415, 2.42, 2.006, 2.145, 2.888, 3.803, 3.923]
valores = [1.826, 4.23, 4.619]
eqs = spline(x,y)

for key,value in eqs.items():
    def p(x):
        return eval(value['eq'])
    for v in valores:
        if v >= value['domain'][0] and v <= value['domain'][1]:
            print(v, end=' ')
            print(p(v))

# x = [-2,-1.5,-0.8,1,2,4,5,5.4,6.1,6.5]
# y = [-1,2,3,1,4,2,3,2.3,3.2,3.7]

# eqs = spline(x,y)

# for key,value in eqs.items():
#     def p(x):
#         return eval(value['eq'])
#     t = np.linspace(*value['domain'], 100)
#     plt.plot(t,p(t), label=f"$S_{key}(x)$")

# plt.scatter(x,y)
# plt.legend()
# plt.savefig('spline.png')