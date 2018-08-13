import numpy as np
M=np.arange(100*100).reshape(100,100)
N=M
N.resize(1,100*100)
Ans=np.array(np.where(N>50))
print(Ans.sum())
