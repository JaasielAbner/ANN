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

# Q9:
# x = [-4.159, -3.8489, -3.2724, -3.0377, -2.8281, -2.4959, -2.0775, -1.6553, -1.6335, -1.2061, -0.7912, -0.5579, -0.1677, 0.0358, 0.4831, 0.713, 1.1342, 1.4529, 1.9354, 2.1009, 2.496, 2.9034, 3.1899, 3.5422, 3.6281, 4.0375]
# y = [2.5022, 6.2774, 7.7442, 8.5563, 7.5277, 6.6229, 5.3381, 4.3841, 4.0516, 3.6482, 4.031, 4.208, 4.0618, 4.9134, 5.2685, 5.5337, 6.1944, 6.391, 5.2962, 4.692, 3.7245, 2.6878, 2.1545, 2.5798, 2.7525, 3.4038]
#Q10:
# x = [-4.0778, -3.7372, -3.6917, -3.3056, -2.9918, -2.6856, -2.4014, -2.3341, -2.1102, -1.6768, -1.4055, -1.1087, -1.0417, -0.55, -0.2729, -0.0236, 0.0677, 0.3294, 0.5985, 1.05, 1.2249, 1.4176, 1.703, 2.0137, 2.2176, 2.5053, 2.7523, 3.1031, 3.383, 3.4594, 3.8348, 4.0779]
# y = [4.2469, 7.0529, 6.4116, 6.8863, 6.8405, 6.1193, 6.2176, 5.5819, 5.0128, 4.7209, 4.539, 4.8364, 3.336, 4.4804, 4.9443, 5.6172, 5.0211, 3.7381, 5.3373, 5.9369, 6.5602, 5.6465, 5.5183, 4.7193, 4.8056, 4.1321, 3.6803, 3.4783, 3.441, 3.0951, 4.0189, 5.5903]

# Q2 Prova:
x = [-4.0974, -3.8655, -3.5859, -3.3592, -3.0112, -2.8117, -2.4663, -2.1942, -1.8931, -1.8495, -1.3918, -1.1502, -0.9619, -0.636, -0.4358, -0.1803, 0.2651, 0.4225, 0.7431, 0.9772, 1.1057, 1.3649, 1.702, 1.8844, 2.14, 2.528, 2.7477, 3.0828, 3.2805, 3.599, 3.8615, 4.0977]
y = [4.7493, 4.8281, 5.8776, 6.4298, 5.9261, 5.9678, 5.5698, 4.61, 4.4764, 4.3553, 4.6828, 4.5108, 4.6375, 4.8176, 4.7241, 4.7326, 4.4547, 5.0844, 5.2241, 5.2182, 5.3001, 5.1963, 5.3326, 5.1736, 5.0302, 4.4728, 3.8879, 3.9623, 3.9203, 4.8398, 4.0581, 6.8565]


r = best_parabola(x,y)
print(r)