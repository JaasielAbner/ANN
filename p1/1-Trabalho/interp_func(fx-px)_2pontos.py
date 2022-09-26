import numpy as np


def f(x):
    return 1/(1+25*pow(x,2)) #funcao


def poly(x, y):
    n = len(x) - 1
    A = []
    for xi in x:
        row = [1]
        for j in range(1, n + 1):
            row.append(xi**j)
        A.append(row)
    return np.linalg.solve(A, y)


def p(x, coefs):
    first = coefs[0]
    return first + sum([ai*x**j for j, ai in enumerate(coefs[1:], 1)])


if __name__ == '__main__':
    x = [-0.857, 0.216, 0.895]
    #x = [-0.805 , -0.802]
    y = []

    for i in x:
        y.append(f(i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, y)
    print(coefs)
    print(abs(f(-0.289) - p(-0.289, coefs))) #ponto 1
    print(abs(f(0.084) - p(0.084, coefs))) #ponto 2
