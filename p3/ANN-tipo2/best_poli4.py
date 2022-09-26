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
    #MATRIZ B
    yis = 0
    xises_yis = 0
    xises2_yis = 0
    xises3_yis = 0
    xises4_yis = 0
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
        #MatrizB
        yis += y[i]
        xises_yis +=x[i] * y[i]
        xises2_yis += y[i] * (x[i]**2)
        xises3_yis += y[i] * (x[i]**3)
        xises4_yis += y[i] * (x[i]**4)



    A = [[n,xises,xises_quadrado,xises_cubo,xises_quarta],[xises,xises_quadrado,xises_cubo,xises_quarta,xises_quinta],
        [xises_quadrado,xises_cubo,xises_quarta,xises_quinta,xises_sexta],[xises_cubo,xises_quarta,xises_quinta,xises_sexta,xises_setima],
        [xises_quarta,xises_quinta,xises_sexta,xises_setima,xises_oitava]]
    B = [yis,xises_yis,xises2_yis,xises3_yis,xises4_yis]
    a,b,c,d,e = np.linalg.solve(A,B)
    return a,b,c,d,e

x = [-4.4947, -4.3515, -4.242, -4.1726, -4.0321, -3.9821, -3.8343, -3.7369, -3.704, -3.5645, -3.5029, -3.3482, -3.3277, -3.1742, -3.0948, -3.0209, -2.9272, -2.7676, -2.7, -2.5896, -2.5338, -2.4271, -2.3551, -2.218, -2.1582, -2.0101, -1.8959, -1.8059, -1.7463, -1.6588, -1.5912, -1.4382, -1.3289, -1.2166, -1.113, -1.0602, -0.9908, -0.8204, -0.8119, -0.6531, -0.598, -0.4486, -0.359, -0.2987, -0.1999, -0.0436, -0.0017, 0.1509, 0.2473, 0.3017, 0.426, 0.4662, 0.5743, 0.6735, 0.7695, 0.8744, 1.0252, 1.0561, 1.1567, 1.2867, 1.3697, 1.4354, 1.5738, 1.6895, 1.7654, 1.8557, 1.9251, 2.0425, 2.1142, 2.2834, 2.2859, 2.4675, 2.5613, 2.6725, 2.6939, 2.8463, 2.8769, 3.0226, 3.0947, 3.2193, 3.2741, 3.3891, 3.5019, 3.5551, 3.6884, 3.7578, 3.9062, 3.9697, 4.0735, 4.1592, 4.2678, 4.3411, 4.5001, 4.5505, 4.6886, 4.7709, 4.8225, 4.9382]
y = [1.3822, 2.6272, 3.6019, 3.8525, 6.5802, 4.9186, 6.4614, 6.2813, 6.287, 6.5509, 6.8165, 7.5833, 7.0859, 7.3749, 8.2507, 7.6982, 7.3918, 7.1693, 7.4427, 8.2679, 7.2097, 7.1854, 7.0172, 7.8601, 6.8379, 6.5916, 6.3835, 6.4582, 6.2598, 6.33, 6.2291, 4.506, 5.3162, 4.5396, 4.738, 4.9465, 4.8256, 4.6769, 4.9899, 4.4179, 4.4424, 4.1383, 4.1522, 4.2378, 5.1973, 4.3169, 4.7789, 4.377, 4.4434, 4.0339, 4.2829, 4.203, 4.3282, 4.7407, 4.4086, 5.0458, 5.1194, 4.896, 5.1029, 5.4109, 5.789, 6.1872, 6.1041, 6.2823, 5.6591, 6.9597, 8.4052, 6.5657, 7.7066, 8.2349, 8.1627, 8.1505, 7.7451, 9.1548, 8.1047, 8.3423, 9.3919, 8.9052, 10.1144, 9.9381, 9.8866, 10.1652, 10.2141, 10.3119, 10.1251, 10.4119, 10.3091, 10.0884, 9.6022, 9.223, 9.3744, 8.7663, 8.1929, 8.1875, 7.4535, 6.6309, 8.1271, 5.6447]

r = best_parabola(x,y)
print(r)
