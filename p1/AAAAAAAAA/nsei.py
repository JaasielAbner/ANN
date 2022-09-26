import math

############################
# esse aqui são coisas que eu encontrei perdidas que são refrentes a prova
# a primeira é sobre infectados, a segunda é sobre empuxo
# (eu acho????)


lambida = 1.41 * 10**(-10)
n = 152224869
infectados = n*(1/4)

f = f'({n}+1)/(1+{n}*pow(M_E,-{lambida}*({n}+1)*x)) - {infectados}'

# f = f'({n}+1)/(1+{n}*(math.e**(-{lambida}*({n}+1)*x))) - {infectados}'

print(f)

########## # # # #############

k1 = 42000
k2 = 71
m = 92
g = 9.81
h= 0.55

ex = f' (2*{k2}*pow(x,(5/2.0)))/(5.0)+(1/2.0)*{k1}*x*x - {m}*{g}*x -{m}*{g}*{h}'

# ex = f' (2*{k2}*(x**(5/2.0)))/(5.0)+(1/2.0)*{k1}*x*x - {m}*{g}*x -{m}*{g}*{h}'

print(ex)