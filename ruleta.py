import sys
import numpy as np # pip install matplotlib: libreria con numpy y pyplot
import matplotlib.pyplot as plt
import argparse
import statistics


# Argumentos de línea de comandos
'''
# python programa.py -c XXX -n YYY -e ZZ
parser = argparse.ArgumentParser(description='Simulación de Ruleta.')
parser.add_argument('-c', '--corridas', type=int, required=True, help='Cantidad de corridas/simulaciones')
parser.add_argument('-n', '--tiradas', type=int, required=True, help='Cantidad de tiradas por corrida')
parser.add_argument('-e', '--elegido', type=int, required=True, help='Número apostado/elegido')
args = parser.parse_args()
cant_tiradas = args.c
corridas = args.t
numero_elegido = args.e
'''

cant_tiradas = 1000
corridas = 1
numero_elegido = 0

# ----------- Inicio de la simulación -----------
print(f"Simulando {corridas} corridas de {cant_tiradas} tiradas. Apostando al {numero_elegido}...")

# Definición de variables para almacenar resultados
fa = [] # Frecuencia absoluta 
fr = [] # Frecuencia relativa 

vp = [] # Valor promedio de las tiradas por corrida

desv = [] # Desvio de las tiradas por corrida
vari = [] # Varianza de las tiradas por corrida

cantidadExitos = []

valores_total = []

# La ruleta tiene 37 numeros (0 al 36)
fre = 1.0 / 37.0 # Frecuencia relativa esperada
vpe = 18.0       # Valor promedio esperado (suma de 0 a 36 dividido 37)
desve = statistics.pstdev(list(range(37)))
varie = statistics.pvariance(list(range(37)))

for i in range(corridas):
        
    # Generamos todas las tiradas con numpy para mayor eficiencia
    valores = np.random.randint(0, 37, cant_tiradas)
    valores_total.append(valores)
    # 1. Frecuencia absoluta por Corrida: cantidad de veces que aparece un numero en una corrida
    fac = []

    # 2. Frecuencia Relativa por Corrida: cantidad de veces que aparece un numero en una corrida / cantidad de numeros

    frc = []

    for j in range(37):
        contadorResultados = 0
        for v in range(len(valores)):
            if(j == valores[v] ):
                contadorResultados = contadorResultados + 1
        #frecuencia absoluta del numero j en la corrida i
        fac.append(contadorResultados)  
        #frecuencia relativa del numero j en la corrida i
        frc.append(float(contadorResultados / cant_tiradas))
    fa.append(fac)
    fr.append(frc)

    # 3. Valor promedio de la corrida

    contadorPromedio = 0
    for v in range(len(valores)):
        contadorPromedio = contadorPromedio + valores[v]

    promedioCorrida = float(contadorPromedio/cant_tiradas) 
    vp.append(promedioCorrida)

    # 4. Desvio de las tiradas por corrida

    sumaVarianza = 0
    for v in range(len(valores)):
        # La diferencia entre el valor y el promedio, al cuadrado
        sumaVarianza += (valores[v] - promedioCorrida) ** 2 
    varianzaCorrida = float(sumaVarianza / cant_tiradas)
    vari.append(varianzaCorrida)
    
    # Desvío estándar: raíz cuadrada de la varianza
    desvio_corrida = float(varianzaCorrida ** 0.5)
    desv.append(desvio_corrida)



    print(f"Varianza: {varianzaCorrida} - Desvío: {desvio_corrida}")


     
        
print('Frecuencia Absoluta')
print(fa)
print('Frecuencia Relativa')
print(fr)
print('Valor Promedio')
print(vp)


# Dibuja el gráfico de frecuencia relativa
plt.plot(fr)
plt.title("Número de Tiradas sobre Frecuencia Relativa") # Establece el título del gráfico
plt.xlabel("Número de tiradas") # Establece el título del eje x
plt.ylabel("Frecuencia Relativa") # Establece el título del eje y
plt.show() # Muestra el gráfico





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