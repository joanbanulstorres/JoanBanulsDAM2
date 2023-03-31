from time import perf_counter
import os

print("\nCargando...")

tiempo_inicial = perf_counter()
numero = 1.00000000054
iteraciones = 5000000

# Escritura en el archivo 1
archivo1 = open("archivo1.txt", "w")
for i in range(iteraciones):
    numero *= 1.000000000001
    archivo1.write(str(numero) + "\n")
archivo1.close()

# Lectura del archivo 1 y escritura de su contenido en el archivo 2 
archivo1 = open("archivo1.txt", "r")
archivo2 = open("archivo2.txt", "w")
lineas = archivo1.readlines()
contador = 0
for linea in lineas:
    contador += 1
    archivo2.write("Valor del número en la iteración {}: {}".format(contador, linea.strip()) + "\n")
archivo1.close()
archivo2.close()

# Se borran los archivos
os.remove("archivo1.txt")
os.remove("archivo2.txt")

tiempo = perf_counter() - tiempo_inicial
print("\nTiempo de ejecución: " + str(tiempo) + " s")
