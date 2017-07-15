import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

a = -15.0
b = 15.0
puntos= 100
h= (b-a)/(puntos)
c=1.0
gamma = c*(0.0005)/h
tiempo = 60


x = np.linspace(a,b, puntos)
y = np.linspace(a,b, puntos)

amplitud0 = np.zeros((int(puntos), int(puntos)))

#Inicial
amplitud0[int(puntos/3)][int(puntos/2)]= -0.5


fig = plt.figure()
ax = fig.gca(projection='3d')
X,Y = np.meshgrid(x,y)
surf = ax.plot_surface(X,Y, amplitud0[:], rstride=1, cstride=1, color='c')
ax.set_xlim(-15,15)
ax.set_ylim(-15,15)
ax.set_zlim(-2,0)

plt.show()









