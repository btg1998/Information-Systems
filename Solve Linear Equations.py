from scipy import linalg
import numpy as np
A=np.array([[1,-1,1],[1,-1,0],[1,1,-1]])
B=np.array([42,6,6])
print(linalg.solve(A,B))
