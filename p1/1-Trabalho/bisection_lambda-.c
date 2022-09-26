#include <stdio.h>
#include <math.h>
#define PI 3.14159265359

void bisection(double(*f)(double),double a,double b,int n){

    if (f(a)*f(b)>=0) {
        printf("o metodo de bolzano nao sabe dizer se existe uma raiz no intervalo {%.16f,%.16f}",a,b);
        return;

    } else {

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
  //double e = -exp(17.89/x)*8.61; 
    return ((120747975+1)/(1+120747975*(pow(M_E,-1.41*0.0000000001*(120747975+1)*x))))-25/100;
   //return x*(16.65-2*x)*(8.76-2*x)-6.632455372;
}

int main(void){
    double a = 0; // incio do intervalo de analise
    double b = 2187; // fim do intervalo de analise
    int n = 12; // quantidade de interacoes
    
    
    bisection(f,a,b,n);

    return 0;
}
