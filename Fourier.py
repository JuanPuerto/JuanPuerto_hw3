import numpy as np
import matplotlib.pyplot as plt

signal = np.genfromtxt('signal.dat', delimiter = ',') # Almacena los datos del archivo signal.dat en la variable: signal
incompletos = np.genfromtxt('incompletos.dat', delimiter = ',') # Almacena los datos del archivo incompletos.dat en la variable: incompletos

x = signal[:,0]
y = signal[:,1]

plt.figure()
plt.plot(x,y) # Grafica datos signal
plt.xlabel('Tiempo') 
plt.ylabel('y') 
plt.title("Signal") 
plt.savefig('PuertoJuan_signal.pdf') 

def fourier(x,y): # Transformada de Fourier
	n = len(x)
	m = len(y)
	transformada = np.linspace(0,0,n)
	for k in range(n):
		for m in range(m)
			transformada[k] += (y[m]*np.exp(-1j*2*np.pi*((k*m)/n))))
	transformada=transformada/n
	return transformada

d=x[1]-x[0] # Espaciado de las muestras en el tiempo

fourier = abs(fourier(x,y)) # Valores positivos de Fourier aplicado a los datos 
fourier2 = fourier(x,y)	# Fourier aplicado a los datos 
frecuencias = np.fft.fftfreq(len(x), d) # Frecuencias de Fourier de los datos

plt.figure()
plt.plot(frecuencias,fourier) # Grafica transformada de Fourier
plt.xlabel('Frecuencia')
plt.ylabel('Transformada de Fourier')
plt.title("Transformada Discreta de Fourier")
plt.savefig('PuertoJuan_TF.pdf')

def pasa_bajos(archivo, frecuencias, c = 1000): # Filtro pasa bajos para frecuencia de corte de 1000Hz
	filtro = archivo.copy()
	filtro[frecuencias > c] = 0 # Frecuencias mayores a 1000Hz las vuelve cero
	return filtro
