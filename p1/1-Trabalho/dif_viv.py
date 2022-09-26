
def dif_div(x: list[float], y:list[float]) -> list[float]:
    num=len(x)
    Y=[yi for yi in y]
    coefs = [y[0]]
    for j in range(num-1):
        for i in range(num-1-j):
            numer=Y[i+1] - Y[i]
            denom=x[i+1+j] - x[i]
            div=numer/denom
            Y[i]=div
        coefs.append(Y[0])
    return coefs


def poly(t, x, coefs):
    val=0
    num=len(coefs)
    for i in range(num):
        prod=1
        for j in range(i):
            prod*=(t-x[j])
        val+= coefs[i]*prod
    return val


def build_func(x, coefs):
    def temp(t):
        return poly(t,x,coefs)
    return temp

if __name__ == '__main__':
    x=[-2.176]
    y=[1.46321012223974]

    coefs = dif_div(x,y)
    p=build_func(x, coefs)
    print(coefs)

   # print(p(1), p(2), p(3), p(4))
