import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib import cm

datos = np.genfromtxt('datos.csv', delimiter=',')

Posicionesx = datos[:,0]
Posicionesy = datos[:,1]
Posicionesz = datos[:,2]
tiempoT =  3120
tiempoPlanetas = tiempoT/10

Sol = 0
Merc = 1
Ven = 2
Tierra = 3
Marte = 4
Jup = 5
Sat = 6
Uran = 7
Nept = 8
Pluto = 9

matrizPosicionesx = np.zeros((10,tiempoPlanetas))
matrizPosicionesy = np.zeros((10,tiempoPlanetas))
matrizPosicionesz = np.zeros((10,tiempoPlanetas))


for i in range(10):
	for j in range(tiempoPlanetas):
		posicion = i + j*10
		matrizPosicionesx[i][j]= Posicionesx[posicion]
		matrizPosicionesy[i][j]= Posicionesy[posicion]
		matrizPosicionesz[i][j]= Posicionesz[posicion]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
linea = ax.plot(matrizPosicionesx[Tierra],matrizPosicionesy[Tierra], matrizPosicionesz[Tierra])
#fig.colorbar(linea, shrink =0.5, aspect = 5)
#ax.set_xlim(-15,15)
#ax.set_ylim(15,-15)
#ax.set_zlim(-2,1)
plt.show()
plt.close()
	









	
