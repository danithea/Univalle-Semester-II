#Resultados de medición con CronoLab.
import numpy as np

def calcular_gravedad_y_uncertumbre(longitudes, inc_longitudes, periodos, inc_periodos):
    g = []
    inc_g = []
    
    for l, T, inc_l, inc_T in zip(longitudes, periodos, inc_longitudes, inc_periodos):
        # Calcular g
        g_val = (4 * np.pi**2 * l) / T**2
        g.append(g_val)
        
        # Calcular incertidumbre en g
        inc_g_val = g_val * np.sqrt((inc_l / l)**2 + (2 * inc_T / T)**2)
        inc_g.append(inc_g_val)
    
    return g, inc_g

# Datos proporcionados
longitudes = [0.800, 0.700, 0.600, 0.500, 0.400]  # Longitudes del péndulo en metros
inc_longitudes = [0.001, 0.001, 0.001, 0.001, 0.001]  # Incertidumbres en las longitudes
periodos = [1.81, 1.69, 1.54, 1.38, 1.24]  # Períodos de oscilación en segundos
inc_periodos = [0.04, 0.06, 0.04, 0.04, 0.05]  # Incertidumbres en los períodos

# Cálculo
gravedad, incertidumbre_gravedad = calcular_gravedad_y_uncertumbre(longitudes, inc_longitudes, periodos, inc_periodos)

# Imprimir resultados
for i in range(len(longitudes)):
    print(f"Para longitud {longitudes[i]} m y período {periodos[i]} s:")
    print(f"  𝑔  = {gravedad[i]:.2f} m/s²")
    print(f"  ∆𝑔  = {incertidumbre_gravedad[i]:.2f} m/s²")
    print(f"  𝑔 ± ∆𝑔 = {gravedad[i]:.2f} ± {incertidumbre_gravedad[i]:.2f} m/s²\n")