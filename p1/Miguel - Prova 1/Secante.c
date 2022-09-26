#include<stdio.h>
#include<math.h>

void secant(double (*f)(double), double inf, double sup, int iteracoes){
    double x2, fx0, fx1;

    for(int i = 0; i < iteracoes; i++){
        fx0 = f(inf);
        fx1 = f(sup);

        if((fx1 - fx0) == 0){
            printf("Divisão por 0 na iteração %d\n", i+1);
            return;
        }

        x2 = (inf * fx1 - sup * fx0)/ (fx1 - fx0);

        printf("x_%d = %.16lf\n", i+2, x2);

        inf = sup;
        sup = x2;
    }

}

void main(){

    double f(double x){
        return x * x - 7;
    }

    double x0 = 2.3711;
    double x1 = 3.25911;

    secant(f, x0, x1, 5);
    
}