import numpy as np # pip install matplotlib: libreria con numpy y pyplot
import matplotlib.pyplot as plt
import argparse

'''
El Grafico 1 muestra la frecuencia relativa del número elegido a 
lo largo de las tiradas de una corrida, comparándola con la frecuencia 
relativa esperada. A medida que se realizan más tiradas, la frecuencia 
relativa acumulada debería acercarse a la frecuencia relativa esperada 
(1/37 para una ruleta con números del 0 al 36). 
Este gráfico es útil para visualizar cómo la simulación converge hacia 
los resultados teóricos a medida que aumenta el número de tiradas.
'''

# --------------- Manejo de argumentos de linea de comandos al ejecutar el script ---------------
'''
# python programa.py -c XXX -n YYY -e ZZ
parser = argparse.ArgumentParser(description='Simulación de Ruleta.')
parser.add_argument('-c', '--corridas', type=int, required=True, help='Cantidad de corridas/simulaciones')
parser.add_argument('-n', '--muestras', type=int, required=True, help='Cantidad de muestras por corrida')
parser.add_argument('-e', '--elegido', type=int, required=True, help='Número apostado/elegido')
'''

# ----------- Definicion de constantes y variables -----------
# Caracteristicas de la simulacion
'''
args = parser.parse_args()
cant_muestras = args.c
corridas = args.t
numero_elegido = args.e
'''
cant_muestras = 1000
corridas = 1
numero_elegido = 0

# Caracteristicas de la ruleta
cant_numeros_ruleta = 37 # Números del 0 al 36
valores_ruleta = np.arange(cant_numeros_ruleta) # Array con los valores 0 a 36 de la ruleta

# --------- Datos Esperados ---------
# Distribucion Uniforme Discreta
fr_e = 1.0 / cant_numeros_ruleta # Frecuencia relativa esperada
vp_e = valores_ruleta.sum() / cant_numeros_ruleta  # Valor promedio esperado
desv_e = float(np.std(valores_ruleta)) # Desvio estandar esperado
vari_e = float(np.var(valores_ruleta)) # Varianza esperada

# ----------- Inicio de la simulación -----------
print(f"Simulando {corridas} corridas de {cant_muestras} tiradas. Apostando al {numero_elegido}...")

fa = [] # Frecuencia absoluta de cada numero por corrida. fa[i][j] = corrida i, numero j
fr_a = [] # Frecuencia relativa de cada numero acumulada por corrida. fr_a[i][j][k] = corrida i, numero j, tirada k
vp_a = [] # Valor promedio acumulado por corrida. vp_a[i][k] = corrida i, tirada k
vd_a = [] # Valor desvio acumulado por corrida. vd_a[i][k] = corrida i, tirada k
vv_a = [] # Valor varianza acumulado por corrida. vv_a[i][k] = corrida i, tirada k

for corrida in range(corridas):
    valores = np.random.randint(0, cant_numeros_ruleta, cant_muestras)

    # Frecuencia absoluta por numero
    fa_c = []
    for numero in range(cant_numeros_ruleta):
        fa_c.append(int(np.sum(valores == numero))) # Cuenta cuántas veces aparece el número en las muestras de la corrida
    fa.append(fa_c)

    # Frecuencia relativa acumulada por numero
    fr_a_c = []
    muestras = np.arange(1, cant_muestras + 1)
    for numero in range(cant_numeros_ruleta):
        acumulado_numero = np.cumsum(valores == numero) # Suma acumulada de cuántas veces apareció el número en las muestras de la corrida
        fr_a_c.append((acumulado_numero / muestras).astype(float).tolist()) # Frecuencia relativa acumulada por numero y corrida
    fr_a.append(fr_a_c)

    # Promedio acumulado
    acumulado = np.cumsum(valores) # Suma acumulada de los valores de las muestras de la corrida
    vp_c = (acumulado / muestras).astype(float)
    vp_a.append(vp_c.tolist())

    # Varianza acumulada
    acumulado_sq = np.cumsum(valores ** 2)
    vv_c = ((acumulado_sq / muestras) - (vp_c ** 2))
    vv_a.append(vv_c.astype(float).tolist())

    # Desvio acumulado
    vd_c = np.sqrt(vv_c)
    vd_a.append(vd_c.astype(float).tolist())



