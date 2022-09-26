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
    c = 0.3685
    r = 1.4564
    l = 1.9124

    # considerando a função e(t) = e^(-e_value*pi*t)*sin(2*t-pi)
    # se e^(-0.0619*pi*t) => e_value = 0.0619
    e_value = 0.0625

    def e(t):
        return np.exp(-e_value*np.pi*t)*np.sin(2*t-np.pi)

    def e_(t):
        return np.exp(-e_value*np.pi*t)*(2*np.cos(np.pi-2*t)+e_value*np.pi*np.sin(np.pi-2*t))

    def e__(t):
        return np.exp(-e_value*np.pi*t)*((4-pow(e_value, 2)*pow(np.pi, 2))*np.sin(np.pi-2*t)-4*e_value*np.pi*np.cos(np.pi-2*t))

    return c*e__(t) + (1/r)*e_(t) + (1/l)*e(t)


if __name__ == '__main__':

    x0, y0 = 0,0
    h = 0.101
    n = 150
    b = 2/3
    x_values = [0.0119, 0.1754, 0.2308, 0.3535, 0.4767, 0.5694, 0.621, 0.7525, 0.8692, 0.9152, 1.0617, 1.1448, 1.2848, 1.3853, 1.4848, 1.547, 1.6447, 1.739, 1.8595, 1.9671, 2.0233, 2.1479, 2.2786, 2.3408, 2.4652, 2.579, 2.6564, 2.7882, 2.8469, 2.9882, 3.0379, 3.119, 3.2157, 3.3555, 3.4285, 3.5634, 3.6231, 3.7372, 3.8676, 3.9686, 4.0121, 4.1569, 4.226, 4.3808, 4.4592, 4.5858, 4.6596, 4.7646, 4.8576, 4.9871, 5.0798, 5.186, 5.2313, 5.3305, 5.4847, 5.5172, 5.6604, 5.7114, 5.8386, 5.9828, 6.0553, 6.1237, 6.2478, 6.3542, 6.4291, 6.5259, 6.6785, 6.7872, 6.8824, 6.9222, 7.043, 7.1115, 7.2889, 7.3118, 7.4683, 7.5752, 7.6784, 7.7381, 7.8537, 7.9216, 8.0482, 8.1262, 8.2349, 8.3245, 8.4343, 8.5837, 8.6483, 8.7553, 8.8328, 8.971, 9.0145, 9.1164, 9.2437, 9.3108, 9.4542, 9.5399, 9.6294, 9.7803, 9.8754, 9.9684, 10.0862, 10.124, 10.2695, 10.3799, 10.4382, 10.5378, 10.6535, 10.7239, 10.8636, 10.9887, 11.0588, 11.1367, 11.243, 11.3122, 11.4389, 11.519, 11.6806, 11.7899, 11.8487, 11.9862, 12.0768, 12.1104, 12.2647, 12.3483, 12.4509, 12.5702, 12.6823, 12.7467, 12.8569, 12.9393, 13.0641, 13.1348, 13.2596, 13.3894, 13.4104, 13.5312, 13.6498, 13.7383, 13.8885, 13.9245, 14.0746, 14.1167, 14.2464, 14.3127, 14.4841, 14.5201, 14.6288, 14.7431, 14.8197, 14.9437]

    # metodo1 = euler(f, x0, y0, h, n)
    # metodo2 = euler_mid(f, x0, y0, h, n)
    # metodo3 = heun(f, x0, y0, h, n)
    # metodo4 = ralston(f, x0, y0, h, n)
    # metodo5 = rk2(g, x0, y0, h, n, b)
    metodo5 = rk2(g, x0, y0, h, n, b)

    indice = [i for i in range(n)]
    lista_x, lista_y = zip(*metodo5)

    for i, xi, yi in zip(indice, lista_x, lista_y):
        # print(f'x{i} = {xi} => y{i} = {yi}')
        print(f'{yi},', end='')

    plt.scatter(lista_x, lista_y)

    plt.savefig('edo.png')