#include <stdio.h>
#include <math.h>
#define ROWS 4
#define COLS 5

void reverse_sub(double E[ROWS][COLS]){
    int d=ROWS-1; 
    double temp[ROWS];
    for(int i=0;i<ROWS;i++){
        int j=d-i;
        double soma=E[j][COLS-1];
        for(int k=j+1;k<COLS-1;k++){
            soma-=E[j][k] * temp[k];
        }
        soma/=E[j][j];
        printf("x_%d = %.16f\n", j+1,soma);
        temp[j]=soma;
    }
}

void printar_matriz(double E[ROWS][COLS]){
    for(int i=0;i<ROWS;i++){
        for(int j=0;j<COLS;j++) 
            printf("%f ", E[i][j]);
        printf("\n");
    }
}

void gauss(double E[ROWS][COLS]){
    for(int j=0;j<COLS-2;j++){
        for(int i=j;i<ROWS;i++){
            if(E[i][j]!=0){
                if(i!=j){
                    for(int k=0;k<COLS;k++){
                        double temp=E[i][k];
                        E[i][k]=E[j][k];
                        E[j][k]=temp;
                    }
                }

                //aplicar operações a*Lj + Lm -> Lm
                for(int m=j+1;m<ROWS;m++){
                    double a=-E[m][j]/E[j][j];
                    for(int n=j;n<COLS;n++){
                        E[m][n]+=a*E[j][n];
                    }
                }
                
                printar_matriz(E);
                printf("\n");
                break;
            }
            // break;

        }
        
    }
}

int main(){
    double E[ROWS][COLS]={{2,4,6,2,4},{1,2,-1,3,8},{-3,1,-2,1,-2},{1,3,-3,-2,6}};

    printar_matriz(E);
    printf("\n");
    gauss(E);
    reverse_sub(E);

    return 0;
}