# --------- Graficos de comparación en UNA corrida ---------
# Grafico 1: Gráfico de bastones - Frecuencia Absoluta
plt.stem(range(1, cant_numeros_ruleta+1), fa[0], label='Frecuencia Absoluta')
plt.title("Gráfico de Bastones - Frecuencia Absoluta de cada número en una corrida")
plt.xlabel("Valores de la Ruleta")
plt.ylabel("Cantidad de veces que salió")
plt.show()

# Grafico 2
# Dibuja el gráfico de valor promedio acumulado para el nro elegido a lo largo de las tiradas de una corrida
plt.plot(range(1, cant_muestras+1), vp_a[0], label='Valor Promedio de una corrida')
plt.axhline(y=vp_e, color='r', linestyle='--', label='Valor Promedio Esperado') # Dibuja una línea horizontal para el valor promedio esperado
plt.title("Número de Tiradas sobre Valor Promedio") # Establece el título del gráfico
plt.xlabel("Número de tiradas") # Establece el título del eje x 
plt.ylabel("Valor Promedio") # Establece el título del eje y
plt.legend() # Muestra la leyenda
plt.show() # Muestra el gráfico

# Grafico 3
# Dibuja el gráfico de valor desvio acumulado para el nro elegido a lo largo de las tiradas de una corrida
plt.plot(range(1, cant_muestras+1), vd_a[0], label=f'Valor Desvio del número {numero_elegido}')
plt.axhline(y=desv_e, color='r', linestyle='--', label='Valor Desvio Esperado') # Dibuja una línea horizontal para el valor desvio esperado
plt.title("Número de Tiradas sobre Valor Desvio") # Establece el título del gráfico
plt.xlabel("Número de tiradas") # Establece el título del eje x 
plt.ylabel("Valor Desvio") # Establece el título del eje y
plt.legend() # Muestra la leyenda
plt.show() # Muestra el gráfico

# Grafico 4
# Dibuja el gráfico de valor varianza acumulado para el nro elegido a lo largo de las tiradas de una corrida
plt.plot(range(1, cant_muestras+1), vv_a[0], label=f'Valor Varianza del número {numero_elegido}')
plt.axhline(y=vari_e, color='r', linestyle='--', label='Valor Varianza Esperado') 
plt.title("Número de Tiradas sobre Valor Varianza")
plt.xlabel("Número de tiradas")
plt.ylabel("Valor Varianza")
plt.legend()
plt.show()

# --------- Graficos de comparación del NUMERO ELEGIDO por tirada de 1 corrida ---------
# Grafico 1
# Dibuja el gráfico de frecuencia relativa para el NUMERO ELEGIDO a lo largo de las tiradas de una corrida
plt.plot(range(1, cant_muestras+1), fr_a[0][numero_elegido], label=f'Frecuencia Relativa del número {numero_elegido}')
plt.axhline(y=fr_e, color='r', linestyle='--', label='Frecuencia Relativa Esperada')
plt.title("Número de Tiradas sobre Frecuencia Relativa del NÚMERO ELEGIDO")
plt.xlabel("Número de tiradas") 
plt.ylabel("Frecuencia Relativa")
plt.legend()
plt.show()

# ---------- Graficos de tendencia de la distribución de los valores (TCL) a lo largo de las corridas ----------
# Grafico 1
# Dibuja el histograma de los promedios finales de cada corrida
promedios_finales = [promedios_corrida[-1] for promedios_corrida in vp_a]
plt.hist(promedios_finales, bins=0.5, edgecolor='black')
plt.axvline(x=vp_e, color='r', linestyle='--', label='Valor Promedio Esperado')
plt.title("Histograma de promedios finales por corrida")
plt.xlabel("Valor Promedio Final")
plt.ylabel("Frecuencia")
plt.legend()
plt.show()