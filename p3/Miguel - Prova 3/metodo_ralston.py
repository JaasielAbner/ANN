def ralston(f,x0,y0,h,n):
    r = []
    for _ in range(n):
        m1 = f(x0,y0)
        m2 = f(x0 + ((3/4) * h), y0 + ((3/4)*h) * m1)
        y1 = y0 + h *(m1 + 2 * m2) / 3
        x0 += h
        y0 = y1
        r.append((x0,y0))
    return r

#Q10 Prova:
def f(x,y):
    return y*(2-x)+x+1

x0, y0 = 0.44227, 1.49503
e = ralston(f,x0,y0, h=0.1083,n=10)
for xi, yi in e:
    print(xi, yi)