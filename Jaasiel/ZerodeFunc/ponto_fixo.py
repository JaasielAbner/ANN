# seja g:[a,b]->R
# 0. g tem que ser contínua
# 1. g(x)\in [a,b] para todo x\in[a,b] é o mesmo que g([a, b])\subset[a,b]
# 2. |g'(x)| < 1 para todo x\in[a,b]
# f(x) = 0 <--> g(x) = x

import math


def g(x):
    func = ((3 * pow(x, 4) + 2 * pow(x, 2) + 3) / (4 * pow(x, 3) + 4 * x - 1))   
    return func

n = 10
a, b = [1, 2]

x0 = 1.39396
iterations = [1, 2, 3, 4, 5, 6, 7, 8]

for i in range(1, iterations[-1] + 1):
    xn = g(x0)
    x0 = xn
    if i in iterations:
        print("%.7f"%x0 + ",")
        
