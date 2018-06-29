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
num=100
for i in files:
    if(hasNumbers(i)):
        print(i)
        data=np.genfromtxt(i)
        dataMag=data[:]
        T.append(float(i))
        Maverage=sum(dataMag[-int(num):])/num
        M.append(Maverage)
import matplotlib.pylab as plt

plt.plot(T,M,'.-')
plt.savefig('plot1.pdf')
plt.savefig('plot1.png')
plt.show()
