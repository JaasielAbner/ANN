#include <stdio.h>
#include <math.h>
#define ROWS 4
#define COLS 4

void printar_matriz(double E[ROWS][COLS]){
    printf("\n");
    for(int i=0;i<ROWS;i++){
        for(int j=0;j<COLS;j++) 
            printf("%.14f ", E[i][j]);
        printf("\n");
    }
}

void trocarLinha(int l1, int l2, double E[ROWS][COLS]){
    double aux[COLS];
    for(int i=0;i<COLS;i++) aux[i]=E[l1][i];
    for(int i=0;i<COLS;i++) E[l1][i]=E[l2][i];
    for(int i=0;i<COLS;i++) E[l2][i]=aux[i];
    printar_matriz(E);
}

void mult(double E[ROWS][COLS], double x, int l){
    for(int i=0;i<COLS;i++) E[l][i]*=x;
    printar_matriz(E);
}

void combinacaoLinear(double E[ROWS][COLS], double x, int Lmult, int Lsoma, int Ldestino){
    for(int i=0;i<COLS;i++) E[Ldestino][i]=(x*E[Lmult][i] + E[Lsoma][i]);
    printar_matriz(E);
}

int main(){
    double E[ROWS][COLS]={{-1,-4,4,1}, {5,5,-7,7}, {-2,7,5,2}, {5,-3,7,-7}};
    combinacaoLinear(E, 5, 0, 1,1);
    combinacaoLinear(E, -2,0,2,2);
    combinacaoLinear(E,5,0,3,3);
    combinacaoLinear(E,1,1,2,2);
    combinacaoLinear(E, -23.0/15.0, 1, 3,3);
    combinacaoLinear(E, -53.0/75.0,2,3,3);
    

    return 0;
}
