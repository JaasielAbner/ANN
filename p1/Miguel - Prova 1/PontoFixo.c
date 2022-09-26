#include<stdio.h>

double ponto_fixo(double (*f)(double), double chuteInicial, int iteracoes){
    double novoChute;
    for(int i = 0; i < iteracoes; i++){
        novoChute = f(chuteInicial);

        printf("x_%d = %.16lf\t", i+1, novoChute);
        printf("f(x_%d) = %.16lf\n", i+1, f(novoChute));
        chuteInicial = novoChute;
    }
}

void main (){
    double f(double x){
        return (x*x - 1) / 3;
    }

    double x0 = 0.56;

    double g(double x){
        return x / 2 + 1 / x;
    }

    double y0 = 1.78;

    ponto_fixo(g, y0, 25);
}