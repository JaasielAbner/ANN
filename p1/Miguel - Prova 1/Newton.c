#include<stdio.h>
#include<math.h>

void newton(double (*func)(double),double (*dfunc)(double), double chuteInicial, int iteracoes){

    for(int i = 0; i < iteracoes; i++){
        double dfx0 = dfunc(chuteInicial);

        if(dfx0 == 0){
            printf("Não é possível executar a iteração %d do método\n", i+1);
            printf("\tf'(%lf) = 0\n", chuteInicial);
            return;
        }

        chuteInicial = chuteInicial - func(chuteInicial) / dfx0;
        printf("x_%d = %.16lf\n", i+1, chuteInicial);
    }
}

void main(){

    double f(double x){
        return x * x - 2;
    }

    double df(double x){
        return 2 * x;
    }

    double x0 = -2.03327;
    newton(f,df,x0,5);
}