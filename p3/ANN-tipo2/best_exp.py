import math
import random
import numpy as np
from typing import List

#x = a + (b-a) * np.random.rand(10)
#x.sort()
x = [0.6553, 0.7157, 0.9677, 1.2246, 1.3563, 1.6922, 1.8713, 2.1114, 2.2801, 2.4031, 2.5918, 2.9451]
y = [0.8323, 0.1131, 1.3164, 3.7026, 4.3807, 9.6732, 14.3237, 20.821, 26.5062, 32.5631, 40.4272, 64.4698]

def best_exp(x: List[float],y: List[float]):
    sum_x = sum(x)
    sum_x2 = sum(xi**2 for xi in x)
    A = [[len(x),sum_x],[sum_x,sum_x2]]
    y_ = [math.log(yi) for yi in y]
    sum_xy = sum(xi * yi for xi,yi in zip(x,y_))
    B = [sum(y_),sum_xy]
    a0,a1 = np.linalg.solve(A,B)
    a,b = math.exp(a0),a1
    return a,b

r = best_exp(x,y)
print(r)
