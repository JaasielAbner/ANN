def euler(f, x0, y0, h, n):
    r = []
    for i in range(n):
        m1 = f(x0,y0)
        m2 = f(x0 + (h/2), y0 + (h/2) * m1)
        yk = y0 + h * m2
        y0 = yk
        x0 += h
        r.append((x0, y0))
    return r

#Q8 Prova:
# def f(x,y):
#     return y*(2-x)+x+1

def f(x, y):
    return k*y + v

h=0.0625
n = int(1/h)
k = 0.0851
v = 56369

x0, y0 = 0, 1252359 

# x0 = 1.23883
# y0 = 2.39759
e = euler(f, x0, y0, h, n)
for xi, yi in e:
    print(xi, yi)