import numpy as np # pip install matplotlib: libreria con numpy y pyplot
import matplotlib.pyplot as plt
import argparse

# Manejo de argumentos de linea de comandos al ejecutar el script
'''
# python programa.py -c XXX -n YYY -e ZZ
parser = argparse.ArgumentParser(description='Simulación de Ruleta.')
parser.add_argument('-c', '--corridas', type=int, required=True, help='Cantidad de corridas/simulaciones')
parser.add_argument('-n', '--tiradas', type=int, required=True, help='Cantidad de tiradas por corrida')
parser.add_argument('-e', '--elegido', type=int, required=True, help='Número apostado/elegido')
'''

# ----------- Definicion de constantes y variables -----------
# Caracteristicas de la simulacion
'''
args = parser.parse_args()
cant_tiradas = args.c
corridas = args.t
numero_elegido = args.e
'''
cant_tiradas = 1000
corridas = 30
numero_elegido = 0

# Caracteristicas de la ruleta
cant_numeros = 37 # Números del 0 al 36
valores_ruleta = np.arange(cant_numeros) # Array con los valores 0 a 36 de la ruleta

# Definicion de constantes para resultados esperados por ser una distribucion Uniforme Discreta
fre = 1.0 / cant_numeros # Frecuencia relativa esperada
vpe = valores_ruleta.sum() / cant_numeros  # Valor promedio esperado
desve = float(np.std(valores_ruleta)) # Desvio estandar esperado
varie = float(np.var(valores_ruleta)) # Varianza esperada

# ----------- Simulación -----------
# Definicion de variables para almacenar resultados
fa = [] # Frecuencia absoluta 
fr = [] # Frecuencia relativa 
vp = [] # Valor promedio de las tiradas por corrida
desv = [] # Desvio de las tiradas por corrida
vari = [] # Varianza de las tiradas por corrida
cantidad_exitos = [] # Cantidad de veces que salió el número elegido por corrida
valores_total = [] # Almacena los valores de todas las tiradas de todas las corridas para graficos agregados

# Inicia la simulacion
print(f"Simulando {corridas} corridas de {cant_tiradas} tiradas. Apostando al {numero_elegido}...")

for i in range(corridas):
    valores = np.random.randint(0, cant_numeros, cant_tiradas)
    valores_total.append(valores)
    
    fac = [] # Frecuencia absoluta por corrida
    frc = [] # Frecuencia relativa por corrida

    for j in range(cant_numeros):
        contador_resultados = 0
        for v in range(cant_tiradas):
            if j == valores[v]:
                contador_resultados += 1
        fac.append(contador_resultados)
        frc.append(float(contador_resultados / cant_tiradas))
    fa.append(fac)
    fr.append(frc)

    promedio_corrida = float(np.mean(valores)) # Valor promedio por corrida
    vp.append(promedio_corrida)

    varianza_corrida = float(np.var(valores)) # Varianza por corrida
    vari.append(varianza_corrida)

    desvio_corrida = float(np.std(valores)) # Desvio por corrida
    desv.append(desvio_corrida)

    print(f"Corrida N°{i}:\n Promedio: {promedio_corrida} - Varianza: {varianza_corrida} - Desvío: {desvio_corrida}\n")   


# --------- Graficos de comparación por tirada ---------
# estos tres son para ver cómo se van acercando al valor esperado a medida que aumentan las tiradas

# Grafico 1: Historigrama - Promedio --> eje x: las 1000 tiradas, eje y: valor del promedio que se va calculando en cada tirada
# Grafico 2: Historigrama - Varianza --> eje x: las 1000 tiradas, eje y: valor de la varianza que se va calculando en cada tirada
# Grafico 3: Frecuencia relativa del numero elegido por tirada --> eje x: las 1000 tiradas, eje y: valor de la frecuencia relativa del numero elegido que se va calculando en cada tirada

# HACER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# --------- Graficos de comparación por corrida ---------
# estos son para ver que los valores de cada corrida efectivamente son cercanos a los valores esperados

# Grafico 1: Gráfico de bastones - Frecuencia Absoluta
valores_total_concat = np.concatenate(valores_total) # Concatenar los arrays de valores de todas las corridas en un solo array
conteos = np.bincount(valores_total_concat) # Contar la frecuencia absoluta de cada número en el array concatenado

plt.stem(range(cant_numeros), conteos)
plt.title("Gráfico de Bastones - Frecuencia Absoluta de cada número en todas las corridas")
plt.xlabel("Valores de la Ruleta")
plt.ylabel("Cantidad de veces que salió")
plt.show()

