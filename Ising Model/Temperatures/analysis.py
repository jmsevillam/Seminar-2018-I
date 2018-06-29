from os import walk
import numpy as np
for (dirpath,dirnames,filenames) in walk('temp/.'):
    files=filenames
M=[]
T=[]
files.sort()
for i in files:
    print(i)
    data=np.genfromtxt('temp/'+i)
    dataMag=data[:,1]
    T.append(float(i))
    Maverage=sum(dataMag[-1000:])/1000.
    M.append(Maverage)
import matplotlib.pylab as plt

plt.plot(T,M,'.')
plt.show()
