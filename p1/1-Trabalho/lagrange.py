def lagrange(x,y):
    #retorna yi dividido pelo denominador do polinomio Li
    num=len(x)
    coefs = []
    for i in range(num):
        prod=1
        for j in range(num):
            if i!=j:
                prod*=(x[i] - x[j])
        ci=y[i]/prod
        coefs.append(ci)
    return coefs

def pl(t: float,x: list[float], coefs: list[float]) -> float:
    soma=0
    num = len(coefs)
    for i in range(num):
        prod=1
        for j in range(num):
            if i!=j:
                prod*=(t-x[j])
        prod*= coefs[i]
        soma+=prod
    return soma


def poly(x, coefs):
    def f(t):
        return pl(t,x, coefs)
    return f


if __name__ == '__main__':
    x=[0.498,0.748,1.068,1.652, 1.845, 2.391, 2.791]
    y=[0.5533073859836118241,0.853248578254926,0.991406120155034,0.6647694638801,0.589148423189379, 0.5527490210250,0.6324626531321351]
    
    # x=[-0.691, 0.247, 0.681]
    # y=[0.07729752396, 0.39600431644 ,0.07940273264]
    
    # x=[1,3]
    # y=[1,-1]
    c = lagrange(x,y)
    print(c)
    lagr=poly(x, c)
    # print(lagrange(x, y))
    print(lagr(0))

    import matplotlib.pyplot as plt
    import numpy as np

    plt.scatter(x,y)
    t=np.linspace(min(x), max(x), 100)
    lt=[lagr(ti) for ti in t]
    plt.plot(t, lt)
    plt.savefig('lagrange.png')
    
