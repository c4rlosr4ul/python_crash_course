
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

# Definición de constantes
pi = np.pi  # Uso de np.pi para obtener el valor de π
m = 1
E = 1
h_bar = 1
V_0 = 1

# Cálculo de variables
p = np.sqrt(2 * m * E / h_bar)
q = np.sqrt(2 * m * (V_0 - E) / h_bar)
xi = np.array([1, (p / q)])

# Corrección en la definición de la matriz, uso de np.exp para operaciones con NumPy
vector_or_matrix = np.array([[np.exp(1), np.exp(2)],  # Asumiendo que a=1, b=2 para el ejemplo
                             [np.exp(3), np.exp(4)]])  # Asumiendo que c=3, d=4 para el ejemplo

# Definición de funciones
def T(x):
    return np.sqrt(x)

def check_condition(x):
    return x + 1 

# Uso de funciones trigonométricas de np para operaciones con arrays
angle = pi / 4
sin_value = np.sin(angle)
sinh_value = np.sinh(1)  # Uso de 1 directamente

# Bucle corregido
x = 1
while x < 100:
    print(x)
    x = check_condition(x)  # Actualización de x basada en la condición

# Gráfica bidimensional
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()

# Gráfica tridimensional
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter([1, 2, 3], [4, 5, 6], [7, 8, 9])  # Gráfica tridimensional simple
plt.show()

