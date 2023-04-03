from time import perf_counter
import os

iteraciones = 10000000

print("\nCargando...")

# CÁLCULOS - PROCESADOR

tiempo_inicial = perf_counter()

numero = 1.00000000054
for i in range(iteraciones):
    numero *= 1.000000000001

tiempo = perf_counter() - tiempo_inicial
print("\nTiempo de ejecución (procesador): " + str(tiempo) + " s")

print("\nCargando...")

# ESCRITURA Y LECTURA - DISCO DURO

tiempo_inicial = perf_counter()

# Escritura en el archivo 1
archivo1 = open("archivo1.txt", "w")
for i in range(iteraciones):
    archivo1.write(str("hola") + "\n")
archivo1.close()

# Lectura del archivo 1 y escritura de su contenido en el archivo 2 
archivo1 = open("archivo1.txt", "r")
archivo2 = open("archivo2.txt", "w")
lineas = archivo1.readlines()
contador = 0
for linea in lineas:
    contador += 1
    archivo2.write("Palabra {}: {}".format(contador, linea.strip()) + "\n")
archivo1.close()
archivo2.close()

# Se borran los archivos
os.remove("archivo1.txt")
os.remove("archivo2.txt")

tiempo = perf_counter() - tiempo_inicial
print("\nTiempo de ejecución (disco duro): " + str(tiempo) + " s")
