#include<stdio.h>
#include <math.h>

#define ROWS 3
#define COLS 4

void print_matriz(double m[ROWS][COLS]){
    for(int i=0; i<ROWS; i++){
        for(int j=0; j<COLS; j++){
            printf("%.8f\t", m[i][j]);
        }
        printf("\n");
    }
}

void gauss(double E[ROWS][COLS]) {
    for (int j = 0; j < COLS ; j++) {
        for (int i = j; j < ROWS; i++) {
            if (E[i][j]!= 0) {
                if(i != j) { 
                    // trocar linhas
                    for (int k = 0; k < COLS - 2; k++) {
                        double aux = E[i][k];
                        E[j][k] = E[j][k];
                        E[j][k] = aux;
                    }
                }
                // aplicar operações elementares em linha
                // a * Lj + Lm -> Lm
                for (int m = j + 1; m < ROWS; m++) {
                    double a = -E[m][j]/E[j][j];
                    for (int n = j; n < COLS; n++) {
                        E[m][n] += a * E[j][n];
                    }
                }
                print_matriz(E);
                printf("\n");
                break; //para de procurar elementos diferentes de 0
            }
            else {
                if(i == ROWS - 1){
                    printf("Sistema não tem solução");
                }
            }
        } 
    } 
}

int main(int argc, char *argv[]){
    
    double m[ROWS][COLS] = {{-1 , 0, 1, 1},
                                                    {1, -1, 1, 1} , 
                                                    {0, 1 , -1, 1}};
    print_matriz(m);
    printf("\n");
    gauss(m);
    
}
/* 
    Blocos plano inclinado

    double m1 = 132;
    double m2 = 105;
    double m3 = 37;
    double u1 = 0.27;
    double u2 = 0.39;
    double u3 = 0.43;
    double g = 9.81;
    double ang = 0.82030474843; // em rad
    
    double F1h = m1 * g * (sin(ang));
    double F2h = m2 * g * (sin(ang));
    double F3h = m3 * g * (sin(ang));

    double F1v = m1 * g * (cos(ang));
    double F2v = m2 * g * (cos(ang));
    double F3v = m3 * g * (cos(ang));
    
    double f1 = u1 * F1v;
    double f2 = u2 * F2v;
    double f3 = u3 * F3v; */