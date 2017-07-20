import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib import cm

datos = np.genfromtxt('datos.csv', delimiter=',')

Posicionesx = datos[:,0]
Posicionesy = datos[:,1]
Posicionesz = datos[:,2]
tiempoT =  len(Posicionesx)
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


for i in range(0,10):
	for j in range(0,tiempoPlanetas):
		posicion = int(i + j*10)
		matrizPosicionesx[i][j]= Posicionesx[posicion]
		matrizPosicionesy[i][j]= Posicionesy[posicion]
		matrizPosicionesz[i][j]= Posicionesz[posicion]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
linea = ax.plot(matrizPosicionesx[Sol],matrizPosicionesy[Sol], matrizPosicionesz[Sol], 'y')
linea = ax.plot(matrizPosicionesx[Merc],matrizPosicionesy[Merc], matrizPosicionesz[Merc])
linea = ax.plot(matrizPosicionesx[Ven],matrizPosicionesy[Ven], matrizPosicionesz[Ven])
linea = ax.plot(matrizPosicionesx[Tierra],matrizPosicionesy[Tierra], matrizPosicionesz[Tierra], 'c')
linea = ax.plot(matrizPosicionesx[Marte],matrizPosicionesy[Marte], matrizPosicionesz[Marte], 'r')
linea = ax.plot(matrizPosicionesx[Jup],matrizPosicionesy[Jup], matrizPosicionesz[Jup])
linea = ax.plot(matrizPosicionesx[Sat],matrizPosicionesy[Sat], matrizPosicionesz[Sat])
linea = ax.plot(matrizPosicionesx[Uran],matrizPosicionesy[Uran], matrizPosicionesz[Uran], 'b')
linea = ax.plot(matrizPosicionesx[Nept],matrizPosicionesy[Nept], matrizPosicionesz[Nept])
linea = ax.plot(matrizPosicionesx[Pluto],matrizPosicionesy[Pluto], matrizPosicionesz[Pluto], 'k')


ax.set_xlabel('Unidades Astronomicas (UA)')
plt.title('Sistema Solar')
#plt.show()
plt.savefig('sistemaSolar.pdf')
plt.close()

















	
