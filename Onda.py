import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib import cm

a = -15.0
b = 15.0
puntos= 30
dx = (b-a)/(puntos)
dy = (b-a)/(puntos)
c=1.0
rx = c*(0.5)/dx
ry = c*(0.5)/dy
tiempo = 60


x = np.linspace(a,b, puntos)
y = np.linspace(a,b, puntos)




#Matriz con ampitudes
amplitud0 = np.zeros((puntos, puntos))


#Perturbacion inicial y condiciones iniciales
amplitud0[int((b-a)/3),int((b-a)/2)]= -0.5
#En los bordes
amplitud0[0,:]=0
amplitud0[:,0]=0
amplitud0[-1,:]=0
amplitud0[:,-1]=0
AInicial = np.copy(amplitud0)


amplitud1 = np.zeros((puntos, puntos))
#Condicion inicial
amplitud1[int((b-a)/3),int((b-a)/2)]= -0.5

#i es 1:-1
#i+1 es 2:
#i-1 es 0:-2
for i in range(tiempo+1):
	amplitud1[1:-1,1:-1]= 2*amplitud0[1:-1,1:-1]+ rx*rx/2*(amplitud0[2:,1:-1]-2*amplitud0[1:-1,1:-1]+amplitud0[0:-2,1:-1]) + ry*ry/2*(amplitud0[1:-1,2:]-2*amplitud0[1:-1,1:-1]+amplitud0[1:-1, 0:-2]) 

	amplitud0[0,:]=0
	amplitud0[:,0]=0
	amplitud0[-1,:]=0
	amplitud0[:,-1]=0



amplitudFinal = np.zeros((puntos,puntos))


AinTime=[]
time=[]
t=0
AinTime.append(amplitud0)
AinTime.append(amplitud1)
#while t<tiempo:
#	time.append(t)
#	for i in range(tiempo+1):
#		amplitudFinal[1:-1,1:-1]=2*(1-rx*rx)*amplitud1[1:-1,1:-1]-amplitud0[1:-1,1:-1]+rx*rx*(amplitud1[2:,1:-1]+amplitud1[0:-2,1:-1]) + 2*(1-ry*ry)*amplitud1[1:-1,1:-1]-amplitud0[1:-1,1:-1]+ry*ry*(amplitud1[1:-1,2:]+amplitud1[1:-1,0:-2])
	
#	amplitudFinal[0,:]=0
#	amplitudFinal[:,0]=0
#	amplitudFinal[-1,:]=0
#	amplitudFinal[:,-1]=0
	
#	amplitud0 = np.copy(amplitud1)
#	amplitud1 = np.copy(amplitudFinal)
#	AinTime.append(amplitudFinal)
#	t+=1

#Intento de otra manera
while t<tiempo:
	time.append(t)
	for i in range(1,puntos-1):
		amplitudFinal[i,i]=2*(1-rx*rx)*amplitud1[i,i]-amplitud0[i,i]+rx*rx*(amplitud1[i+1,i]+amplitud1[i-1,i]) + 2*(1-ry*ry)*amplitud1[i,i]-amplitud0[i,i]+ry*ry*(amplitud1[i,i+1]+amplitud1[i,i-1])
	
	amplitudFinal[0,:]=0
	amplitudFinal[:,0]=0
	amplitudFinal[-1,:]=0
	amplitudFinal[:,-1]=0
	
	amplitud0 = np.copy(amplitud1)
	amplitud1 = np.copy(amplitudFinal)
	AinTime.append(amplitudFinal)
	t+=1


fig = plt.figure()
ax = fig.gca(projection='3d')
X,Y = np.meshgrid(x,y)
surf = ax.plot_surface(X,Y, AinTime[2], color='c', cmap = cm.coolwarm)
fig.colorbar(surf, shrink =0.5, aspect = 5)
ax.set_xlim(-15,15)
ax.set_ylim(15,-15)
ax.set_zlim(-1,0)
plt.show()

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#linea = ax.plot_surface(X,Y, AinTime[10], color='c', cmap = cm.coolwarm)
#ax.set_xlim(-15,15)
#ax.set_ylim(15,-15)
#ax.set_zlim(-2,1)

#def anima(i):
#	amplitud = AinTime[i]
#	ax.clear()	
#	linea = ax.plot_surface(X,Y,amplitud, cmap = cm.coolwarm)
#	ax.set_zlim(-2,1)
#	return linea,

#anim = animation.FuncAnimation(fig, anima, tiempo, fargs=(0,1,1.05), interval=25, blit=False)
#anim.save('Onda.mp4', fps = 10)



