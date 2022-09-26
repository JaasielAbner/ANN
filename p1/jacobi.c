#include<stdio.h>

/* #define ROWS 3
#define COLS 3 */

#define ROWS 4
#define COLS 4

void jacobi(double A[ROWS][ROWS], double B[ROWS], double chute[ROWS], int n){

    double next[ROWS];
    for(int k = 0 ; k < n ; k++){
        for(int i = 0 ; i < ROWS ; i++){
            double bi = B[i];
            for(int j = 0 ; j < ROWS ; j++){
                if(j != i){
                    bi -= A[i][j] * chute[j];
                }
            }
            bi /= A[i][i];
            printf("x_%d^(%d) = %.16f\t", i+1, k+1, bi);
            next[i] = bi;
        }
        printf("\n");
        //atualizar o chute
        for(int i = 0 ; i < ROWS ; i++){
            chute[i] = next[i];
        }
    }

}

int main(){
    
/* M[3][3]
    double a[ROWS][COLS] = {{5.05, 3.02, 0.98, }, {-1.03, 5.42, 3.34}, {-4.78, 3.43, 9.26}};
    double b[ROWS] = {-0.75, -2.14, 3.36};
    double chute[COLS] = {-4.09, -0.7, -1.09}; */

    double a[ROWS][COLS] = {{7.45, 3.68, -0.53, -2.07}, {3.54, -8.08, 0.51, -2.87}, {-0.25, -0.57, 4.41, -2.43}, {4.94, -1.83, -2.06, -9.99}};
    double b[ROWS] = {-4.38, -1.47, 0.66, -4.68};
    double chute[COLS] = {-3.59, 4.24 ,-2.43,3.77}; 

    int n = 16;

    jacobi(a, b, chute, n);
}
/*     for(int it = 0; it < n; it++){
        double temp[COLS];
        for(int i =0; i < ROWS; i++){
            double xi = b[i];
            for(int j=0; j<COLS; j++){
                if(i != j){
                    xi -= a[i][j] * chute[j];
                }
            }
            xi /= a[i][i];
            temp[i] = xi;
        }
        printf("X^(%d) -> ", it + 1);
        for(int k=0; k < COLS; k++){
            chute[k] = temp[k];
            printf("%.10f\t", chute[k]);
        }
        printf("\n");
    } */