import numpy as np
import matplotlib.pyplot as plt

signal = np.genfromtxt('signal.dat', delimiter = ',') # Almacena los datos del archivo signal.dat en la variable: signal
incompletos = np.genfromtxt('incompletos.dat', delimiter = ',') # Almacena los datos del archivo incompletos.dat en la variable: incompletos

x = signal[:,0]
y = signal[:,1]

plt.figure()
plt.plot(x,y]) # Grafica datos signal
plt.xlabel('x') # Nombre eje x
plt.ylabel('y') # Nombre eje y
#plt.savefig('PuertoJuan_signal.pdf') # Guarda la grafica en PuertoJuan_signal.pdf

def fourier(archivo):
	n = len(archivo)
	m = np.linspace(0,n)
	for k in range(transformada.shape[0]):
		transformada[k] = np.sum((archivo*np.exp(-1j*2*np.pi*((k*m)/n))))
	return transformada

fourier = fourier(signal)
frecuencias = np.fft.fftfreq(signal.shape[0], d=2.0)

plt.figure()
plt.plot(frecuencias,fourier)
plt.show()

def pasa_bajos(archivo, frecuencias, c = 1000): # Filtro pasa bajos para frecuencia de corte de 1000Hz
    filtro = archivo.copy()
    filtro[frecuencias > c] = 0 # Frecuencias mayores a 1000Hz las vuelve cero
return filtro
