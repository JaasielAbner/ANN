#include <stdio.h>
#define ROWS 3
#define COLS 3

void seidel(double coeficientes[ROWS][COLS], double independentes[ROWS], double chute[COLS], int iteracoes){
    double aproximacao;
    for(int it = 0; it < iteracoes; it++){
        // isolando a n-ésima variável da n-ésima equação
        for(int i = 0; i < ROWS; i++){
            aproximacao = independentes[i];
            for(int j = 0; j < COLS; j++){
                if(i != j){ // isolando a variável na diagonal
                    aproximacao -= coeficientes[i][j]*chute[j];
                }
            }
            aproximacao /= coeficientes[i][i];
            chute[i] = aproximacao;
        }
        printf("X^(%d) -> ", it+1);
        for(int k = 0; k < COLS; k++){
            printf("%.16lf ", chute[k]);
        }
        printf("\n");
    }
}

void main(){
    double coeficientes[ROWS][COLS] = {{-2.29558, 0.64784, -0.52745},{1.48798, 5.50587, -2.8976},{4.41924, -3.67, -9.20953}}; // matriz de coeficientes do sistema
    double independentes[ROWS] = {-4.20427, 0.09913, -4.86948}; // matriz de termos independentes do sistema
    double chute[COLS] = {0.10376, 1.88603, 3.84214}; // chute inicial

    seidel(coeficientes, independentes, chute, 18);
}