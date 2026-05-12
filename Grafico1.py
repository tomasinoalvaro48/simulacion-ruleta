import numpy as np # pip install matplotlib: libreria con numpy y pyplot
import matplotlib.pyplot as plt

'''
El Grafico 1 muestra la frecuencia relativa del número elegido a 
lo largo de las tiradas de una corrida, comparándola con la frecuencia 
relativa esperada. A medida que se realizan más tiradas, la frecuencia 
relativa acumulada debería acercarse a la frecuencia relativa esperada 
(1/37 para una ruleta con números del 0 al 36). 
Este gráfico es útil para visualizar cómo la simulación converge hacia 
los resultados teóricos a medida que aumenta el número de tiradas.
'''

#Argumentos de línea de comandos
cant_tiradas = 10000
corridas = 1
numero_elegido = 0


#--------- Datos Esperados ---------
# La ruleta tiene 37 numeros (0 al 36)
fre = 1.0 / 37.0 # Frecuencia relativa esperada
vpe = 18.0       # Valor promedio esperado (suma de 0 a 36 dividido 37)
desve = np.std(np.arange(37)) # Desvio estandar esperado
varie = desve**2 # Varianza esperada


# ----------- Inicio de la simulación -----------
print(f"Simulando {corridas} corridas de {cant_tiradas} tiradas. Apostando al {numero_elegido}...")


valores = np.random.randint(0, 37, cant_tiradas)

frca = [] # Frecuencia relativa acumulada por corrida
vpn = [] # Valor promedio acumulado por corrida
vdn = [] # Valor desvio acumulado por corrida
vvn = [] # Valor varianza acumulado por corrida

acumulado = 0
for i in range(len(valores)):
    if(valores[i] == numero_elegido):
        acumulado += 1
    frca.append(acumulado / (i + 1))

for i in range(len(valores)):
    #Valor promedio acumulado
    vpa = 0
    for j in range(i+1):
        vpa = vpa + valores[j]
    vpn.append(float(vpa) / (i + 1))
    

    #Desvio acumulado
    vda = 0
    for j in range(i+1):
        vda += ((valores[j] - vpn[i])**2) # Suma de los cuadrados de las diferencias entre cada valor y el valor promedio acumulado
    vda = (vda/(i + 1))**0.5 # Desviación estándar acumulada
    vdn.append(vda)

    #Varianza acumulada
    vva = 0
    for j in range(i+1):
        vva += ((valores[j] - vpn[i])**2) # Suma de los cuadrados de las diferencias entre cada valor y el valor promedio acumulado
    vva = vva/(i + 1) # Varianza acumulada
    vvn.append(vva)

    


        






#Grafico 1

# Dibuja el gráfico de frecuencia relativa para el nro elegido a lo largo de las tiradas de una corrida
plt.plot(range(1, cant_tiradas+1), frca, label=f'Frecuencia Relativa del número {numero_elegido}') # Dibuja la frecuencia relativa del número elegido
plt.axhline(y=fre, color='r', linestyle='--', label='Frecuencia Relativa Esperada') # Dibuja una línea horizontal para la frecuencia relativa esperada
plt.title("Número de Tiradas sobre Frecuencia Relativa") # Establece el título del gráfico
plt.xlabel("Número de tiradas") # Establece el título del eje x
plt.ylabel("Frecuencia Relativa") # Establece el título del eje y
plt.legend() # Muestra la leyenda
plt.show() # Muestra el gráfico


#Grafico 2
# Dibuja el gráfico de valor promedio acumulado para el nro elegido a lo largo de las tiradas de una corrida
plt.plot(range(1, cant_tiradas+1), vpn, label=f'Valor Promedio del número {numero_elegido}') # Dibuja el valor promedio del número elegido
plt.axhline(y=vpe, color='r', linestyle='--', label='Valor Promedio Esperado') # Dibuja una línea horizontal para el valor promedio esperado
plt.title("Número de Tiradas sobre Valor Promedio") # Establece el título del gráfico
plt.xlabel("Número de tiradas") # Establece el título del eje x 
plt.ylabel("Valor Promedio") # Establece el título del eje y
plt.legend() # Muestra la leyenda
plt.show() # Muestra el gráfico

#Grafico 3
# Dibuja el gráfico de valor desvio acumulado para el nro elegido a lo largo de las tiradas de una corrida
plt.plot(range(1, cant_tiradas+1), vdn, label=f'Valor Desvio del número {numero_elegido}') # Dibuja el valor desvio del número elegido
plt.axhline(y=desve, color='r', linestyle='--', label='Valor Desvio Esperado') # Dibuja una línea horizontal para el valor desvio esperado
plt.title("Número de Tiradas sobre Valor Desvio") # Establece el título del gráfico
plt.xlabel("Número de tiradas") # Establece el título del eje x 
plt.ylabel("Valor Desvio") # Establece el título del eje y
plt.legend() # Muestra la leyenda
plt.show() # Muestra el gráfico


#Grafico 4
# Dibuja el gráfico de valor varianza acumulado para el nro elegido a lo largo
# de las tiradas de una corrida
plt.plot(range(1, cant_tiradas+1), vvn, label=f'Valor Varianza del número {numero_elegido}') # Dibuja el valor varianza del número elegido
plt.axhline(y=varie, color='r', linestyle='--', label='Valor Varianza Esperado') # Dibuja una línea horizontal para el valor varianza esperado
plt.title("Número de Tiradas sobre Valor Varianza") # Establece el título del gráfico
plt.xlabel("Número de tiradas") # Establece el título del eje x 
plt.ylabel("Valor Varianza") # Establece el título del eje y
plt.legend() # Muestra la leyenda
plt.show() # Muestra el gráfico

       








