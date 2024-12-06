
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.stats import linregress

# Configuración de salida
output_dir = "figures"
os.makedirs(output_dir, exist_ok=True)

def load_data(file_path):
    """Carga y procesa los datos de un archivo XML en formato VOTable."""
    import xml.etree.ElementTree as ET
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespace = {"v": "http://www.ivoa.net/xml/VOTable/v1.1"}
    
    # Extraer campos y filas
    fields = [field.attrib['name'] for field in root.findall(".//v:FIELD", namespace)]
    rows = [[td.text for td in tr.findall(".//v:TD", namespace)] for tr in root.findall(".//v:TR", namespace)]
    return pd.DataFrame(rows, columns=fields)

def clean_data(df):
    """Convierte columnas relevantes a valores numéricos."""
    for col in ['Plx', 'e_Plx', 'BPmag', 'RPmag', 'Gmag', 'Teff', 'logg', '[Fe/H]', 'pmRA', 'pmDE']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    df['BP-RP'] = df['BPmag'] - df['RPmag']
    return df

def filter_by_parallax(df, plx_min=0.3, plx_max=0.4):
    """Filtra datos según un rango de paralaje."""
    return df[(df['Plx'] >= plx_min) & (df['Plx'] <= plx_max)]

def plot_parallax_histogram(df, filename):
    """Genera un histograma de paralajes."""
    plt.figure(figsize=(10, 6))
    plt.hist(df['Plx'].dropna(), bins=50, color='blue', alpha=0.7, label='Todas las estrellas')
    plt.axvline(df['Plx'].mean(), color='red', linestyle='--', label=f'Promedio: {df["Plx"].mean():.3f} mas')
    plt.xlabel('Paralaje (mas)')
    plt.ylabel('Número de estrellas')
    plt.title('Distribución de Paralajes')
    plt.legend()
    plt.savefig(os.path.join(output_dir, filename), format="pdf")
    plt.show()

def plot_hr_diagram(df, filename, title):
    """Genera un diagrama Hertzsprung-Russell."""
    plt.figure(figsize=(10, 6))
    plt.scatter(df['BP-RP'], df['Gmag'], c='blue', alpha=0.6, label='Estrellas')
    plt.gca().invert_yaxis()
    plt.xlabel('Índice de Color (BP-RP)')
    plt.ylabel('Magnitud Absoluta (Gmag)')
    plt.title(title)
    plt.legend()
    plt.savefig(os.path.join(output_dir, filename), format="pdf")
    plt.show()

def plot_motion(df, filename):
    """Genera un gráfico de movimientos propios."""
    plt.figure(figsize=(10, 6))
    plt.quiver(np.zeros(len(df)), np.zeros(len(df)), df['pmRA'], df['pmDE'], angles='xy', scale_units='xy', scale=1, color='green')
    plt.xlabel('Movimiento Propio en Ascensión Recta (mas/año)')
    plt.ylabel('Movimiento Propio en Declinación (mas/año)')
    plt.title('Vectores de Movimiento Propio')
    plt.grid()
    plt.savefig(os.path.join(output_dir, filename), format="pdf")
    plt.show()


def plot_teff_vs_magnitude(df, filename):
    """Relaciona temperatura efectiva y magnitud absoluta."""
    # Filtrar filas donde ambas columnas tienen datos válidos
    valid_data = df.dropna(subset=['Teff', 'Gmag'])

    if len(valid_data) > 1:  # Verificar que hay datos suficientes
        plt.figure(figsize=(10, 6))
        plt.scatter(valid_data['Teff'], valid_data['Gmag'], c='purple', alpha=0.7, label='Estrellas')
        slope, intercept, _, _, _ = linregress(valid_data['Teff'], valid_data['Gmag'])
        x_fit = np.linspace(valid_data['Teff'].min(), valid_data['Teff'].max(), 100)
        y_fit = slope * x_fit + intercept
        plt.plot(x_fit, y_fit, color='orange', linestyle='--', label='Ajuste lineal')
        plt.gca().invert_yaxis()
        plt.xlabel('Temperatura Efectiva (K)')
        plt.ylabel('Magnitud Absoluta (Gmag)')
        plt.title('Relación entre Temperatura Efectiva y Magnitud')
        plt.legend()
        plt.savefig(os.path.join(output_dir, filename), format="pdf")
        plt.show()
    else:
        print(f"Datos insuficientes para generar el gráfico de {filename}. Se requiere al menos 2 puntos.")


def plot_metallicity_distribution(df, filename):
    """Genera un histograma de metalicidad."""
    plt.figure(figsize=(10, 6))
    plt.hist(df['[Fe/H]'].dropna(), bins=30, color='gold', alpha=0.7)
    plt.xlabel('Metalicidad [Fe/H]')
    plt.ylabel('Número de estrellas')
    plt.title('Distribución de Metalicidad')
    plt.savefig(os.path.join(output_dir, filename), format="pdf")
    plt.show()

# Cargar datos
file_path_1 = 'ngc6811-r1.5-p.3.4.xml'
file_path_2 = 'ngc6811-r1.5.xml'

data_1 = load_data(file_path_1)
data_2 = load_data(file_path_2)

# Procesar datos
data_1 = clean_data(data_1)
data_2 = clean_data(data_2)

# Filtrar datos
filtered_data_1 = filter_by_parallax(data_1, 0.3, 0.4)
filtered_data_2 = data_2  # Sin restricción de paralaje

# Generar gráficas
plot_parallax_histogram(filtered_data_1, "parallax_histogram_restricted.pdf")
plot_hr_diagram(filtered_data_1, "hr_diagram_restricted.pdf", "Diagrama H-R (Restricción de Paralaje)")
plot_hr_diagram(filtered_data_2, "hr_diagram_full.pdf", "Diagrama H-R (Completo)")
plot_motion(filtered_data_1, "motion_vectors_restricted.pdf")
plot_teff_vs_magnitude(filtered_data_1, "teff_vs_magnitude_restricted.pdf")
plot_metallicity_distribution(filtered_data_1, "metallicity_distribution_restricted.pdf")

# Resumen del análisis
summary = {
    "Número de estrellas analizadas (archivo 1)": len(data_1),
    "Número de estrellas analizadas (archivo 2)": len(data_2),
    "Número de estrellas tras filtro (archivo 1)": len(filtered_data_1),
    "Paralaje promedio (archivo 1)": filtered_data_1['Plx'].mean(),
    "Metalicidad promedio (archivo 1)": filtered_data_1['[Fe/H]'].mean(),
}
print(summary)
