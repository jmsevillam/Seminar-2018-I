import numpy as np
import matplotlib.pylab as plt

def H(ising0,i1,j1):
	E=0.
	ip=i1+1
	il=i1-1
	jp=j1+1
	jl=j1-1
	
	if jl<0: jl=M-1
	if jp==M: jp=0
	if il<0: il=N-1
	if ip==N: ip=0
	
	E=J*(ising0[i1,jp]+ising0[i1,jl]+ising0[il,j1]+ising0[ip,j1])
	
	return E

def f(x0):
	if x0>0.5:
		return 1.
	else:
		return -1.

def initialize(ising0):
	for i in range(N):
		for j in range(M):
			r0=np.random.rand(1)[0]
			ising0[i,j]=f(r0)

def MonteCarloStep(ising0):
	i0=int(N*np.random.rand(1)[0])		
	j0=int(M*np.random.rand(1)[0])

	Eold=ising0[i0,j0]*H(ising0,i0,j0)
	Enew=-ising0[i0,j0]*H(ising0,i0,j0)

	dE=Eold-Enew
	if dE<0:
		ising0[i0,j0]=-ising0[i0,j0]
	else:
		r=np.random.rand(1)[0]
		if r<np.exp(-dE/kbT):
			ising0[i0,j0]=-ising0[i0,j0]
	
N=100
M=100
kbT=.1

ising=np.zeros((N,M))
plt.imshow(ising)
plt.show()
initialize(ising)
#print np.sum(ising)/(N*M)
pl=plt.imshow(ising)
plt.colorbar(pl)
plt.savefig('1.png')
plt.show()
J=1.
for i in range(N*N*M*M):
	MonteCarloStep(ising)
	print i,np.sum(ising)/(N*M)
pl=plt.imshow(ising,vmin=-1,vmax=1)
plt.colorbar(pl)
plt.savefig('2.png')
plt.show()
