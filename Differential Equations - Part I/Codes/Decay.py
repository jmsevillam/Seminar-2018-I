def f(P0):
	return -P0/tau
tau=1. 
h=0.01
N=1000
P=1.

for i in range(N):
	print i*h,P
	P=P+h*f(P)
