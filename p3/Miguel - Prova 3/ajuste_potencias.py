import math
import numpy as np

def ajuste_potencia(x,y):
    n = len(x)

    logX     = [math.log(xi) for xi in x]
    logY     = [math.log(yi) for yi in y]
    somaX    = sum(logX)
    somaX2   = sum(xi ** 2 for xi in logX)
    somalogY = sum(logY)
    prodXY   = sum(xi * yi for xi, yi in zip(logX,logY))

    A = [[n, somaX],[somaX, somaX2]]
    B = [somalogY, prodXY]
    a0, a1 = np.linalg.solve(A,B)
    a, b = math.exp(a0), a1

    return a,b

# Q3:
x = [0.3324, 0.4039, 0.775, 1.117, 1.4345, 1.8739, 2.299, 2.3912, 2.7956, 3.2827, 3.5023, 3.6831, 4.3062, 4.3541, 4.952, 5.2645, 5.461, 5.781, 6.161, 6.5345, 6.7923, 7.0454, 7.5262, 7.7913, 8.2757, 8.5763, 8.846, 9.1713, 9.6539, 9.9284]
y = [5.1671, 5.1072, 4.3025, 5.0361, 4.7376, 3.8347, 3.7747, 3.5251, 3.6908, 3.4891, 2.6483, 4.0594, 3.2972, 3.9815, 3.5355, 1.881, 3.6431, 3.543, 3.6152, 4.0162, 3.6042, 4.167, 4.588, 4.1211, 3.922, 3.0092, 4.6776, 5.2811, 5.7963, 6.1178]

a,b = ajuste_potencia(x,y)
print(a,b)
