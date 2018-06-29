from os import walk
import numpy as np
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
for (dirpath,dirnames,filenames) in walk('.'):
    files=filenames
    break
print files
    
M=[]
T=[]
files.sort()
for i in files:
    if(hasNumbers(i)):
        print(i)
        data=np.genfromtxt(i)
        dataMag=data[:,1]
        T.append(float(i))
        Maverage=sum(dataMag[-1000:])/1000.
        M.append(Maverage)
import matplotlib.pylab as plt

plt.plot(T,M,'.')
plt.show()
