#include<iostream>
const double tau=1.;
double f(double P0);
int main(void){
  double h=0.01;
  int N=1000;
  double P=1.;
  for(int i=0;i<N;i++){
    std::cout<<i*h<<'\t'<<P<<std::endl;
    P=P+h*f(P);
  }

  return 0;
}

double f(double P0){
  return -P0/tau;
}
