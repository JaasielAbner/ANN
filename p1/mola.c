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
int main() {
    double m1 = 5.98,
            m2 = 5.46,
            m3 = 2.79,
            k1 = 57.29,
            k2 = 51.63,
            k3 = 97.99,
            g = 9.81;

    // Seidel input
    double a[L][C] = {{k1+k2, -k2, 0},
                            {-k2, k2+k3, -k3},
                            {0, -k3, k3}
    };

    double b[L] = {m1*g, m2*g, m3*g};

    double chute[C] = {2, 3, 3};

    int n = 200;

    jacobi(a,b,chute,n);

    return 0;
}