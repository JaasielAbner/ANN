#include <stdio.h>
#define ROWS 3
#define COLS 4

void print_matrix(double m[ROWS][COLS]){
    for(int i = 0; i < ROWS; i++){
        for(int j = 0; j < COLS; j++){
            printf("%.8lf ", m[i][j]);
        }
        printf("\n");
    }
}

void gauss(double m[ROWS][COLS]){
    double a;
    double temp;
    for(int j = 0; j < ROWS; j++){ // coluna
        for(int p = j; p < ROWS; p ++){ // linha
            if(m[p][j] != 0){
                if(p != j){
                    // trocando as linhas p e j
                    temp = 0;
                    for(int k = 0; k < COLS; k ++){
                        temp = m[j][k];
                        m[j][k] = m [p][k];
                        m[p][k] = temp;
                    }
                }

                for(int i = j+1; i < ROWS; i++){
                    a = -m[i][j] / m[j][j];
                    for(int q = 0; q < COLS; q++){
                        m[i][q] += a * m[j][q];
                    }
                }

            }
        }
        print_matrix(m);
        printf("\n\n");
    }
}

int main(){
    double m[ROWS][COLS] = {{1,2,3,4},{1,5,3,1}, {2,4,-1,1}};
    gauss(m);

    return 0;
}