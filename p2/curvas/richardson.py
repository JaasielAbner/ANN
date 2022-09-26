import math


def richardson(col1):
    col1 = [item for item in col1]
    n = len(col1)
    for j in range(n - 1):
        temp_col = [0] * (n-1-j)
        for i in range(n - 1 - j):
            power = j + 1
            temp_col[i] = (2 ** power * col1[i+1] - col1[i]) / (2 ** power - 1)
        col1[:n - 1 - j] = temp_col
        print(temp_col)
    return col1[0]


def func(x):
    return pow(x, pow(x, -x))


if __name__ == '__main__':

    err_order = 7
    h = 0.39012
    x0 = 1.32472
    orders = [4, 5, 6, 7, 8]

    def F1(f, x0, h):
        return (func(x0 + h) - func(x0)) / h

    col_F1 = [F1(func, x0, h/2**i) for i in range(err_order)]

    aprox = richardson(col_F1)

    print(f'{aprox = }')