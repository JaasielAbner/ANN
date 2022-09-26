#include <stdio.h>
#include <math.h>

#include "func.h"

void bisection(double(*f)(double),double a,double b,int n){
    if (f(a)*f(b)>=0) {
        printf("o medoto de bolzano nao sabe dizer se existe uma raiz no intervalo {%.16f,%.16f}",a,b);
        return;
    }
    else{
        for(int k=0;k<n;k++){
            double m = 0.5*(a+b);
            printf("x_%d = %.16f\n", k+1,m);
            if(f(m)==0){
                printf("voce encontrou uma raiz pra f: z= %.16f",m);
            }
            if(f(a)*f(m)<0){
                b=m;
            }
            else{
                a=m;
            }
    }
    }

}

double f(double x){
    double e = exp(x); 
    return e - 2 * pow(x,2) + x - 1.5 ; // funcao
}

int main(void){
    double a = 0.1; // incio do intervalo de analise
    double b = 1.96; // fim do intervalo de analise
    int n = 12; // quantidade de interacoes
    
    //bisection(f,a,b,n);

    bisection(populational_growth, a, b, n);

    return 0;
}
