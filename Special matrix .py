import numpy as np
A=np.array([[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [ 4, 6, 13, 20, 22], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]])
ans=[]
row_sum=A.sum(axis=1)
N=A.transpose()
col_sum=N.sum(axis=1)
ans=row_sum+col_sum
np.append(ans,np.trace(A))
np.append(ans,np.trace(A[::-1]))
an=np.unique(ans)
if len(an)==1:
    print("yes")
else:
    print("no")
