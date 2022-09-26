#include <stdio.h>
#include <math.h>

void false_position(double (*f)(double), double a, double b, int n, double tol){
    if (f(a) * f(b) < 0)
    {

        for (int i = 0; i < n; i++)
        {
            double fa = f(a);
            double fb = f(b);
            double c;
            c = (a * fb - b * fa) / (fb - fa);
            if (f(c) == 0)
            {
                printf("Voce encontrou uma raiz para f. Ela é: %.16f\n", c);
                return;
            }

            printf("x_%d = %.15f \n", i + 1, c);
            if (fa * f(c) < 0)
            {
                b = c;
            }
            else
            {
                a = c;
            }
        }
    }
    else
    {
        printf("O intervalo [ %.16f, %.16f] nao serve\n", a, b);
    }
}

double f(double t){
        double e = 2.71828182846; // euler
        double n = 103481111;
        double lambda = 1.41*1 / pow(10,10);
        double x = (n * 25)/ 100;
        return ( (n+1) / (1 + n * (1/exp(lambda*(n+1)*t ))) ) - x;
}

int main(){

    double a = 0;
    double b = 2530;
    int max_iter = 7;
    double tol = 0.00001;

    false_position(f, a, b, max_iter, tol);
}