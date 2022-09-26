#include <stdio.h>
#include <math.h>
#include "func.h"

void secante(double (*f)(double), double x0, double x1, int n){
    double fx0 = f(x0);
    double fx1 = f(x1);
    if(fx0 == fx1){
        printf("Escolha outras estimativas iniciais");
    } else {
        for(int i =0; i<n;i++){
            double x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0);

            fx0 = f(x1);
            fx1 = f(x2);
            if(fx0 == fx1){
                printf("x_%d = %.16f (preisei parar)",i+2,x2);
                return;
            }else{
                printf("x_%d = %.16f\n",i+1,x2);
                x0 = x1;
                x1 = x2;
            }
        }
    }
}

int main(){
    double f(double x){
        double e = exp(x);
        return 1465338*exp(x) + (380274/x)*(exp(x)-1)-3544635;
    }

    double x0 = 0.69;
    double x1 = 4.73;
    int n = 5;

    secante(box_lid_size, x0, x1, n);
}
