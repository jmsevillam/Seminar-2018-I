from os import walk
import numpy as np
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
folder='mag/'
for (dirpath,dirnames,filenames) in walk(folder+'.'):
    files=filenames
    break
print files
M=[]
T=[]
files.sort()
num=1000
for i in files:
        print(i)
        data=np.genfromtxt(folder+i)
        dataMag=data[:]
        T.append(float(i))
        Maverage=sum(dataMag[-int(num):])/num
        M.append(Maverage)
import matplotlib.pylab as plt

fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_xlabel('Temperature $T$')
ax.set_ylabel('Magnetization $|<M>|$')
ax.plot(T,M,'.-', label='Simulation')
plt.savefig('plot1.pdf')
plt.show()

folder='sus/'
for (dirpath,dirnames,filenames) in walk(folder+'.'):
    files=filenames
    break
print files
Chi=[]
T=[]
files.sort()
for i in files:
        print(i)
        data=np.genfromtxt(folder+i)
        dataMag=data[:]
        T.append(float(i))
        Chiaverage=sum(dataMag[-int(num):])/num
        Chi.append(Chiaverage)
import matplotlib.pylab as plt

fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_xlabel('Temperature $T$')
ax.set_ylabel('Susceptibility $|<\chi>|$')
ax.plot(T,Chi,'.-', label='Simulation')
plt.savefig('plot2.pdf')
plt.show()
