#   Codigo que implementa la interpolacion segmentada
#   para ajustar un conjunto de datos
#
#   Naydelin Palomo Martinez

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos de ejemplo con tres comportamientos distintos
datos_x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
datos_y = np.array([0.0, -1.5, -2.8, -3.0, -2.7, -2.0])

# Interpolaciones
lineal_interp = interp1d(datos_x, datos_y, kind='linear')
cuadratica_interp = interp1d(datos_x, datos_y, kind='quadratic')
cubica_interp = interp1d(datos_x, datos_y, kind='cubic')

# Valores para graficar
x_vals = np.linspace(0, 5, 100)
y_lineal = lineal_interp(x_vals)
y_cuadratica = cuadratica_interp(x_vals)
y_cubica = cubica_interp(x_vals)

# Graficar
plt.figure(figsize=(8, 6))
plt.scatter(datos_x, datos_y, color='red', label='Datos originales')
plt.plot(x_vals, y_lineal, '--', label='Interpolación Lineal', color='blue')
plt.plot(x_vals, y_cuadratica, '-.', label='Interpolación Cuadrática', color='green')
plt.plot(x_vals, y_cubica, label='Interpolación Cúbica', color='purple')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Interpolación Segmentada: Lineal, Cuadrática y Cúbica')
plt.legend()
plt.grid()
plt.savefig('interpolacion_segmentada.png')
plt.show()
