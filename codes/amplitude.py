import numpy as np
import matplotlib.pyplot as plt

# Definición de constantes y parámetros
m = 1.0  # Masa
h_bar = 1.0  # Constante reducida de Planck
V_0 = 10.0  # Potencial
E = 5.0  # Energía
a = 1.0  # Comienzo de la barrera
b = 2.0  # Fin de la barrera
N = 100.0  # Extensión de la normalización

# Definición de p y q
p = np.sqrt(2 * m * E) / h_bar
q = np.sqrt(2 * m * (V_0 - E)) / h_bar

# Definición de xi y eta
xi = q/p - p/q
eta = q/p + p/q

# Definición de las funciones seno y coseno hiperbólicos
def sh(x):
    return np.sinh(x)

def ch(x):
    return np.cosh(x)

# Funciones auxiliares
cd = np.cosh(q * (b - a))
sd = np.sinh(q * (b - a))

# Cálculo de A_3 A_3*
A3_squared_inv = (
    (a + N) * (cd**2) + ((xi**2 + eta**2) / 4) * (sd**2) -
    (eta / (2 * p)) * sd * (2 * cd * (np.sin(2 * p * (N + a)) - xi * sd * (1 - np.cos(2 * p * (N + a))))) +
    ((1 + (p**2) / (q**2)) * (np.sinh(2 * (q * b - p)) - np.cosh(2 * (q * a - p))) / (2 * q)) +
    (b - a) * ((1 - (p**2) / (q**2)) * (np.cos(2 * p * b) / 2) - (2 * p / q) * (np.sin(p * b) / 2)) + (N - b)
)**-1

# Cálculo de |A_3|
A3 = np.sqrt(A3_squared_inv)
# Definición de las funciones de onda
def psi_1(x):
    return ((ch(q * (b - a)) + 1j * xi / 2 * sh(q * (b - a))) * np.exp(1j * p * (b - a)) * np.exp(1j * p * x) -
            1j * eta / 2 * sh(q * (b - a)) * np.exp(1j * p * (b + a)) * np.exp(-1j * p * x)) * A3

def psi_2(x):
    return ((0.5 * np.exp(q * b) * (1 - 1j * p / q) * np.exp(-1j * p * b) * np.exp(-q * x) +
             0.5 * np.exp(-q * b) * (1 + 1j * p / q) * np.exp(1j * p * b) * np.exp(q * x)) * A3)

def psi_3(x):
    return A3 * np.exp(1j * p * x)

# Generación de los valores de x y cálculo de psi para cada región
x_values = np.linspace(-15, 15, 1000)
psi_values = np.piecewise(x_values, [x_values < a, (x_values >= a) & (x_values <= b), x_values > b],
                          [lambda x: psi_1(x), lambda x: psi_2(x), lambda x: psi_3(x)])

# Graficar la función de onda
plt.plot(x_values, psi_values.real, label='Parte Real')
plt.plot(x_values, psi_values.imag, label='Parte imaginaria')
plt.xlabel('x')
plt.ylabel('psi(x)')
plt.title(f"Función de Onda: $m = {m}$, $\hbar = {h_bar}$, $V_0 = {V_0}$, $E = {E}$\n"
    f"$a = {a}$, $b = {b}$, $N = {N}$")
plt.legend()
plt.grid(True)
# Guardar el gráfico en formato PDF en alta calidad
plt.savefig('funcion_de_onda.pdf', format='pdf', dpi=300, bbox_inches='tight')

# Mostrar el gráfico
plt.show()
