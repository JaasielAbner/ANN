import math

pontos = (-0.14887433898163122, 0.14887433898163122)
pesos = (0.29552422471475287, 0.29552422471475287)
pontosEpesos = zip(pontos,pesos) # sempre dada

def quadratura(f, pontos_e_pesos):
    # serve apenas p/ funções no intervalo [-1, 1]
    soma = 0
    for x_k, c_k in pontos_e_pesos:
        soma += c_k * f(x_k)
    return soma

def change(f, a, b, u): # transforma uma integral definida num intervalo a,b numa definida no intervalo -1,1
    return f((b+a)/2 + ((b-a)*u)/2)*(b-a)/2

def coeficientes_funcao(f, a, b, fs):
    if a != -1 or b != 1:
        raise ValueError('a deve ser -1 e b deve ser 1')

    n = len(fs)
    coeficientes = []
    for k in range(n):
        # ck = integral de f*fk em [a,b] / integral de fk² em [a,b]
        def ffk(x):  return f(x) * fs[k](x)
        def fkfk(x): return fs[k](x)**2
        ck = quadratura(ffk, pontosEpesos) / quadratura(fkfk, pontosEpesos)
        coeficientes.append(ck)

    return coeficientes

def f1(x): return 1
def f2(x): return x
def f3(x): return (3* x ** 2 - 1)/2

def f(x):
    if x >= 0:
        return 1
    return 2

fs = [f1,f2,f3]
coeficientes = coeficientes_funcao(f, -1, 1, fs)
print(coeficientes)

def g(x):
    soma = 0
    for k, ck in enumerate(coeficientes):
        soma += ck * fs[k]
    return soma