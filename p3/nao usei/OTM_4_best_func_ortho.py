import math
import matplotlib.pyplot as plt
import numpy as np

n2 = [ (0.5773502692, 1.0000000000), (-0.5773502692, 1.0000000000)]
n3 = [ (0.7745966692, 0.5555555556), (0.0000000000, 0.8888888889), (-0.7745966692, 0.5555555556) ]
n4 = [ (0.8611363116, 0.3478548451), (0.3399810436, 0.6521451549), (-0.3399810436, 0.6521451549), (-0.8611363116, 0.3478548451) ]
n5 = [ (0.9061798459, 0.2369268850), (0.5384693101, 0.4786286705), (0.0000000000, 0.5688888889), (-0.5384693101, 0.4786286704), (-0.9061798459, 0.2369268850) ]
# n6 = [ (0.6612093864662645, 0.3607615730481386), (-0.6612093864662645, 0.3607615730481386),
#        (-0.2386191860831969, 0.46791393457269104), (0.2386191860831969, 0.46791393457269104),
#        (-0.932469514203152, 0.17132449237917036), (0.932469514203152, 0.17132449237917036)]

#usar somente se o intervalo for de [-1, 1]
def quadratura(f, ponto_e_peso):
    soma = 0
    for x_k, c_k in ponto_e_peso:
      soma += c_k * f(x_k)
    return soma

#construir combinacao linear f ~ * c1 * f1 + c2 * f2 + ...
def coeffs_best_func(f, a, b, fs):
    coeffs = []
    for k in range(len(fs)):
        # ck = integral de f*fk em [a,b] /  integral fk*fk em [a,b]
        def ffk(x):
            return f(x) * fs[k](x)
        def fkfk(x):
            return fs[k](x) ** 2
        ck = quadratura(ffk, n5) / quadratura(fkfk, n5)
        coeffs.append(ck)
    return coeffs

def f1(x): return 1
def f2(x): return x
def f3(x): return (3 * x ** 2 - 1) / 2

def f(x):
    if x>=0:
        return 1
    return 2

fs = [f1, f2, f3]

a, b = [-1,1]
result = coeffs_best_func(f, a, b, fs)
print(result)

def g(x):
    soma = 0
    for k, ck in enumerate(result):
        soma += ck * fs[k](x)
    return soma

t = np.linspace(a, b, 100)
ft = [f(i) for i in t]
gt = [g(i) for i in t]

plt.plot(t, ft, label='gráfico de f')
plt.plot(t, gt, label='gráfico de g')
plt.legend
plt.savefig('best_func_ortho.png')
