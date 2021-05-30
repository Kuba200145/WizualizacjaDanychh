import numpy as np
import matplotlib.pyplot as plt

#Zad1
fig= plt.figure()
ax= fig.gca(projection='3d')

z= np.linspace(0, 2*np.pi, 100)
x= np.sin(z)
y= np.cos(z)*2

ax.plot(x,y,z,label='Wykres do zad1')
ax.legend()
plt.show()
