import math

def quadratura(f, pontos_e_pesos):
    soma = 0
    for x_k, c_k in pontos_e_pesos:
        soma += c_k * f(x_k)
    return soma

def change(f, a, b, u): # transforma uma integral definida num intervalo a,b numa definida no intervalo -1,1
    return f((b+a)/2 + ((b-a)*u)/2)*(b-a)/2

def f(x):
    return math.exp(x)*math.sin(x)/(1+x**2)

a, b = [0.689, 2.652]

def g(u):
    return change(f, a, b, u)

pontos = (-0.1252334085114689, 0.1252334085114689, -0.3678314989981802, 0.3678314989981802, -0.5873179542866175, 0.5873179542866175, -0.7699026741943047, 0.7699026741943047, -0.9041172563704749, 0.9041172563704749, -0.9815606342467192, 0.9815606342467192)
pesos = (0.24914704581340277, 0.24914704581340277, 0.2334925365383548, 0.2334925365383548, 0.20316742672306592, 0.20316742672306592, 0.16007832854334622, 0.16007832854334622, 0.10693932599531843, 0.10693932599531843, 0.04717533638651183, 0.04717533638651183)

print('g(x): ', quadratura(g, zip(pontos,pesos)))
print('f(x): ', quadratura(f, zip(pontos,pesos)))

# se o intervalo nao for -1, 1, usar a primeira