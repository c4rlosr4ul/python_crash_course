
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Directory to save figures
output_dir = "figures"
os.makedirs(output_dir, exist_ok=True)

# Step 1: Load and prepare the data
def load_data(file_path):
    import xml.etree.ElementTree as ET
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespace = {"v": "http://www.ivoa.net/xml/VOTable/v1.1"}
    fields = [field.attrib['name'] for field in root.findall(".//v:FIELD", namespace)]
    rows = [[td.text for td in row.findall(".//v:TD", namespace)] for row in root.findall(".//v:TR", namespace)]
    return pd.DataFrame(rows, columns=fields)

# Step 2: Clean and convert data
def clean_data(df):
    for col in ['Plx', 'e_Plx', 'BPmag', 'RPmag', 'Gmag', 'Teff', 'logg', '[Fe/H]']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

# Step 3: Filter cluster members based on parallax range
def filter_cluster_members(df, plx_min=0.2, plx_max=0.6):
    cluster_df = df[(df['Plx'] >= plx_min) & (df['Plx'] <= plx_max)]
    cluster_df['BP-RP'] = cluster_df['BPmag'] - cluster_df['RPmag']
    return cluster_df.dropna(subset=['BP-RP', 'Gmag'])

# Step 4: Generate visualizations
def plot_parallax_histogram(df, plx_min, plx_max):
    plt.figure(figsize=(10, 6))
    plt.hist(df['Plx'].dropna(), bins=50, color='blue', alpha=0.7, label='All stars')
    plt.axvspan(plx_min, plx_max, color='red', alpha=0.3, label='Cluster range')
    plt.xlabel('Parallax (mas)')
    plt.ylabel('Number of stars')
    plt.title('Parallax Distribution')
    plt.legend()
    plt.savefig(os.path.join(output_dir, "parallax_distribution.pdf"), format="pdf")
    plt.show()

def plot_hr_diagram(cluster_df):
    plt.figure(figsize=(10, 6))
    plt.scatter(cluster_df['BP-RP'], cluster_df['Gmag'], c='blue', alpha=0.7)
    plt.gca().invert_yaxis()
    plt.xlabel('BP-RP (Color Index)')
    plt.ylabel('Gmag (Absolute Magnitude)')
    plt.title('Hertzsprung-Russell Diagram for NGC 6811')
    plt.savefig(os.path.join(output_dir, "hr_diagram.pdf"), format="pdf")
    plt.show()

def plot_temperature_distribution(cluster_df):
    plt.figure(figsize=(10, 6))
    plt.hist(cluster_df['Teff'].dropna(), bins=30, color='orange', alpha=0.7)
    plt.xlabel('Effective Temperature (Teff, K)')
    plt.ylabel('Number of stars')
    plt.title('Distribution of Effective Temperatures')
    plt.savefig(os.path.join(output_dir, "temperature_distribution.pdf"), format="pdf")
    plt.show()

def plot_temperature_vs_magnitude(cluster_df):
    plt.figure(figsize=(10, 6))
    plt.scatter(cluster_df['Teff'], cluster_df['Gmag'], c='green', alpha=0.6)
    plt.gca().invert_yaxis()
    plt.xlabel('Effective Temperature (Teff, K)')
    plt.ylabel('Gmag (Absolute Magnitude)')
    plt.title('Temperature vs Magnitude')
    plt.savefig(os.path.join(output_dir, "temperature_vs_magnitude.pdf"), format="pdf")
    plt.show()

def plot_metallicity_distribution(cluster_df):
    plt.figure(figsize=(10, 6))
    plt.hist(cluster_df['[Fe/H]'].dropna(), bins=30, color='purple', alpha=0.7)
    plt.xlabel('[Fe/H] (Metallicity)')
    plt.ylabel('Number of stars')
    plt.title('Distribution of Metallicity ([Fe/H])')
    plt.savefig(os.path.join(output_dir, "metallicity_distribution.pdf"), format="pdf")
    plt.show()

# Step 5: Generate report
def generate_summary(df, cluster_df):
    return {
        'Total stars analyzed': len(df),
        'Cluster members identified': len(cluster_df),
        'Mean parallax (cluster)': cluster_df['Plx'].mean(),
        'Mean BP-RP (color)': cluster_df['BP-RP'].mean(),
        'Mean Teff (if available)': cluster_df['Teff'].mean() if 'Teff' in cluster_df.columns else 'N/A',
    }

# Execute the analysis
file_path = 'ngc6811-r1.5-p.3.4.xml'
data = load_data(file_path)
cleaned_data = clean_data(data)
cluster_members = filter_cluster_members(cleaned_data)

# Visualizations
plot_parallax_histogram(cleaned_data, plx_min=2, plx_max=3)
plot_hr_diagram(cluster_members)
plot_temperature_distribution(cluster_members)
plot_temperature_vs_magnitude(cluster_members)
plot_metallicity_distribution(cluster_members)

# Summary
summary = generate_summary(cleaned_data, cluster_members)
print(summary)