# Grafico 2: Gráfico de bastones - Frecuencia relativa del numero elegido por corrida
x_corridas = range(1, corridas + 1) # Eje x con el número de corridas (1, 2, ..., corridas)
fr_corridas = [] # Eje y con la frecuencia relativa del número elegido en cada corrida
for corrida in fr:
    fr_corridas.append(corrida[numero_elegido]) 

plt.stem(x_corridas, fr_corridas, label=f'Frecuencia Relativa del número {numero_elegido}')
plt.axhline(y=fre, color='r', linestyle='--', label='Frecuencia Relativa Esperada')
plt.title("Gráfico de bastones - Número de Corridas sobre Frecuencia Relativa")
plt.xlabel("Número de corridas")
plt.ylabel("Frecuencia Relativa")
plt.legend()
plt.show()

# Grafico 3: Promedio por corrida
plt.stem(x_corridas, vp, label='Valor Promedio')
plt.axhline(y=vpe, color='r', linestyle='--', label='Valor Promedio Esperado')
plt.title("Gráfico de bastones - Número de Corridas sobre Valor Promedio")
plt.xlabel("Número de corridas")
plt.ylabel("Valor Promedio")
plt.legend()
plt.show()

# Grafico 4: Desvio estandar por corrida
plt.stem(x_corridas, desv, label='Valor Desvio')
plt.axhline(y=desve, color='r', linestyle='--', label='Valor Desvio Esperado')
plt.title("Gráfico de bastones - Número de Corridas sobre Valor Desvio")
plt.xlabel("Número de corridas")
plt.ylabel("Valor Desvio")
plt.legend()
plt.show()

# Grafico 5: Varianza por corrida
plt.stem(x_corridas, vari, label='Valor Varianza')
plt.axhline(y=varie, color='r', linestyle='--', label='Valor Varianza Esperado')
plt.title("Gráfico de bastones - Número de Corridas sobre Valor Varianza")
plt.xlabel("Número de corridas")
plt.ylabel("Valor Varianza")
plt.legend()
plt.show()

# estos gráficos se usan para ver cómo los valores acumulados de cada corrida son más precisos y tienden 
# a una distribución normal a medida que aumentan las corridas

# HACER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

'''

    exitos = np.count_nonzero(valores == numero_elegido)



    fa.append(exitos)
    # 2. Frecuencia relativa: exitos / tiradas
    fr.append(exitos / cant_tiradas)
    # 3. Valor promedio: media de los resultados en la corrida
    vp.append(np.mean(valores))
    # 4. Desvio de los resultados
    desv.append(statistics.pstdev(valores))
    # 5. Varianza de los resultados
    vari.append(statistics.pvariance(valores))
print("\n--- ESTADISTICOS FINALES ---")
print(f"Probabilidad teorica (esperada): {fre:.4f}")
print(f"Frecuencia relativa media (simulada): {np.mean(fr):.4f}")
print(f"Valor promedio teorico: {vpe:.2f}")
print(f"Valor promedio simulado: {np.mean(vp):.2f}")

# Preparar datos agregados para graficos
if valores_total:
    valores_total = np.concatenate(valores_total)
else:
    valores_total = np.array([])

# Dibuja el gráfico de bastones (frecuencia absoluta por numero)
conteos = np.bincount(valores_total, minlength=37) if valores_total.size > 0 else np.zeros(37, dtype=int)
plt.bar(range(37), conteos, color='blue')
plt.title("Gráfico de Bastones")
plt.xlabel("Valores de la Ruleta")
plt.ylabel("Cantidad de veces que salió")
plt.show()


# Dibuja el gráfico de promedio de tiradas
plt.plot(vp)
plt.title("Valor promedio de las tiradas") # Establece el título del gráfico
plt.xlabel("Número de tiradas") # Establece el título del eje x
plt.ylabel("Valor promedio de las tiradas") # Establece el título del eje y
plt.show() # Muestra el gráfico

# Dibuja el gráfico del valor de desvio
plt.plot(desv)
plt.title("Desvio de las tiradas") # Establece el título del gráfico
plt.xlabel("Número de tiradas") # Establece el título del eje x
plt.ylabel("Valor del desvio") # Establece el título del eje y
plt.show() # Muestra el gráfico

# Dibuja el gráfico del valor de la varianza
plt.plot(vari)
plt.title("Varianza de las tiradas") # Establece el título del gráfico
plt.xlabel("Número de tiradas") # Establece el título del eje x
plt.ylabel("Valor de la varianza") # Establece el título del eje y
plt.show() # Muestra el gráfico

'''