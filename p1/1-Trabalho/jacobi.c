#include <stdio.h>
#include <math.h>
#include "func.h"

#define L 4
#define C 4

void jacobi(double A[L][C], double B[L], double chute[L], int n){
    double next[L];
    for(int k=0;k<n;k++){
        for(int i=0;i<L;i++){
            double bi=B[i];
            for(int j=0;j<C;j++){
                if(j!=i) bi-=A[i][j]*chute[j];
            }
            bi/=A[i][i];
            printf("x_%d(%d) = %.16f | ", i+1, k+1, bi);
            next[i]=bi;
        }
        printf("\n");
        //atualizar o chute
        for(int i=0;i<L;i++) chute[i]=next[i];
    }
}

int main(){
    double A[L][C]={{-5.84, -1.59, 0.24, 2.9},{1.27, 8.71, 2.58, -3.75},{-0.31, 1.2, 5.21, 2.58},{3.79, 0.86, -3.67, -9.44}};
    double B[L]={4.06, 1.13, -2.75, 2.54}; // result

    double chute[L]={0.36, 0.25, -0.66, 1.62}; // x0
    int n=18;

    jacobi(A, B, chute, n);

    return 0;
}
