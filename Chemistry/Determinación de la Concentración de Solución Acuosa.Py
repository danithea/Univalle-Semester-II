import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Datos corregidos de concentración y densidad
data = {
    'Concentracion (%)': [5, 10, 15, 20],
    'Densidad (g/mL)': [0.991, 1.015, 1.057, 1.078]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Ajustar línea de tendencia (lineal) con valores recalculados
m = 0.00606
b = 0.9595

# Crear valores para la línea de ajuste
x_range = np.linspace(min(df['Concentracion (%)']), max(df['Concentracion (%)']), 100)
y_fit = m * x_range + b

# Datos para la concentración desconocida
densidad_desconocida = 1.050
concentracion_predicha = (densidad_desconocida - b) / m

# Actualizar los datos con el nuevo punto
df_desconocida = pd.DataFrame({
    'Concentracion (%)': [5, 10, 15, 20, concentracion_predicha],
    'Densidad (g/mL)': [0.991, 1.015, 1.057, 1.078, densidad_desconocida]
})

# Configurar estilo de gráfico
plt.figure(figsize=(12, 7))

# Graficar los datos experimentales
plt.scatter(df['Concentracion (%)'], df['Densidad (g/mL)'], color='royalblue', s=100, edgecolor='black', zorder=5, label='Datos experimentales')

# Graficar la línea de ajuste
plt.plot(x_range, y_fit, color='darkgreen', linewidth=2, linestyle='--', label='Línea de ajuste lineal')

# Anotar los datos experimentales
for i, txt in enumerate(df['Densidad (g/mL)']):
    plt.annotate(f'{txt:.3f}', (df['Concentracion (%)'][i], df['Densidad (g/mL)'][i]), 
                 textcoords="offset points", xytext=(0,5), ha='center', fontsize=10, color='black', fontweight='bold')

# Anotar el punto de densidad desconocida con el porcentaje estimado
plt.scatter(concentracion_predicha, densidad_desconocida, color='blue', s=150, edgecolor='black', zorder=5, label=f'Porcentaje estimado: {concentracion_predicha:.2f}%')
plt.annotate(f'{concentracion_predicha:.2f}%', (concentracion_predicha, densidad_desconocida), 
             textcoords="offset points", xytext=(0,10), ha='center', fontsize=12, color='black', fontweight='bold')

# Mejorar apariencia del gráfico
plt.title('Densidad vs. Concentración de Soluciones de Sacarosa', fontsize=18, fontweight='bold')
plt.xlabel('Concentración (%)', fontsize=14)
plt.ylabel('Densidad (g/mL)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_linewidth(0.8)
plt.gca().spines['bottom'].set_linewidth(0.8)
plt.gca().spines['left'].set_color('black')
plt.gca().spines['bottom'].set_color('black')

# Ajustar márgenes y guardar la imagen
plt.tight_layout()
plt.savefig('grafico_densidad_vs_concentracion_sacarosa_mejorado.png', dpi=300, bbox_inches='tight')
plt.show()
