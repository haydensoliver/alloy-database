
from matplotlib import pyplot as plt
import numpy as np

base = 92
path = "/fslhome/holiver2/work/vasp/alloydatabase/finished/0-CdCoN/"

EATOM = []
PSCENC = []
TOTEN = []
TEWEN = []
EBANDS = []
SIGMA0 = []
nENTRO = []
CPUTIME = []
IRRKPTS = []
KPTORDER = []

with open(path + "EBANDS.txt", "r") as f:
    for line in f.readlines():
        EBANDS.append(float(line))

with open(path + "energySigma0.txt", "r") as f:
    for line in f.readlines():
        SIGMA0.append(float(line))

with open(path + "PSCENC.txt", "r") as f:
    for line in f.readlines():
        PSCENC.append(float(line))

with open(path + "TEWEN.txt", "r") as f:
    for line in f.readlines():
        TEWEN.append(float(line))

with open(path + "TOTEN.txt", "r") as f:
    for line in f.readlines():
        TOTEN.append(float(line))
errorTOTEN = []
for i in TOTEN:
    errorTOTEN.append(abs(i-TOTEN[base]))

        
with open(path + "EATOM.txt", "r") as f:
    for line in f.readlines():
        EATOM.append(float(line))

with open(path + "noEntropy.txt", "r") as f:
    for line in f.readlines():
        nENTRO.append(float(line))

with open(path + "cputime.txt", "r") as f:
    for line in f.readlines():
        CPUTIME.append(float(line))

with open(path + "irrkpts.txt", "r") as f:
    for line in f.readlines():
        IRRKPTS.append(float(line))

with open(path + "kptorder.txt", "r") as f:
    for line in f.readlines():
        a = int(line[2:4])
        b = int(line[12:14])
        KPTORDER.append([a,b])

#print(KPTORDER)

alldata = sorted(zip(KPTORDER,CPUTIME,IRRKPTS,TOTEN,TEWEN,PSCENC,SIGMA0,nENTRO,EBANDS))

#print(alldata[0])

error_alldata = []

#i for i in abs(alldata[-1] - alldata[0]))


for i in range(0,len(alldata)-1):
    A = []
    A.append(alldata[i][0])
    for j in range(1,len(alldata[-1])):
        a = abs(alldata[-1][j] - alldata[i][j])
        
        A.append(a)
    A[2] = alldata[i][2]
    error_alldata.append(A)

#print(error_alldata)

kpts = 4

eTOTEN = []
eTEWEN = []
ePSCENC = []
eSIGMA0 = []
e_nENTRO = []
eEBANDS = []
ikpts = []


#print(error_alldata)
for h in range(0,14):
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    irrk = []
#KPTORDER,CPUTIME,IRRKPTS,TOTEN,TEWEN,PSCENC,SIGMA0,nENTRO,EBANDS
    for i in range(len(error_alldata)):                                                   
        if error_alldata[i][0][0] == kpts:
            a.append(alldata[i][3])
            b.append(error_alldata[i][4])
            c.append(error_alldata[i][5])
            d.append(error_alldata[i][6])
            e_nENTRO.append(error_alldata[i][7])
            f.append(error_alldata[i][8])
            irrk.append(error_alldata[i][2])
    kpts = 3 * h + 4
    eTOTEN.append(a)
    eTEWEN.append(b)
    ePSCENC.append(c)
    eSIGMA0.append(d)
    e_nENTRO.append(e)
    eEBANDS.append(f)
    ikpts.append(irrk)
    #print(a)
    
#print(eTOTEN)
del eTOTEN[0]
del ikpts[0]
del eSIGMA0[0]

print(ikpts)
    
"""Now we're going to plot the data"""
base = 92 #line number 93 is the 43x43x43 kpt grid

for i in range(len(ikpts)):
    plt.plot(ikpts[i],eSIGMA0[i])
plt.loglog()
plt.xlabel("Irreducible k-points")
plt.ylabel("Error")
plt.title("Energy Sigma -> 0")
plt.savefig('graph3.pdf')



for i in range(len(ikpts)):
#    print(ikpts[i])
    n = 4 + i * 3
    plt.plot(ikpts[i],eTOTEN[i], label=str(n) + 'frzkpts')
plt.loglog()
plt.legend(loc='best')
plt.xlabel("Irreducible k-points")
plt.ylabel("Error")
plt.title("TOTEN")

plt.savefig('graph4.pdf')


















#print(TOTEN[base])


#print(errorTOTEN)
"""
plt.scatter(IRRKPTS, errorTOTEN)
#plt.loglog()
plt.xlabel("# of Irreducible Kpoints")
plt.ylabel("Error")
plt.title("nKpoints vs error")
plt.savefig('graph1.pdf', bbox_inches='tight')


plt.scatter(IRRKPTS, CPUTIME)
plt.xlabel("Irreducible Kpoints")
plt.ylabel("Time")
plt.savefig('graph2.pdf', bbox_inches='tight')

#plt.scatter(
"""
