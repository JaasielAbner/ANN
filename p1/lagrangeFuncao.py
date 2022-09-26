import numpy as np

def lagrange(x, y):
    for i in range(len(x)):
        a = 1
        for j in range(len(x)):
            if i != j:
                a *= (x[i]-x[j])
        print(y[i]/a)


if __name__ == '__main__':
    # x = [-1.823, -0.45, 0.724, 1.497, 2.787, 3.853, 5.34, 6.035]  # coordenadas x do ponto
    # y = [0.564, 0.967, 0.941, 0.732, -0.161, -0.891, -0.611, 0.007]  # coordenadas y do ponto

    x = []
    y = []
    z = [0.472, 0.66, 1.246, 1.562, 2.031, 2.52, 2.696]

    def f(x):
        return np.cos(np.sin(np.log(x**2)))

    for i in z:
        x.append(i)
        y.append(f(i))

    lagrange(x, y)