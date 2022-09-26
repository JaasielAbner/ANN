'''
Em um circuito com tensão aplicada E e com resistência R, indutância L e capacitância C em paralelo, a corrente i satisfaz a equação diferencial
didt=Cd2Edt2+1RdEdt+1LE.
Suponha que C=0.384farads, R=1.4601ohm, L=1.7764henrie e que a tensão seja dada por
E(t)=e−0.0602πtsin(2t−π).
Se i(t0)=i0, com t0=0 e i0=0, use o método de Ralston para encontrar estimativas para a corrente i nos pontos tk=t0+kh, onde k=1,2,…,150 e h=0.0715.

'''


import numpy as np
import matplotlib.pyplot as plt


def euler(f, x0, y0, h, n):
    vals = []
    for k in range(n):
        y0 += h*f(x0, y0)
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 1
def euler_mid(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h/2) * m1)
        y0 += h*m2
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 1/2
def heun(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h*m1)
        y0 += h*(m1+m2)/2
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 2/3
# def ralston(f, x0, y0, h, n):
#     vals = []
#     for _ in range(n):
#         m1 = f(x0, y0)
#         m2 = f(x0 + 0.75*h, y0 + 0.75*h*m1)
#         y0 = h*(m1 + 2*m2)/3
#         x0 += h
#         vals.append([x0, y0])
#     return vals


# padrao = euler_mid
def rk2(f, x0, y0, h, n, b=1.0):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
    vals = []
    a = 1-b
    p = 1/(2*b)
    q = p
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + p*h, y0 + q*h*m1)
        y0 += (a*m1 + b*m2)*h
        x0 += h
        vals.append([x0, y0])
    return vals


def rk2_h_variavel(f, x0, y0, n, b, x_values):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
    b = 0.5
    vals = []
    a = 1-b
    p = 1/(2*b)
    q = p
    for i in range(n):
        if i == 0:
            h = x_values[0] - x0
        else:
            h = x_values[i] - x_values[i-1]
        m1 = f(x0, y0)
        m2 = f(x0 + p*h, y0 + q*h*m1)
        y0 += (a*m1 + b*m2)*h
        x0 += h
        vals.append([x0, y0])
    return vals


def diff(a, b):
    return sum((ai - bi)**2 for ai, bi in zip(a, b))


def f(x, y):
    return -y/np.sqrt(9**2-y**2)


def g(t, i):
    c = 0.2531
    r = 1.1295
    l = 1.6337

    # considerando a função e(t) = e^(-e_value*pi*t)*sin(2*t-pi)
    # se e^(-0.0619*pi*t) => e_value = 0.0619
    e_value = 0.0796

    def e(t):
        return np.exp(-e_value*np.pi*t)*np.sin(2*t-np.pi)

    def e_(t):
        return np.exp(-e_value*np.pi*t)*(2*np.cos(np.pi-2*t)+e_value*np.pi*np.sin(np.pi-2*t))

    def e__(t):
        return np.exp(-e_value*np.pi*t)*((4-pow(e_value, 2)*pow(np.pi, 2))*np.sin(np.pi-2*t)-4*e_value*np.pi*np.cos(np.pi-2*t))

    return c*e__(t) + (1/r)*e_(t) + (1/l)*e(t)


if __name__ == '__main__':

    x0, y0 = 0,0
    h = 0.0915
    n = 150
    b = 0.5
    x_values = [0.0772, 0.1238, 0.2798, 0.3361, 0.481, 0.5338, 0.6701, 0.7884, 0.827, 0.9586, 1.0526, 1.1252, 1.2594, 1.3546, 1.4652, 1.5715, 1.6817, 1.7894, 1.8404, 1.9666, 2.0327, 2.1312, 2.2581, 2.3791, 2.4752, 2.5663, 2.6604, 2.7742, 2.8514, 2.9572, 3.0277, 3.1873, 3.2437, 3.3868, 3.4384, 3.5357, 3.6239, 3.7116, 3.8106, 3.9224, 4.0299, 4.1382, 4.2324, 4.3886, 4.4532, 4.535, 4.6421, 4.7313, 4.8627, 4.9362, 5.0777, 5.1787, 5.2259, 5.3463, 5.4301, 5.517, 5.6689, 5.7276, 5.8137, 5.9543, 6.0191, 6.128, 6.2796, 6.3698, 6.4549, 6.5486, 6.6222, 6.7683, 6.8576, 6.9334, 7.0839, 7.1483, 7.2121, 7.3884, 7.4539, 7.5871, 7.6459, 7.7433, 7.8894, 7.9656, 8.0345, 8.1302, 8.2346, 8.337, 8.4128, 8.5258, 8.6101, 8.725, 8.8568, 8.9685, 9.0641, 9.1268, 9.2303, 9.3257, 9.4327, 9.5331, 9.6179, 9.7615, 9.876, 9.9562, 10.0593, 10.1885, 10.2811, 10.3643, 10.4455, 10.5572, 10.6198, 10.7852, 10.8288, 10.9106, 11.0749, 11.1666, 11.2309, 11.3722, 11.4498, 11.5463, 11.6763, 11.7532, 11.8154, 11.9286, 12.039, 12.1237, 12.2729, 12.3319, 12.4543, 12.5829, 12.6306, 12.7338, 12.8693, 12.9688, 13.0676, 13.1362, 13.2454, 13.3653, 13.4605, 13.5555, 13.6159, 13.7136, 13.8246, 13.9777, 14.0476, 14.177, 14.2632, 14.3856, 14.418, 14.5605, 14.6491, 14.7378, 14.8666, 14.9818]    # metodo1 = euler(f, x0, y0, h, n)
    # metodo2 = euler_mid(f, x0, y0, h, n)
    #metodo3 = heun(f, x0, y0, h, n, x_values)
    # metodo4 = ralston(f, x0, y0, h, n)
    #metodo5 = rk2(g, x0, y0, h, n, b)
    metodo5 = rk2_h_variavel(g, x0, y0, n, b, x_values)

    indice = [i for i in range(n)]
    lista_x, lista_y = zip(*metodo5)

    for i, xi, yi in zip(indice, lista_x, lista_y):
        #print(f'x{i} = {xi} => y{i} = {yi}')
        print(f'{yi},', end='')

    plt.scatter(lista_x, lista_y)

    plt.savefig('edo.png')
