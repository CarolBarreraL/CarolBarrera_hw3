import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
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

plutox = matrizPosicionesx[9]
plutoy = matrizPosicionesy[9]
plutoz = matrizPosicionesz[9]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
linea, = ax.plot(plutox,plutoy,plutoz, label = 'Pluto')
ax.legend()
#linea = ax.plot(matrizPosicionesx[Sol],matrizPosicionesy[Sol], matrizPosicionesz[Sol], 'y')
#linea = ax.plot(matrizPosicionesx[Merc],matrizPosicionesy[Merc], matrizPosicionesz[Merc])
#linea = ax.plot(matrizPosicionesx[Ven],matrizPosicionesy[Ven], matrizPosicionesz[Ven])
#linea = ax.plot(matrizPosicionesx[Tierra],matrizPosicionesy[Tierra], matrizPosicionesz[Tierra], 'c')
#linea = ax.plot(matrizPosicionesx[Marte],matrizPosicionesy[Marte], matrizPosicionesz[Marte], 'r')
#linea = ax.plot(matrizPosicionesx[Jup],matrizPosicionesy[Jup], matrizPosicionesz[Jup])
#linea = ax.plot(matrizPosicionesx[Sat],matrizPosicionesy[Sat], matrizPosicionesz[Sat])
#linea = ax.plot(matrizPosicionesx[Uran],matrizPosicionesy[Uran], matrizPosicionesz[Uran], 'b')
#linea = ax.plot(matrizPosicionesx[Nept],matrizPosicionesy[Nept], matrizPosicionesz[Nept])
#linea = ax.plot(matrizPosicionesx[Pluto],matrizPosicionesy[Pluto], matrizPosicionesz[Pluto], 'k')


ax.set_xlabel('Unidades Astronomicas (UA)')
plt.title('Sistema Solar')

sim = []
def animar(i):

	x = plutox[i]
	y = plutoy[i]
	z = plutoz[i]
	linea = ax.scatter(x,y,z)
	return linea,


anim = animation.FuncAnimation(fig, animar, interval =30, blit=False)

plt.show()

#anim.save('sistemaSolar.mp4', fps=10)
#plt.close()


#for i in range(26000):
#	im = plt.plot(matrizPosicionesx[Pluto],matrizPosicionesy[Pluto], matrizPosicionesz[Pluto])
#	sim.append([im])

#anim = animation.ArtistAnimation(fig, sim, interval =80, blit = True, repeat=False)
#plt.show()













	
