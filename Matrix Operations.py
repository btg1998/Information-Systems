import sys
import numpy as np
try:
    n = int(input("Enter N for a NxN matrix: "))
except ValueError:
    print("Oops!  That was no valid number.")
    sys.exit(0)
M=np.arange(n*n).reshape(n,n)
print("matrix: ",M)
ch=int(input(" Enter Choice 1-transpose 2- trace 3-min 4-max 5-mean 6-variance 7-unique elements 8-indices of min and max 9- second small "))
if(ch==1):
    print(M.transpose())
elif ch==2:
    print(np.trace(M))
elif ch==3:
    print(M.min())
elif ch==4:
    print(M.max())
elif ch==5:
    print(M.mean())
elif ch==6:
    print(np.var(M))
elif ch==7:
    print(np.unique(M))
elif ch==8:
    j=np.argmin(M)
    print(" Min: "+str(j))
    print(j/n,j%n)
    j=np.argmax(M)
    print(" Max: "+str(j))
    print(j/n,j%n)
elif ch==9:
    N=M
    i=np.argmin(N)
    j=i
    j=j/n
    M[j][(i%n)]=n*n
    i=N.min()
    print(i)
    
