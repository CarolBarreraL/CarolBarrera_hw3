import numpy as np
import matplotlib.pyplot as plt


a = -15.0
b = 15.0
h=0.1
puntos= (b-a)/(h)
c=1.0
gamma = c*(0.0005)/h
tiempo = 60
lamda = np.pi/2
#Numero de onda
k=np.pi*2/lamda
w = np.pi*2/tiempo

t = np.linspace(a,b,puntos)
#x = np.linspace(a,b,puntos)
#y = np.linspace(a,b,puntos)

amplitud = np.zeros((30, 30))
#Inicial
amplitud[10][15]= -0.5


#fi0 = np.sin(k*xv - w*t)

plt.imshow(amplitud)
plt.show()


