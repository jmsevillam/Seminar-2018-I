#include<iostream>
#include<cmath>
const double w0=1., gamma=0.2;
const double h=0.1, delta=1.0;
const double F=0.4, w=0.2;
const int N=1000;
double g(double theta0,double omega0,double t);
double f(double theta0,double omega0,double t);
int main(void){
  double omega=1;
  double theta=0;
  for(int i=0;i<N;i++){
    std::cout<<i*h<<'\t'<<theta<<'\t'<<omega<<std::endl;	
    omega=omega+h*f(theta,omega,i*h);
    theta=theta+h*g(theta,omega,i*h);
  }
  return 0;
}
double g(double theta0,double omega0,double t){
  return omega0;}
double f(double theta0,double omega0,double t){
  return -w0*w0*sin(theta0)-gamma*omega0+F*sin(w*t+delta);}
