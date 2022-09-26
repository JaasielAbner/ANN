import numpy as np
import matplotlib.pylab as plt

def spline(x, y):
    n = len(x)
    a = {k: v for k, v in enumerate(y)}
    h = {k: x[k + 1] - x[k] for k in range(n - 1)}

    A = [[1] + [0] * (n - 1)]
    for i in range(1, n - 1):
        row = [0] * n
        row[i - 1] = h[i - 1]
        row[i] = 2 * (h[i - 1] + h[i])
        row[i + 1] = h[i]
        A.append(row)
    A.append([0] * (n - 1) + [1])

    B = [0]
    for k in range(1, n - 1):
        row = 3 * (a[k + 1] - a[k]) / h[k] - 3 * (a[k] - a[k - 1]) / h[k - 1]
        B.append(row)
    B.append(0)

    c = dict(zip(range(n), np.linalg.solve(A, B)))

    b = {}
    d = {}
    for k in range(n - 1):
        b[k] = (1 / h[k]) * (a[k + 1] - a[k]) - (h[k] / 3) * (2 * c[k] + c[k + 1])
        d[k] = (c[k + 1] - c[k]) / (3 * h[k])

    s = {}
    for k in range(n - 1):
        print(f'Equation {k}:')
        print(f'a[{k}] = {a[k]}')
        print(f'b[{k}] = {b[k]}')
        print(f'c[{k}] = {c[k]}')
        print(f'd[{k}] = {d[k]}')
        eq = f'{a[k]}{b[k]:+}*(x{-x[k]:+}){c[k]:+}*(x{-x[k]:+})**2{d[k]:+}*(x{-x[k]:+})**3'
        s[k] = {'eq': eq, 'domain': [x[k], x[k + 1]]}

    return s


x = []
y = []
z = [(0.355,5.179), (0.713,5.484), (1.552,4.976), (2.358,5.298), (3.058,4.443), (3.203,4.368), (4.22,3.492), (4.526,2.511)]

for xi, yi in z:
    x.append(xi)
    y.append(yi)

eqs = spline(x, y)

for eq in eqs.values():
    print(eq)


def s(x):
    for key, value in eqs.items():
        if value['domain'][0] <= x <= value['domain'][1]:
            return eval(value['eq'])


print(s(1.792))
print(s(3.774))
print(s(4.494))



for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f'$S_{key}(x)$')

plt.scatter(x, y)
plt.legend()
plt.savefig('spline.png')