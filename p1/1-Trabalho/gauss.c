#include <stdio.h>

#define ROWS 3
#define COLS 4

void print_matrix(double matrix[ROWS][COLS]){
    for(int i=0; i < ROWS; i++){
        for(int j = 0; j < COLS; j++){
            printf("%f\t", matrix[i][j]);
        }
        printf("\n");
    }
}

void gauss(double E[ROWS][COLS]){
    for(int j =0; j< COLS -2; j++){
        for(int i=j; i<ROWS;i++){
            if(E[i][j] != 0){
                if(i!=j){
                    //é preciso trocar linhas
                    for(int k=0;k<COLS;k++){
                        double temp = E[i][k];
                        E[i][k] = E[j][k];
                        E[j][k] = temp;
                    }
                }
                //aplicar operações elementares em linha
                // a * Lj + Lm -> Lm
                for (int m = j+1; m<ROWS;m++){
                    double a = -E[m][j]/E[j][j];
                    for(int n=j;n<COLS;n++){
                        E[m][n] += a * E[j][n];
                    }
                }
                print_matrix(E);
                printf("\n");
                break;
            }
        }
    }
}

void reverse_sub(double E[ROWS][COLS]){
    int last = ROWS - 1;
}

int main(){
    double E[ROWS][COLS] = {
        {0.48, 0.17, 0.35, -4094},
        {0.19, 0.51, 0.30, -3311},
         {0.23, 0.18, 0.59,-5496} 
    };

    print_matrix(E);
    printf("\n");
    gauss(E);

    //reverse_sub(E);
}
