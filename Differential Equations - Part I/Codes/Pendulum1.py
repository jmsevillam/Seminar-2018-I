import math as m
def g(theta0,omega0):
	return omega0
def f(theta0,omega0,t):
	return -w0**2.*m.sin(theta0)-gamma*omega0+F*m.sin(w*t+delta)
gamma=.2
w0=1.
omega=1.
theta=0.
h=0.1
N=1000
delta=1.
w=.2
F=.4
for i in range(N):
	print i*h,theta,omega	
	omega=omega+h*f(theta,omega,i*h)
	theta=theta+h*g(theta,omega)

