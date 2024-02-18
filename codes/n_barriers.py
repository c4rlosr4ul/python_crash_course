
import numpy as np
import matplotlib.pyplot as plt

# Definición de constantes y parámetros
b = 2  # Separación entre barreras
a = 1  # Anchura de cada barrera
N = 3  # Número de barreras
V0 = 5.0  # Altura de las barreras
m = 1.0  # Masa de la partícula
h_bar = 1.0  # Constante reducida de Planck

# Inicialización de arrays para las posiciones x y los potenciales V
x = np.zeros(2 * N)
V = np.zeros(2 * N + 1)

# Configuración de las posiciones de las fronteras entre las regiones
x[0] = -N * (a + b) / 2 + b / 2
for i in range(1, 2 * N, 2):
    x[i] = x[i - 1] + a
    if i + 1 < 2 * N:
        x[i + 1] = x[i] + b

# Configuración de los potenciales en cada región
for i in range(0, 2 * N + 1, 2):
    V[i] = 0.0  # Regiones fuera de las barreras
    if i < 2 * N:
        V[i + 1] = V0  # Regiones de las barreras

# Función para calcular las matrices de condiciones de frontera
def f(z, q):
    return np.array([[np.exp(1j * q * z), np.exp(-1j * q * z)], [q * np.exp(1j * q * z), -q * np.exp(-1j * q * z)]])

# Función para calcular las matrices inversas necesarias para las condiciones de frontera
def g(z, q):
    if np.isclose(q, 0):
        return np.array([[1, 0], [0, 1]])  # Matriz identidad como caso límite
    else:
        return np.array([[np.exp(-1j * q * z), np.exp(-1j * q * z) / q], [np.exp(1j * q * z), -np.exp(1j * q * z) / q]]) / 2

# Rango de energías para calcular el coeficiente de transmisión
E = np.linspace(0, V0, 200)

# Array para almacenar los valores del coeficiente de transmisión
trans = np.zeros(len(E))

# Cálculo del coeficiente de transmisión para cada energía
for j, energy in enumerate(E):
    q_values = np.sqrt(2 * m * (energy - V) + 0j) / h_bar  # Asegura cálculo en dominio complejo
    A = np.array([1, 0])  # Inicializa la amplitud para la primera región
    
    # Aplica las condiciones de frontera para cada región
    for i in range(2 * N - 1, -1, -1):
        A = g(x[i], q_values[i]) @ f(x[i], q_values[i + 1]) @ A

    # Calcula el coeficiente de transmisión
    trans[j] = 1 / abs(A[0])**2

# Graficación del coeficiente de transmisión en función de la energía
plt.plot(E, trans)
plt.grid(True)
plt.ylim([0, 1.1])
plt.xlabel('Energía (E)')
plt.ylabel('Coeficiente de transmisión ($T_r$)')
plt.title('Coeficiente de transmisión vs Energía para $N=2$ barreras')
plt.savefig('transmision_vs_energia_corregido.pdf', format='pdf', bbox_inches='tight', dpi=300)  # Guarda la gráfica en alta calidad
plt.show()

