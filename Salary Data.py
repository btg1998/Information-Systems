from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import csv
import scipy
import numpy as np
import matplotlib
from scipy import stats
from scipy.optimize import curve_fit
def func(x, a,b,c,d):
     return a*(x**3) + b*(x**2) + c*x +d

Data=[]
with open('SalaryData.csv', 'r') as csvfile:
    read = csv.reader(csvfile, delimiter=',', quotechar='|')
    f=0
    for row in read:
        if f!=0:
            Data.append(row)
        f=f+1
Exp=[]
TExp=[]
Sal=[]
for i in Data:
    Exp.append(int(i[2]))
    TExp.append(int(i[4]))
    Sal.append(int(i[5]))
print("Stats of Experience: ")
print(stats.describe(Exp))
print("Stats of Total Experience: ")
print(stats.describe(TExp))
print("Stats of Salary: ")
print(stats.describe(Sal))
fig=plt.figure()
fig.suptitle('Experience V/S Salary', fontsize=14, fontweight='bold')
plt.scatter(Exp,Sal)
Sal=np.array(Sal)
Exp=np.array(Exp)
popt, pcov = curve_fit(func, Exp, Sal)
SSR=(sum((func(Exp,*popt)-Sal)**2)/Exp.size)
print(SSR)
plt.plot(np.unique(Exp), np.poly1d(np.polyfit(Exp, Sal, 3))(np.unique(Exp)))
#plt.plot(Exp, func(Exp, *popt))
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()
