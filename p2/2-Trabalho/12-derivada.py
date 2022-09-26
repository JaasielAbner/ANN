import math


def richardson(col_1):
    n = len(col_1) - 1
    for i in range(n - 1):
        for j in range(n - 1 - i):
            numer = 2 ** (i+1) * col_1[j + 1] - col_1[j]
            denom = 2 ** (i+1) - 1
            value = numer/denom
            col_1[j] = value
    return col_1[0]


if __name__ == '__main__':

    def func(x):
        return (x**2) * (math.tan(math.sin(x / math.pi)))

    h = 0.44049
    x0 = -0.15452
    orders = [2, 3, 4, 5, 6]
    cols = []

    def F1(h):
        return (func(x0 + h) - func(x0)) / h

    for order in orders:
        cols.append(F1(h / 2**order))
        aprox = richardson(cols)
        print(f'order({order}) = {aprox}')

    print('=================')

    for i, order in enumerate(orders):
        # print(i, order)
        cols = [F1(h/2**i) for i in range(2, 3)]
        aprox = richardson(cols)
        
        print(f'{aprox}')

    print('=================')

    cols = [F1(h/2**i) for i in range(2, 7)]
    aprox = richardson(cols)
    print(f'{aprox}')

    print('cols=', cols)
