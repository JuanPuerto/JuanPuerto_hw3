import numpy as np
import matplotlib.pyplot as plt

signal = np.genfromtxt('signal.dat', delimiter = ',') # Almacena los datos del archivo signal.dat en la variable: signal
incompletos = np.genfromtxt('incompletos.dat', delimiter = ',') # Almacena los datos del archivo incompletos.dat en la variable: incompletos

plt.plot(signal[:,0],signal[:,1]) # Grafica datos signal
plt.xlabel('x') # Nombre eje x
plt.ylabel('y') # Nombre eje y
plt.savefig('PuertoJuan_signal.pdf') # Guarda la grafica en PuertoJuan_signal.pdf
