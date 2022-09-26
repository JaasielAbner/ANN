#include <stdio.h>
#include <math.h>
#define L 6
#define C 6

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
    double g = 9.81, k = 52 * M_PI/180,
            mi1 = 0.24, mi2 = 0.51, mi3 = 0.51,
            m1 = 64, m2 = 56, m3 = 28,
            r1 = (m1 * g * sin(k)) - (mi1 * m1 * g * cos(k)),
            r2 = (m2 * g * sin(k)) - (mi2 * m2 * g * cos(k)),
            r3 = (m3 * g * sin(k)) - (mi3 * m3 * g * cos(k));

    printf("%.16f,   %.16f,   %.16f", r1, r2, r3);

    // Seidel input
    double a[L][C] = {{m1, 1, 0},
                            {m2, -1, 1},
                            {m3, 0, -1}
    };

    double b[C] = {r1, r2, r3};

    double chute[L] = {5, 148, 127};

    int n = 300;

    jacobi(a,b,chute,n);

    return 0;
}
