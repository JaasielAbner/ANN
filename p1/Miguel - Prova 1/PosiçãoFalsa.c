#include<stdio.h>
// #include<math.h>

void fpos(double (*f)(double), double inferior, double superior, int iteracoes){
    double fa = f(inferior);
    double fb = f(superior);

    if(fa * fb >= 0){
        printf("Impossível determinar se há raiz no intervalo [%lf,%lf]\n", inferior, superior);
        return;
    }

    double pontoMedio;
    double fx;

    for(int i = 0; i < iteracoes; i++){
        pontoMedio = ((inferior * fb) - (superior * fa)) / (fb - fa);
        fx = f(pontoMedio);
        
        printf("x_%d = %.16lf\n", i+1, pontoMedio);

        if(fx == 0){
            printf("A raiz é: x = %.16lf\n", pontoMedio);
            return;
        }

        if(fa * fx < 0){
            superior = pontoMedio;
            fb = fx;
        }else{
            inferior = pontoMedio;
            fa = fx;
        }
        
    }
}

void main(){

    double f(double x){
        return 2 * (x + 1) * (x - 0.5) * (x - 1);
    }

    double inferior1 = 0.6373;
    double superior1 = 1.4608;
    int iteracoes1 = 5;

    fpos(f, inferior1, superior1, iteracoes1);

}