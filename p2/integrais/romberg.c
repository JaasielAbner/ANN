#include <stdio.h>
#include <math.h>

#define ORDEM_ERRO 8
#define numElemsFirstCol 4

double trapz(double(*f)(double), double a, double b, int n){
    double soma = 0;
    double h = (double)(b-a) / (double)n;
    for (int i = 1; i < n; i++){
        soma += f(a + i * h);
    }
    soma *= 2;
    soma += f(a);
    soma += f(b);
    soma *= (0.5 * h);
    return soma;
}

void romberg(double coluna_F1[]){
    for (int i = 0; i < numElemsFirstCol - 1; i++){
        for (int j = 0; j < numElemsFirstCol - 1; j++){
            double numer = pow(2, (i + 1) * 2) * coluna_F1[j + 1] - coluna_F1[j];
            double denom = pow(2, (i + 1) * 2) - 1;
            coluna_F1[j] = numer / denom;
        }
    }
    printf("Aprox 0(h^%d) - %.16f", ORDEM_ERRO, coluna_F1[0]);
}

double f(double x){
    return exp(-x*x);
}


int main()
{
    double a = 0;
    double b = 1;
    double h = 0.5;
    int n = (int)((b -a) / h);
    printf("n = %.16f", (double)n);

    double coluna_F1[] = {};

    for (int i = 0; i < numElemsFirstCol; i++){
        coluna_F1[i] = trapz(f, a, b, pow(2, i) * n);
    }

    romberg(coluna_F1);
}
