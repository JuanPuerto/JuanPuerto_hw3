import numpy as np
import matplotlib.pyplot as plt

signal = np.genfromtxt('signal.dat', delimiter = ',') # Almacena los datos del archivo signal.dat en la variable: signal
incompletos = np.genfromtxt('incompletos.dat', delimiter = ',') # Almacena los datos del archivo incompletos.dat en la variable: incompletos

x = signal[:,0] # Para signal
y = signal[:,1] # Para signal

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

def frec_prin(f): # Devuelve las frecuencias principales
	lista1=[]
	for i in range(len(f)):
		if fourier[i]>0.4:
			lista1.append(f[i])
	return lista1
	
print('Las frecuencias principales son: \n',frec_prin(frecuencias)) # Imprime las frecuencias principales

def pasa_bajos(archivo, frecuencias, c = 1000): # Filtro pasa bajos para frecuencia de corte de 1000Hz
	filtro = archivo.copy()
	filtro[frecuencias > c] = 0 # Frecuencias mayores a 1000Hz las vuelve cero
	return filtro
	
bajos = pasa_bajos(frecuencias, fourier2)

inversa = np.fft.ifft(bajos[1]) # Transformada inversa usando paquetes de numpy

xsevero = np.linspace(min(x),max(x),len(inversa))

plt.figure()
plt.plot(x,inversa) # Grafica transformada inversa de Fourier
plt.xlabel('Tiempo')
plt.ylabel('y')
plt.title("Transformada Inversa de Fourier")
plt.savefig('PuertoJuan_filtrada.pdf')

x_crack = incompletos[:,0] # Para incompletos
y_crack = incompletos[:,1] # Para incompletos

print("Se puede realizar la transformada de Fourier a incompletos.dat, pero la informacion obtenida de esta no es correcta, porque los datos no poseen el mismo delta de tiempo. ")
