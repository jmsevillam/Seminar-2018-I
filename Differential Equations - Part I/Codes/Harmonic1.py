import math as m
def g(theta0,omega0):
	return omega0
def f(theta0,omega0,t):
	return -w0**2.*theta0
gamma=.2
w0=1.
omega=1.
theta=0.
h=0.1
N=1000
delta=1.
w=.2
F=2.
for i in range(N):
	print i*h,theta,omega	
	theta1=theta+h*g(theta,omega)
	omega1=omega+h*f(theta,omega,i*h)
	theta=theta1	
	omega=omega1

