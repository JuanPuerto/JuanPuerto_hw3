import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from matplotlib.colors import LogNorm

arboles = plt.imread('Arboles.png').astype(float) # Lee la imagen de formato PNG y la transforma en un array de tipo float

arboles_fft = fftpack.fft2(arboles) # Transformada de Fourier

plt.figure()
plt.imshow(np.abs(arboles_fft) # Grafica transformada de Fourier
plt.colorbar()
plt.title('Transformada de Fourier')
plt.savefig('PuertoJuan_FT2D.pdf')

fraccion = 0.1
arboles_fft2 = arboles_fft.copy()
a,b = arboles_fft2.shape
aboles_fft2[int(a*fraccion):int(a*(1-fraccion))] = 0
arboles_fft2[:, int(b*fraccion):int(b*(1-fraccion))] = 0

plt.figure()
plt.imshow(np.abs(arboles_fft2), norm=LogNorm(vmin=5)) # Grafica filtro de ruido
plt.colorbar()
plt.title('Transformada de Fourier Filtrada')
plt.savefig('PuertoJuan_FT2D_filtrada.pdf')

arboles_filtrado = fftpack.ifft2(arboles_fft2).real

plt.figure()
plt.imshow(arboles_filtrado, plt.cm.gray) # Grafica  Imagen Reconstruida
plt.title('Imagen Reconstruida')
plt.savefig('PuertoJuan_Imagen_filtrada.pdf')
