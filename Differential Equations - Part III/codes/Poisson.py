import numpy as np
import matplotlib.pylab as plt

def timestep(Matrix0):
    N0,M0=np.shape(Matrix0)
    Matrix2=Matrix0.copy()
    for i in range(1,N0-1):
        for j in range(1,M0-1):
            if frontera(i,j,N0,M0): continue
            Matrix2[i,j]=(Matrix0[i+1,j]+Matrix0[i-1,j]+Matrix0[i,j+1]+Matrix0[i,j-1])/4.
    return Matrix2
def frontera(i,j, N0,M0):
	if np.sqrt((i-N0/2.)**2+(j-N0/2.)**2.)<50 and np.sqrt((i-N0/2.)**2+(j-N0/2.)**2.)>48 : return True
	elif np.sqrt((i-N0/2.)**2+(j-N0/2.)**2.)<20 and np.sqrt((i-N0/2.)**2+(j-N0/2.)**2.)>18 : return True
#    if i==N0/4. and j<3.*N0/4 and j>N0/4: return True
#    if i==3.*N0/4. and j<3.*N0/4 and j>N0/4: return True
def Initial_Conditions(Matrix0):
    N0,M0=np.shape(Matrix0)
    V0=1.
    Matrix2=Matrix0.copy()
    for i in range(N0):
        for j in range(M0):
	        if np.sqrt((i-N0/2.)**2+(j-N0/2.)**2.)<50 and np.sqrt((i-N0/2.)**2+(j-N0/2.)**2.)>48 :  Matrix2[i,j]=V0
	        elif np.sqrt((i-N0/2.)**2+(j-N0/2.)**2.)<20 and np.sqrt((i-N0/2.)**2+(j-N0/2.)**2.)>18 :  Matrix2[i,j]=-V0
	       	else:  Matrix2[i,j]=0.
#            if (i==0 or i==N0-1) or (j==0 or j==N0-1):
#                Matrix2[i,j]=0
#            elif i==N0/4. and j<3.*N0/4 and j>N0/4: Matrix2[i,j]=V0
#            elif i==3.*N0/4. and j<3.*N0/4 and j>N0/4: Matrix2[i,j]=-V0
#            else: Matrix2[i,j]=0
    return Matrix2
size=100
Matrix=np.eye(size)
Matrix=Initial_Conditions(Matrix)
pl=plt.imshow(Matrix)
plt.colorbar(pl)
plt.show()
N=1501
for i in range(N):
    print (float(i)/float(N-1))
    Matrix=timestep(Matrix)
pl=plt.imshow(Matrix)
plt.colorbar(pl)
plt.show()
