
import numpy as np
import matplotlib.pyplot as plt

# Constantes
m = 1.0
h_bar = 1.0
V_0 = 1.0
b = 1.0  # Ancho de la barrera

# Funciones auxiliares p y q
def p(E):
    return np.sqrt(2 * m * E) / h_bar

def q(E):
    return np.sqrt(2 * m * (V_0 - E)) / h_bar

# Función xi
def xi(E):
    return q(E) / p(E) - p(E) / q(E)

# Función T corregida
def T(E):
    exp_term = np.exp(b * q(E))
    sin_term = np.sin(b * p(E))
    cos_term = np.cos(b * p(E))
    denominator = 0.5 * xi(E) * sin_term + cos_term

    # Para evitar divisiones por cero, devolvemos 0 si el denominador es 0
    if denominator == 0:
        return 0

    return (exp_term / denominator) ** 2

# Generación de valores de E (desde un valor muy pequeño hasta justo por debajo de V_0 para evitar problemas matemáticos)
E_values = np.linspace(0.01, V_0 - 0.01, 500)

# Cálculo de T para cada valor de E
T_values = np.array([T(E) for E in E_values])

# Creación de la gráfica
plt.plot(E_values, T_values, label='Transmitancia')
plt.xlabel('Energía (E)')
plt.ylabel('Transmitancia (T)')
plt.title('Transmitancia en función de la Energía')
plt.legend()
plt.grid(True)
plt.show()

