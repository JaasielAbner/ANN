#include <stdio.h>
#include <math.h>
#include "func.h"


void false_position(double (*f)(double),double a,double b,int n){
    double fa = f(a);
    double fb = f(b);
    if(fa * fb >= 0){
        printf("O Teorema de Bolzano não sabe dizer se existe raiz para f no intervalo [%.16f, %.16f]",a,b);
        return;
    }else {
        double x;
        for(int i =0;i<n;i++){
            x = (a *fb - b * fa) / (fb - fa);
            printf("x_%d = %.16f\n", i+1,x);
            double fx = f(x);
            if(fx == 0){
                printf("Encontramos uma raiz para f, ela é x = %.16f",x);
                return;
            }
            if(fa * fx < 0){
                b = x;
                fb = fx;
            }else{
                a = x;
                fa = fx;
            }
        }
    }
}

int main(){
    double f(double x){
        //double e = exp(x); 
        //return 1-((pow(130.65,2))/(9.81*(pow(8.09*x,3)+((pow(0.5*x,2))*(pow(0.5*x,2))*(pow(0.5*x,2))))))*(8.09+x);
        //return 1-((pow(130.65,2))/(9.81*pow((8.09*x+((pow(x,2))/2)),3)))*8.09+x;
        return (120747975+1)/(1+120747975*pow(M_E,-1.41*0.0000000001*(120747975+1)*x))-30186993.75;
    }
    //intervalo iniial
    double a = 0;
    double b = 4.87;

    int n = 11; // número de iterações

    false_position(box_lid_size,a,b,n);
}
