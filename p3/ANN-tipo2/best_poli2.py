import numpy as np

def best_par(x,y):
    n = len(x)
    xises = 0
    #MATRIZ A
    xises = 0
    xises_quadrado = 0
    xises_cubo = 0
    xises_quarta = 0
    #MATRIZ B
    yis = 0
    xises_yis = 0
    xises2_yis = 0
    for i in range(n):
        xises += x[i]
        xises_quadrado += x[i]**2
        xises_cubo +=x[i]**3
        xises_quarta +=x[i]**4

        yis += y[i]
        xises_yis +=x[i] * y[i]
        xises2_yis += y[i] * (x[i]**2)

    A = [[n,xises,xises_quadrado],[xises,xises_quadrado,xises_cubo],[xises_quadrado,xises_cubo,xises_quarta]]
    B = [yis,xises_yis,xises2_yis]
    a,b,c = np.linalg.solve(A,B)
    return a,b,c

x = [0.6553, 0.7157, 0.9677, 1.2246, 1.3563, 1.6922, 1.8713, 2.1114, 2.2801, 2.4031, 2.5918, 2.9451]
y = [0.8323, 0.1131, 1.3164, 3.7026, 4.3807, 9.6732, 14.3237, 20.821, 26.5062, 32.5631, 40.4272, 64.4698]

r = best_par(x,y)
print(r)
