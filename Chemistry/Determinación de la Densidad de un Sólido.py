import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Datos de balines
data_balines = {
    'Volumen de los Balines (mL)': [1, 2, 3, 4, 5],
    'Masa de los Balines (g)': [8.39, 16.48, 25.3, 33.25, 42.38]
}

df_balines = pd.DataFrame(data_balines)

# Gráfico para balines: Masa vs. Volumen
plt.figure(figsize=(10, 6))
plt.scatter(df_balines['Volumen de los Balines (mL)'], df_balines['Masa de los Balines (g)'], 
            color='royalblue', s=100, edgecolor='black', zorder=5, label='Datos experimentales')

# Ajustar línea de tendencia
# Para pasar por todos los puntos, usamos polinomio de grado n-1, donde n es el número de puntos
coefficients = np.polyfit(df_balines['Volumen de los Balines (mL)'], df_balines['Masa de los Balines (g)'], len(df_balines) - 1)
polynomial = np.poly1d(coefficients)

# Crear valores para la línea de ajuste
x_range = np.linspace(min(df_balines['Volumen de los Balines (mL)']), max(df_balines['Volumen de los Balines (mL)']), 100)
y_fit = polynomial(x_range)

# Graficar la línea de ajuste
plt.plot(x_range, y_fit, color='darkgreen', linewidth=2, linestyle='--', label='Línea de ajuste exacta')

# Anotaciones
for i, txt in enumerate(df_balines['Masa de los Balines (g)']):
    plt.annotate(f'{txt:.2f}', (df_balines['Volumen de los Balines (mL)'][i], df_balines['Masa de los Balines (g)'][i]), 
                 textcoords="offset points", xytext=(0,5), ha='center', fontsize=10, color='black', fontweight='bold')

plt.title('Masa vs. Volumen de los Balines', fontsize=18, fontweight='bold')
plt.xlabel('Volumen de los Balines (mL)', fontsize=14)
plt.ylabel('Masa de los Balines (g)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_linewidth(0.8)
plt.gca().spines['bottom'].set_linewidth(0.8)
plt.savefig('grafico_masa_vs_volumen_balines.png', dpi=300, bbox_inches='tight')
plt.show()
