import numpy as np

def best_parabola(x,y):
    n = len(x)
    xises = 0
    #MATRIZ A
    xises = 0
    xises_quadrado = 0
    xises_cubo = 0
    xises_quarta = 0
    xises_quinta = 0
    xises_sexta = 0
    xises_setima = 0
    xises_oitava = 0
    xises_nona = 0
    xises_decima = 0
    #MATRIZ B
    yis = 0
    xises_yis = 0
    xises2_yis = 0
    xises3_yis = 0
    xises4_yis = 0
    xises5_yis = 0
    for i in range(n):
        #MatrizA
        xises += x[i]
        xises_quadrado += x[i]**2
        xises_cubo +=x[i]**3
        xises_quarta +=x[i]**4
        xises_quinta +=x[i]**5
        xises_sexta +=x[i]**6
        xises_setima +=x[i]**7
        xises_oitava +=x[i]**8
        xises_nona +=x[i]**9
        xises_decima +=x[i]**10

        #MatrizB
        yis += y[i]
        xises_yis +=x[i] * y[i]
        xises2_yis += y[i] * (x[i]**2)
        xises3_yis += y[i] * (x[i]**3)
        xises4_yis += y[i] * (x[i]**4)
        xises5_yis += y[i] * (x[i]**5)



    A = [[n,xises,xises_quadrado,xises_cubo,xises_quarta,xises_quinta],[xises,xises_quadrado,xises_cubo,xises_quarta,xises_quinta,xises_sexta],
        [xises_quadrado,xises_cubo,xises_quarta,xises_quinta,xises_sexta,xises_setima],[xises_cubo,xises_quarta,xises_quinta,xises_sexta,xises_setima,xises_oitava],
        [xises_quarta,xises_quinta,xises_sexta,xises_setima,xises_oitava,xises_nona],[xises_quinta,xises_sexta,xises_setima,xises_oitava,xises_nona,xises_decima]]
    B = [yis,xises_yis,xises2_yis,xises3_yis,xises4_yis,xises5_yis]
    a,b,c,d,e,f = np.linalg.solve(A,B)
    return a,b,c,d,e,f

x = [-4.2073, -4.1438, -3.99, -3.9237, -3.8783, -3.802, -3.7168, -3.5424, -3.5366, -3.4167, -3.3577, -3.2666, -3.1675, -3.0143, -2.9784, -2.834, -2.7744, -2.6579, -2.609, -2.5433, -2.4378, -2.3401, -2.3007, -2.1443, -2.0594, -1.96, -1.9028, -1.8402, -1.7486, -1.6764, -1.5866, -1.4637, -1.3997, -1.3053, -1.2244, -1.0836, -1.0026, -0.9054, -0.8168, -0.7781, -0.6303, -0.5519, -0.4688, -0.3933, -0.2809, -0.2188, -0.1336, -0.0496, 0.0718, 0.165, 0.2244, 0.3264, 0.4031, 0.4607, 0.5547, 0.6453, 0.7104, 0.8822, 0.9549, 1.01, 1.1115, 1.2023, 1.3054, 1.4058, 1.4667, 1.5925, 1.6136, 1.754, 1.7848, 1.9275, 1.9797, 2.0846, 2.1786, 2.2903, 2.3075, 2.4738, 2.5073, 2.6422, 2.6764, 2.7474, 2.8743, 2.9921, 3.0728, 3.1146, 3.2224, 3.3558, 3.3991, 3.5028, 3.6253, 3.718, 3.7333, 3.8817, 3.9682, 4.0025, 4.1304, 4.1754]
y = [3.2679, 3.5197, 5.0897, 5.6372, 5.8811, 6.1863, 6.2722, 6.9459, 6.7681, 7.0071, 6.6422, 7.5766, 7.1058, 7.3482, 6.8864, 6.2391, 6.4362, 5.237, 5.7046, 5.9151, 5.9807, 5.8636, 6.1783, 5.6023, 4.8132, 4.7922, 4.9896, 5.0165, 4.8483, 4.9081, 5.3167, 3.162, 4.2468, 4.5109, 4.1492, 4.4761, 4.3892, 4.0764, 4.5514, 4.5388, 2.5916, 4.3767, 4.5664, 4.6521, 4.4864, 4.5768, 5.0553, 5.0732, 5.0039, 5.2369, 4.371, 5.1341, 5.6382, 5.2673, 5.6509, 4.952, 5.6239, 5.7407, 5.7066, 5.8484, 5.8122, 7.3717, 5.578, 5.4346, 5.2947, 4.1968, 5.2422, 4.4231, 5.2791, 4.9692, 4.7306, 4.8509, 4.791, 3.8081, 4.6296, 4.3517, 3.823, 3.6192, 3.5676, 3.6855, 3.4422, 3.2174, 3.1079, 3.1049, 3.1313, 3.3652, 3.2883, 3.2817, 3.9638, 3.5851, 4.1172, 4.5711, 5.7772, 5.1027, 6.8434, 6.3478]

r = best_parabola(x,y)
print(r)
