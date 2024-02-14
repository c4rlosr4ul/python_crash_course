import numpy as np
import matplotlib.pyplot as plt

# Constantes
m = 1.0
h_bar = 1.0
V_0 = 1.0
a = 1.0; b = 2.0  # Ancho de la barrera (b - a)

def p(E):
    """Momentum asociado a la energía E."""
    return np.sqrt(2 * m * E) / h_bar

def q(E, mode='less'):
    """Función de onda en la región de potencial no nulo."""
    if mode == 'less':
        return np.sqrt(2 * m * (V_0 - E)) / h_bar
    elif mode == 'greater':
        return np.sqrt(2 * m * (E - V_0)) / h_bar

def xi(E):
    """Parámetro adimensional xi."""
    return q(E) / p(E) - p(E) / q(E)

def T(E, mode='less'):
    """Coeficiente de transmitancia."""
    if mode == 'less':
        denominator = 1 + (1 + 0.25 * xi(E) ** 2) * (np.sinh(q(E)) ** 2)
    elif mode == 'greater':
        eta = q(E, mode='greater') / p(E) + p(E) / q(E, mode='greater')
        denominator = 1 + (eta ** 2 / 4 - 1) * np.sin(q(E, mode='greater') * (b - a))
    
    return 0 if denominator == 0 else (1 / denominator)

def plot_transmitance(E_range, mode='less'):
    """Genera y guarda la gráfica de transmitancia para un rango dado de E."""
    E_values = np.linspace(*E_range, 500)
    T_values = [T(E, mode=mode) for E in E_values]
    
    plt.figure(figsize=(10, 6))
    plt.plot(E_values, T_values, label='Transmitancia')
    plt.xlabel('Energía (E)')
    plt.ylabel('Transmitancia (T)')
    title = 'Transmitancia en función de la Energía ' + ('(E<V0)' if mode == 'less' else '(E>V0)')
    plt.title(title + f', V_0={V_0}, m={m}, $\\hbar$={h_bar}, a={a}, b={b}')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'transmitancia_vs_energia_{"menor" if mode == "less" else "mayor"}.pdf', format='pdf', bbox_inches='tight')
    plt.close()

# Cuando E < V_0
plot_transmitance((0.01, V_0 - 0.01), mode='less')

# Cuando E > V_0
plot_transmitance((V_0 + 0.01, V_0 + 10), mode='greater')  # Ajusta el rango superior según sea necesario

