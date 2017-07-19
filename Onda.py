import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib import cm

a =0
b =30.0
puntos= 60
dx = (b-a)/(puntos-1)
dy = (b-a)/(puntos-1)
c=1.0
r = 0.5
dt = np.sqrt(r)*dx/c
tiempo = 60
iteraciones = 60/dt

x = np.linspace(a,b, puntos)
y = np.linspace(a,b, puntos)


#Matriz con ampitudes
amplitud0 = np.zeros((puntos, puntos))


#Perturbacion inicial y condiciones iniciales
#amplitud0[int((b-a)/3)][int((b-a)/2)]= -0.5
amplitud0[puntos/3][puntos/2]= -0.5

#En los bordes
amplitud0[0,:]=0
amplitud0[:,0]=0
amplitud0[-1,:]=0
amplitud0[:,-1]=0
#Rendija
hueco = 3
amplitud0[(puntos/3)*2][:(puntos/2)-hueco]= 0
amplitud0[(puntos/3)*2][(puntos/2)+hueco:]= 0

AInicial = np.copy(amplitud0)


amplitud1 = np.zeros((puntos, puntos))
#Condicion inicial
amplitud1[puntos/3][puntos/2]= -0.5
amplitud1[0,:]=0
amplitud1[:,0]=0
amplitud1[-1,:]=0
amplitud1[:,-1]=0
#Rendija
amplitud1[(puntos/3)*2][:(puntos/2)-hueco]= 0
amplitud1[(puntos/3)*2][(puntos/2)+hueco:]= 0

#i es 1:-1
#i+1 es 2:
#i-1 es 0:-2
for i in range(1,puntos-1):
	for j in range(1,puntos-1):
		amplitud1[i,j]= amplitud0[i,j]+ r*r/2*(amplitud0[i+1,j]-2*amplitud0[i,j]+amplitud0[i-1,j]) + r*r/2*(amplitud0[i,j+1]-2*amplitud0[i,j]+amplitud0[i, j-1]) 

amplitud0[0,:]=0
amplitud0[:,0]=0
amplitud0[-1,:]=0
amplitud0[:,-1]=0



amplitudFinal = np.zeros((puntos,puntos))


AinTime=[]
t=0
AinTime.append(amplitud0)
AinTime.append(amplitud1)
while t<int(iteraciones):
	for i in range(1,puntos-1):
		for j in range(1,puntos-1):
			amplitudFinal[i,j]=2*amplitud1[i,j]-amplitud0[i,j]+r*(amplitud1[i+1,j]-2*amplitud1[i,j]+amplitud1[i-1,j])+r*(amplitud1[i,j+1]-2*amplitud1[i,j]+amplitud1[i,j-1])
	#Condiciones de frontera
	amplitudFinal[0,:]=0
	amplitudFinal[:,0]=0
	amplitudFinal[-1,:]=0
	amplitudFinal[:,-1]=0
	
	#Rendija
	amplitudFinal[(puntos/3)*2][:(puntos/2)-hueco]= 0
	amplitudFinal[(puntos/3)*2][(puntos/2)+hueco:]= 0

	#Evolucion
	amplitud0 = np.copy(amplitud1)
	amplitud1 = np.copy(amplitudFinal)
	AinTime.append(amplitud1)
	t+=1

itPara30 = 30/dt


fig = plt.figure()
#ax = fig.gca(projection='3d')
X,Y = np.meshgrid(x,y)
ax = fig.add_subplot(111, projection='3d')
linea = ax.plot_surface(X,Y, AinTime[25],rstride=1, cstride=1, color='c', cmap = cm.coolwarm)
fig.colorbar(linea, shrink =0.5, aspect = 5)
#ax.set_xlim(-15,15)
#ax.set_ylim(15,-15)
ax.set_zlim(-2,1)
plt.show()
plt.close()

plt.imshow(AinTime[25])
plt.colorbar()
plt.show()
plt.close()


def anima(i):
	amplitud = AinTime[i]
	ax.clear()	
	linea = ax.plot_surface(X,Y,amplitud, cmap = cm.coolwarm)
	#linea = plt.imshow(amplitud)
	ax.set_zlim(-2,1)
	return linea,

#anim = animation.FuncAnimation(fig, anima, int(iteraciones), interval=25, blit=False)
#anim.save('Onda.mp4', fps = 20)



