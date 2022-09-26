#include <stdio.h>
#include <math.h>

#define ordemEerro 8
// 4 pois a primeira coluna deve ter 'error_order / 2' elementos
#define numElemsFirstCol 4

double trapz(double (*f)(double), double a, double b, int n){
    double soma = 0;
    double h = (double)(b - a) / (double)n;
    for(int i = 1; i < n; i++){
        soma += f(a + i * h);
    }
    soma *= 2;
    soma += f(a);
    soma += f(b);
    soma *= (0.5 * h);
    return soma;
}


void romberg(double array[]){
    for(int i = 0; i < numElemsFirstCol - 1; i++){
        for(int j = 0; j < numElemsFirstCol - 1; j++){
            double numer = pow(2, (i + 1) * 2) * array[j + 1] - array[j];
            double denom = pow(2, (i + 1) * 2) - 1;
            array[j] = numer / denom;
        }
    }
    printf("Aprox O(h^%d) = %.16f\n", ordemEerro, array[0]);
}


double f(double x){
    return -x*(x-21)*(x+1);
}

int main(){

    //exemplo
    //aprox a integral de exp(-x*x), de 0 a 1


    double a = 0;
    double b = 12;
    double h = 12;
    int n = 10;


    printf("%.16f\n", (double)n);

    double coluna_F1[numElemsFirstCol] = {};
    for(int i = 0; i < numElemsFirstCol; i++){
        coluna_F1[i] = trapz(f, a, b, pow(2, i) * n);
        printf("n = %d e trapz = %.16f\n", (int)(pow(2, i) * n), coluna_F1[i]);
    }
    romberg(coluna_F1);

}