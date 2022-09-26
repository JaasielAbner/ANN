#include <stdio.h>
#include<math.h>

void seidel(double *chute, int rows, double matrix[rows][rows+1], int n){
    for(int i=0; i<n; i++){
        for(int r =0; r<rows; r++){
            double temp = 0;
            temp += matrix[r][rows];
            for(int c = 0; c<rows; c++){
                if(r!=c){
                    temp -= (matrix[r][c] * chute[c]);
                }
            }
            temp /= matrix[r][r];
            printf("X_%d,%d = %.16f\n", r + 1, i + 1, temp);
            chute[r] = temp;
        }
        printf("\n");
    }
}

int main(){
    /*
    //ordem do sistema
    int rows = 3;
    //estimativa inicial para solução do sistema
    double chute[3] = {-1.73763, 0.57524, 0.71905};
    //matriz estendida do sistema linear
    double matrix[3][4] = {{3.65843, 1.64339, 0.5043, 2.03862}, {1.97877, -8.46215, -4.97264, -4.06993}, {4.79323, 3.72841, 10.03238, -1.48057}};
    //numero máximo de iterações
    int max_iter = 18;
    */

   //ordem do sistema
    int rows = 4;
    //estimativa inicial para solução do sistema
    double chute[4] = {2.66, 4.35, 4.14, -0.87};
    //matriz estendida do sistema linear
    double matrix[4][5] = {{-16.34, -4.84, 4.82, -4.93, -2.07 }, {3.84, 11.14,-1.49, 4.06, 3.23}, {1.38, -3.2, -9.09, -2.76, 0.43}, {-0.67, -3.48, 3.44, -9.34, -0.54}};
    //numero máximo de iterações
    int max_iter = 16;

    seidel(chute, rows, matrix, max_iter);
}

/* double pi = 3.141592653589793238462643;
    double g = 9.81, k = 36 * pi/180,
            mi1 = 0.27, mi2 = 0.41, mi3 = 0.48,
            m1 = 135, m2 = 124, m3 = 121,
            r1 = (m1 * g * sin(k)) - (mi1 * m1 * g * cos(k)),
            r2 = (m2 * g * sin(k)) - (mi2 * m2 * g * cos(k)),
            r3 = (m3 * g * sin(k)) - (mi3 * m3 * g * cos(k));

    printf("%.16f,   %.16f,   %.16f", r1, r2, r3);

    // Seidel input
    double a[ROWS][COLS] = {{m1, 1, 0},
                            {m2, -1, 1},
                            {m3, 0, -1}
    };

    double b[ROWS] = {r1, r2, r3};

    double chute[COLS] = {5, 148, 127};

    int n = 500; */