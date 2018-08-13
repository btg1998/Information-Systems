import numpy as np
from scipy import special
import scipy.integrate as integrate

def func(x, a, b):
    return x**a + b*x

a=2
b=2	
	
Result = integrate.quad(func, 0, 4,args=(a,b))

print(Result)
