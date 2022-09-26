#include<stdio.h>
#include<math.h>

void bisection(double (*f)(double), double a, double b, int n){
    double fa = f(a);
    double fb = f(b);
    if(fa * f(b) >= 0){
        printf("Não sei dizer que f possui raiz no intervalo raiz no intervalo [%f, %f]", a, b);
        return;
    }else{
        double m =0;
        for(int i=0; i<n; i++){
           
            m = 0.5 * (a + b);
            printf("x_%d = %.16f\n", i + 1, m);
            
            if(f(a) * f(m) < 0){
                b = m;
            }else{
                a = m;
            }
        }
    }

}

int main(int argc, char *argv[]){
    /*double f(double x){
        //double e = 2.71828182845904523530287; // euler
        return pow(x,3) -7 * pow(x,2) + 14 * x -7;
    }
    double a = 0.09722;
    double b = 4.46304;
    int n = 5;*/

    /*double f(double m){
        double e = 2.71828182845904523530287; // euler
        return ((9.81*m)/25.91)*(1 - pow(e, -(25.91/m)*8.31)) - 30.83;
    }
    double a = 36.08;
    double b = 180.1;
    int n = 20;*/

    /*double f(double c){
        double e = 2.71828182845904523530287; // euler
        return ((9.81*68.88)/c)*(1 - pow(e, -(c/68.88)*9.1)) - 20.97;
    }
    double a = 1;
    double b = 100;
    int n = 14;*/

/*    double f(double h){
        //double e = 2.71828182845904523530287; // euler
        double g = 9.81;
        return sqrt(2*g*h)*tanh(sqrt(2*g*h)/(2*5.02)*6.19) - 8.23;
    }
    
    double a = 0.19;
    double b = 17.86;
    int n = 12;
*/

/*  double f(double y){
        //double e = 2.71828182845904523530287; // euler
        double g = 9.81;
        double a = 2.93*y + pow(y,2)/2;
        double b = 2.93 + y;
        double q = 196.01;
        return 1-(pow(q, 2)/(g*pow(a, 3)))*b;
    }
    double a = 0.69;
    double b = 9.99;
    int n = 12;
*/

/* double f(double h){
        //double e = 2.71828182845904523530287; // euler
        double pi = 3.14159265358979323846;
        return (pi*pow(h, 2))*((3*7.28-h)/3) - 645.67;
    }
    double a = 0;
    double b = 14.56;
    int n = 12; */

/*     double f(double h){
        //double e = 2.71828182845904523530287; // euler
        double pi = 3.14159265358979323846;
        double r = 8.71;
        double vs = (4*pi*pow(r, 3))/3;
        double v = vs - ((737.18*vs)/1000);
        return ((pi*pow(h,2))/3) * (3*r-h) - v;
    }
    double a = 0;
    double b = 17.42;
    int n = 12; */

    /*double f(double l){
        double e = 2.71828182845904523530287; // euler
        double p0 = 1500163;
        double v = 309996;
        double p = 3075393;
        return p0*pow(e, l) + (v/l)*(pow(e, l)-1) - p;
    }
    double a = 0.1;
    double b = 1;
    int n = 15;*/

    /*double r = 1.04;
    double f(double h){
        //double e = 2.71828182845904523530287; // euler
        double pi = 3.141592653589793238462643;
        double l = 4.35;        
        double v = 6.24;

        return l*(0.5*pi*pow(r,2) - pow(r,2)*asin(h/r) - h*sqrt(pow(r,2)-pow(h,2))) - v;
    }
    //colocar r - h lá em cima
    double a = 0;
    double b = r;
    int n = 15;*/

    /*double f(double w){
        //double e = 2.71828182845904523530287; // euler
        //double pi = 3.141592653589793238462643;
        double g = 9.81;       
        double t = 1;
        double xt = 1.83;

        return -((g/(2*pow(w,2)))*(sinh(w*t) - sin(w*t))) - xt;
    }
    double a = -4.24;
    double b = -0.31;
    int n = 15;*/

    /*double f(double l){
        //double e = 2.71828182845904523530287; // euler
        //double pi = 3.141592653589793238462643;

        return (179371/1000) - ((2801/25)*l) + 12*pow(l,2);
    }
    double a = 0;
    double b = 4.96;
    int n = 15;*/

    //p1
/*     double f(double x){
        //double e = 2.71828182845904523530287; // euler
        //double pi = 3.141592653589793238462643;

        return pow(x, 3) - 7*pow(x,2) + 14*x - 7;
    }
    double a = 0.04308;
    double b = 4.30541;
    int n = 15; */

    /*double f(double t){
        double e = 2.71828182845904523530287; // euler
        //double pi = 3.141592653589793238462643; //pi
        double l = 1.41 * pow(10,-10);
        double n = 203059833;

        return (n + 1) / (1 + n*pow(e, -l*(n+1)*t)) - 25;
    }
    double a = 0;
    double b = 1337;
    int n = 15; */

    /* double r = 1.22;
    double f(double h){
        //double e = 2.71828182845904523530287; // euler
        double pi = 3.14159265358979323846;
        double vs = (4*pi*pow(r, 3))/3;
        double v = vs - ((462.37*vs)/1000);
        return ((pi*pow(h,2))/3) * (3*r-h) - v;
    }
    double a = 0;
    double b = 2*r;
    int n = 15;
 */


/*     double f(double h){
        //double e = 2.71828182845904523530287; // euler
        double pi = 3.141592653589793238462643;
        double l = 5.51;        
        double v = 49.67;
        double r = 3.29;
        return l*(0.5*pi*pow(r,2) - pow(r,2)*asin(h/r) - h*sqrt(pow(r,2)-pow(h,2))) - v;
    }
    //colocar r - h lá em cima
    double a = 0;
    double b = 3.29;
    int n = 12; */

/*     double f(double w){
        //double e = 2.71828182845904523530287; // euler
        //double pi = 3.141592653589793238462643;
        double g = 9.81;       
        double t = 1.47;
        double xt = 3.97;
        return -((g/(2*pow(w,2)))*(sinh(w*t) - sin(w*t))) - xt;
    } */

/*    double f(double x){
        return 168.6972-110.72*x+12*pow(x,2);
    } 
    double a = 0;
    double b = 4.53;
    int n = 12; */

    double f(double t){
        double e = 2.71828182846; // euler
        double n = 103481111;
        double lambda = 1.41*1 / pow(10,10);
        double x = (n * 25)/ 100;
        return ( (n+1) / (1 + n * (1/exp(lambda*(n+1)*t ))) ) - x;
    }

    double a = 0;
    double b = 2530;
    int n = 12;

    bisection(f, a, b, n);
}