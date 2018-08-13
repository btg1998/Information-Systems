# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 19:51:27 2017

@author: bharg
"""

from mpl_toolkits.mplot3d import Axes3D


from matplotlib import cm


from matplotlib.ticker import LinearLocator, FormatStrFormatter


import matplotlib.pyplot as plt


from scipy import special


import numpy as np

fig = plt.figure()


ax = fig.gca(projection='3d')


X = np.arange(-5, 5, 0.25)


Y = np.arange(-5, 5, 0.25)


X, Y = np.meshgrid(X, Y)


R = np.sqrt(X**2 + Y**2)
'''
Z=special.j0(R)

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0,

antialiased=False)

ax.set_zlim(None,None)


ax.zaxis.set_major_locator(LinearLocator(10))


ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))




fig.colorbar(surf, shrink=0.5, aspect=5)


plt.show()
'''
#########################

Z=special.struve(0,R)

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0,

antialiased=False)


ax.set_zlim(None,None)


ax.zaxis.set_major_locator(LinearLocator(10))


ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))




fig.colorbar(surf, shrink=0.5, aspect=5)


plt.show()

#############################
'''
Z=special.modstruve(6,R)

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0,

antialiased=False)


ax.set_zlim(None,None)


ax.zaxis.set_major_locator(LinearLocator(10))


ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))




fig.colorbar(surf, shrink=0.5, aspect=5)


plt.show()
'''
################################
'''
Z=special.pbdv(0,R)
Z=Z[0]

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0,

antialiased=False)



ax.set_zlim(None,None)


ax.zaxis.set_major_locator(LinearLocator(10))


ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))




fig.colorbar(surf, shrink=0.5, aspect=5)


plt.show()
'''
#############################
