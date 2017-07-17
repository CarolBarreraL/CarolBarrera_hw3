import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

a = -15.0
b = 15.0
puntos= 30
dx = (b-a)/(puntos)
dy = (b-a)/(puntos)
c=1.0
rx = c*(0.5)/dx
ry = c*(0.5)/dy
tiempo = 60


#x = np.linspace(a,b, puntos)
#y = np.linspace(a,b, puntos)
x = np.linspace(a,b, 30)
y = np.linspace(a,b, 30)



#Matriz con ampitudes
#amplitud0 = np.zeros((int(puntos), int(puntos)))
amplitud0 = np.zeros((30, 30))


#Inicial
#amplitud0[int(puntos/3)][int(puntos/2)]= -0.5
amplitud0[10][15]= -0.5
AInicial = np.copy(amplitud0)


amplitud1 = np.zeros((30, 30))
amplitud1[10][15]= -0.5


#i es 1:-1
#i+1 es 2:
#i-1 es 0:-2
for i in range(tiempo+1):
	amplitud1[1:-1,1:-1]= 2*amplitud0[1:-1,1:-1]+ rx*rx/2*(amplitud0[2:,1:-1]-2*amplitud0[1:-1,1:-1]+amplitud0[0:-2,1:-1]) + ry*ry/2*(amplitud0[1:-1,2:]-2*amplitud0[1:-1,1:-1]+amplitud0[1:-1, 0:-2]) 

amplitudFinal = np.zeros((30,30))


AinTime=[]
time=[]
t=0
while t<tiempo:
	time.append(t)
	#amplitud0[10][15]= -0.5*np.sin(30+np.pi*t/20.0)
	for i in range(tiempo+1):
		amplitudFinal[1:-1,1:-1]=2*(1-rx*rx)*amplitud1[1:-1,1:-1]-amplitud0[1:-1,1:-1]+rx*rx*(amplitud1[2:,1:-1]+amplitud1[0:-2,1:-1]) + 2*(1-ry*ry)*amplitud1[1:-1,1:-1]-amplitud0[1:-1,1:-1]+ry*ry*(amplitud1[1:-1,2:]+amplitud1[1:-1,0:-2])

	amplitud0 = np.copy(amplitud1)
	amplitud1 = np.copy(amplitudFinal)
	AinTime.append(amplitudFinal)
	t+=1

fig = plt.figure()
ax = fig.gca(projection='3d')
X,Y = np.meshgrid(x,y)
surf = ax.plot_surface(X,Y, amplitudFinal, rstride=1, cstride=1, color='c')
ax.set_xlim(-15,15)
ax.set_ylim(15,-15)
ax.set_zlim(-2,0)
plt.show()

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#linea, = ax.plot([],[],[], label='Onda', lw=0.5)
#ax.set_xlim(-15,15)
#ax.set_ylim(15,-15)
#ax.set_zlim(-2,0)

#def anima():
#	linea.set_data(x,y)
#	linea.set_3d_properties(amplitudFinal)
#	return linea,

#anim = animation.FuncAnimation(fig, anima, frames=500, fargs=(0,1,1.05), interval=5, blit=True)
#anim.save('Onda.mp4', fps = 10)



