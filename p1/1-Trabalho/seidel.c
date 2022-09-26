#include <stdio.h>
#include <math.h>
#define L 3
#define C 3

void jacobi(double A[L][C], double B[L], double chute[L], int n){
    for(int k=0;k<n;k++){
        for(int i=0;i<L;i++){
            double bi=B[i];
            for(int j=0;j<C;j++){
                if(j!=i) bi-=A[i][j]*chute[j];
            }
            bi/=A[i][i];
            printf("x_%d(%d) = %.16f | ", i+1, k+1, bi);
            chute[i]=bi;
        }
        printf("\n");
    }
}


// INSERIR O TAMANHO DA MATRIZ EM DEFINE
//***************************************************************************

int main(){
    double A[L][C]={{0.48,0.17,0.35},{0.19,0.51,0.30},{0.23,0.18,0.59}};
    double B[L]={4094,3311,5496};

    double chute[L]= {1000,500,500};
    int n=16;

    jacobi(A, B, chute, n);

    return 0;
}
