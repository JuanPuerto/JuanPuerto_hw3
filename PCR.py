import numpy as np
import matplotlib.pyplot as plt

cancer = np.genfromtxt('WDBC.dat', delimiter = ',', dtype = 'U16') # Almacena los datos del archivo WDBC.dat en la variable: cancer

util = cancer[:,2:].astype(float) # Matriz con los parametros numericos

letras = cancer[:,:2] # Matriz con el ID y la columna de Maligno/Benigno

def matriz_cov(archivo): # Matriz de covarianza par un archivo
	dim = np.shape(archivo)[1]	# La dimension de la matriz de covarianza es el numero de columnas del archivo
	puntos = np.shape(archivo)[0]  # Los puntos de la matriz de covarianza son el numero de filas del archivo
	covarianza = np.zeros([dim,dim]) # Genera una matriz de ceros con las dimensiones establecidas
	
	for i in range(dim):
		for j in range(dim):
			promedio_i = np.mean(archivo[:,i]) # Calcula el promedio de los primeros valores
			promedio_j = np.mean(archivo[:,j]) # Calcula el promedio de los segundos valorea
			covarianza[i,j] = np.sum((archivo[:,i]-promedio_i)*(archivo[:,j]-promedio_j))/(puntos-1) # Rellena la matriz de covarianza con los valores dados por la ecuacion de covarianza
	
	return covarianza 
	
covarianza_cancer = matriz_cov(util) # Matriz de covarianza para los datos del archivo WDBC.dat

print("Matriz de covarianza: ","\n",covarianza_cancer) # Imprime matriz de covarianza

eig_val, eig_vec = np.linalg.eig(covarianza_cancer) # Eigenvalores y eigenvectores de la matriz de covarianza

col = np.shape(eig_vec)[1] # Halla el numero de columnas de la matriz de eigenvectores

for i in range(col): # Para imprimir los eigenvalores en orden con sus correspondientes eigenvectores
	print('Eigenvalor',i+1,':',eig_val[i]) # Imprime el eigenvalor ordenado
	print('Eigenvector',i+1,':',eig_vec[:,i]) # Imprime el eigenvector correspondiente al anterior eigenvalor
