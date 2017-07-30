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

Solx = matrizPosicionesx[0]
Soly = matrizPosicionesy[0]
Solz = matrizPosicionesz[0]

mercx = matrizPosicionesx[1]
mercy = matrizPosicionesy[1]
mercz = matrizPosicionesz[1]

venusx = matrizPosicionesx[2]
venusy = matrizPosicionesy[2]
venusz = matrizPosicionesz[2]

tierrax = matrizPosicionesx[3]
tierray = matrizPosicionesy[3]
tierraz = matrizPosicionesz[3]

martex = matrizPosicionesx[4]
martey = matrizPosicionesy[4]
martez = matrizPosicionesz[4]

jupx = matrizPosicionesx[5]
jupy = matrizPosicionesy[5]
jupz = matrizPosicionesz[5]

satx = matrizPosicionesx[6]
saty = matrizPosicionesy[6]
satz = matrizPosicionesz[6]

uranox = matrizPosicionesx[7]
uranoy = matrizPosicionesy[7]
uranoz = matrizPosicionesz[7]

nepx = matrizPosicionesx[8]
nepy = matrizPosicionesy[8]
nepz = matrizPosicionesz[8]

plutox = matrizPosicionesx[9]
plutoy = matrizPosicionesy[9]
plutoz = matrizPosicionesz[9]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



ax.set_xlabel('Unidades Astronomicas (UA)')
plt.title('Sistema Solar')


def animar(i):
	
	ax.clear()

	linea = ax.scatter(Solx[i],Soly[i],Solz[i])
	ax.plot(Solx,Soly,Solz, label = 'Sol')

	linea = ax.scatter(mercx[i],mercy[i],mercz[i])
	ax.plot(mercx,mercy,mercz, label = 'Mercurio')

	linea = ax.scatter(venusx[i],venusy[i],venusz[i])
	ax.plot(venusx,venusy,venusz, label = 'Venus')

	linea = ax.scatter(tierrax[i],tierray[i],tierraz[i])
	ax.plot(tierrax,tierray,tierraz, label = 'Tierra')

	linea = ax.scatter(martex[i],martey[i],martez[i])
	ax.plot(martex,martey,martez, label = 'Marte')

	linea = ax.scatter(jupx[i],jupy[i],jupz[i])
	ax.plot(jupx,jupy,jupz, label = 'Jupiter')

	linea = ax.scatter(satx[i],saty[i],satz[i])
	ax.plot(satx,saty,satz, label = 'Saturno')

	linea = ax.scatter(uranox[i],uranoy[i],uranoz[i])
	ax.plot(uranox,uranoy,uranoz, label = 'Urano')

	linea = ax.scatter(nepx[i],nepy[i],nepz[i])
	ax.plot(nepx,nepy,nepz, label = 'Neptuno')
	
	linea = ax.scatter(plutox[i],plutoy[i],plutoz[i])
	ax.plot(plutox,plutoy,plutoz, label = 'Pluto')

	ax.set_xlabel('Unidades Astronomicas (UA)')
	plt.title('Sistema Solar')
	ax.legend()
	
	return linea,


anim = animation.FuncAnimation(fig, animar, interval =5)

plt.show()

#plt.close()

#sim = []
#for i in range(26000):
#	x = plutox[i]
#	y = plutoy[i]
#	z = plutoz[i]
#	im = ax.scatter(x,y,z)
#	sim.append(im)

#anim = animation.ArtistAnimation(fig, sim, interval =80, blit = True, repeat=False)
#plt.show()













	
