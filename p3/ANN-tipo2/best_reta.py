import math
import numpy as np

def best_reta(x,y):
    n = len(x)
    xises = 0
    yis = 0
    xises_quadrado = 0
    xises_yis = 0
    for i in range(n):
        xises += x[i]
        yis += y[i]
        xises_quadrado += x[i]**2
        xises_yis +=x[i] * y[i]
    A = [[n,xises],[xises,xises_quadrado]]
    B = [yis,xises_yis]
    a,b = np.linalg.solve(A,B)
    return a,b

x = [0.0973, 0.2857, 0.4476, 0.7312, 0.8972, 1.1545, 1.3012, 1.4623, 1.6166, 1.8705, 2.0022, 2.3985, 2.5694, 2.6514, 2.8114, 3.0468, 3.2469, 3.4474, 3.7171, 3.8517, 4.187, 4.3353, 4.5032, 4.6974, 4.9011, 5.058, 5.2947, 5.443, 5.7017, 5.9698, 6.0957, 6.3904, 6.493, 6.7829, 6.8447, 7.0249, 7.231, 7.5454, 7.7374, 7.8338, 8.1776, 8.3658, 8.5065, 8.6798, 8.8591, 9.1394, 9.3531, 9.4198, 9.6083, 9.8973]
y = [0.6656, 0.1847, 0.4143, -0.0323, -0.2435, -0.6617, -0.7569, -1.3152, -1.3322, -1.5274, -1.6667, -2.0092, -2.4103, -2.6944, -2.5433, -2.9835, -4.1213, -3.2574, -3.7003, -4.6747, -4.1607, -4.4744, -4.8095, -5.0633, -4.8879, -5.4137, -5.5455, -5.9256, -6.037, -6.2629, -6.6631, -5.3852, -7.0078, -7.3825, -7.6365, -6.835, -7.8813, -8.4395, -9.4372, -9.6329, -9.2508, -10.5297, -8.5535, -8.8731, -9.5468, -10.159, -10.5106, -8.9222, -10.6727, -11.0359]

r = best_reta(x,y)
print(r)