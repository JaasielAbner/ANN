void main(){

    double n = 187016026;
    double lambda = (1.41*pow(10,-10));

    double f(double x){
        return ((n+1)/(1 + n * exp(-lambda*(n+1)*x)) - (n/4));
    }
    
    double inferior1 = 0;
    double superior1 = 1445.00;
    int iteracoes1 = 12;

    printf("inferior aqui krl: %lf\n",inferior1);
    //bisection(f, inferior1, superior1, iteracoes1);

}
