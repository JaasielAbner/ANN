#include <stdio.h>
#define ROWS 3
#define COLS 3

void jacobi(double coeficientes[ROWS][COLS], double independentes[ROWS], double chute[COLS], int iteracoes){
    double aproximacao;
    double temp[COLS]; 
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
            temp[i] = aproximacao;
        }
        printf("X^(%d) -> ", it+1);
        for(int k = 0; k < COLS; k++){
            chute[k] = temp[k];
            printf("%.16lf ", chute[k]);
        }
        printf("\n");
    }
}

void main(){
    double coeficientes[ROWS][COLS] = {{-1.65443, -0.10593, -0.0393},{2.03917, 7.0493, -3.50093},{-2.92429, 2.222, -6.65549}}; // matriz de coeficientes do sistema
    double independentes[ROWS] = {4.82361, 4.95703, -4.66712}; // matriz de termos independentes do sistema
    double chute[COLS] = {-1.53209, -3.72804, -1.89725}; // chute inicial

    jacobi(coeficientes, independentes, chute, 18);
}