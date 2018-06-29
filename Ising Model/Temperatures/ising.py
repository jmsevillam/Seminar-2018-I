import numpy as np
import matplotlib.pylab as plt
import sys


def H(ising0,i1,j1):
	ip=i1+1
	il=i1-1
	jp=j1+1
	jl=j1-1

	if jl<0: jl=N-1
	if jp==N: jp=0
	if il<0: il=N-1
	if ip==N: ip=0
    
	return J*(ising0[i1,jp]+ising0[i1,jl]+ising0[ip,j1]+ising0[il,j1])

def init(ising0):
	for i in range(N):
		for j in range(N):
			ising0[i,j]=2*np.random.random_integers(0,1)-1

def MCstep(ising0):
	i0=np.random.random_integers(0,N-1)
	j0=np.random.random_integers(0,N-1)
	E=H(ising0,i0,j0)
	Eold=ising0[i0,j0]*E +h*ising[i0,j0]
	Enew=-ising0[i0,j0]*E - h*ising[i0,j0]

	dE=(Eold-Enew)	
	if dE<0.:
		ising0[i0,j0]=-ising0[i0,j0]
	else:
		r=np.random.rand(1)[0]
		if r<np.exp(-dE/kbT):
			ising0[i0,j0]=-ising0[i0,j0]
			
kbT=float(sys.argv[1])
h=.1
J=1.
N=25
ising=np.empty((N,N))
init(ising)

NMS=N*N
data=open("temp/"+sys.argv[1],"w")
for i in range(300*NMS):
	MCstep(ising)
	data.write(str(i)+"\t"+str(np.sum(ising)/NMS)+'\n')
data.close()
