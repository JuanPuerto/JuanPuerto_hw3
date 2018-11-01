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
