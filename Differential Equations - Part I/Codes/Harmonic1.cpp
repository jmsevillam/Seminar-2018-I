#include<iostream>
#include<cmath>
const double w0=1.;
const double h=0.1;
double g(double theta0,double omega0,double t);
double f(double theta0,double omega0,double t);
int main(void){
  double omega=1,omega1; double theta=0,theta1;
  int N=1000;
  for(int i=0;i<N;i++){
    std::cout<<i*h<<'\t'<<theta<<'\t'<<omega<<std::endl;	
    theta1=theta+h*g(theta,omega,i*h);
    omega1=omega+h*f(theta,omega,i*h);
    theta=theta1;
    omega=omega1;}
  return 0;}
double g(double theta0,double omega0,double t){
  return omega0;}
double f(double theta0,double omega0,double t){
  return -w0*w0*theta0;}
