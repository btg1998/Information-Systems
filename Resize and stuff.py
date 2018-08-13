import numpy as np
M=np.arange(25).reshape(5,5)
N=M[:]
N.resize(1,25)
print(M)
print(N)
