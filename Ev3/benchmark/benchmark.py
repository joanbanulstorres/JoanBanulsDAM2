from time import perf_counter

######### ▼ CÁLCULOS DE UN NÚMERO ▼ ##########

tiempo_inicial = perf_counter()

numero = 1.00000000054
iteraciones = 10000000
for i in range(iteraciones):
    numero *= 1.000000000001

tiempo = perf_counter() - tiempo_inicial
print("Tiempo requerido para realizar los cálculos: " + str(tiempo) + " s")

######### ▲ CÁLCULOS DE UN NÚMERO ▲ ##########


######### ▼ CÁLCULOS DE UN NÚMERO Y ESCRITURA Y LECTURA DE ARCHIVOS ▼ ##########

tiempo_inicial = perf_counter()

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

tiempo = perf_counter() - tiempo_inicial
print("Tiempo requerido para realizar los cálculos, escribir y leer en los archivos: " + str(tiempo) + " s")

######### ▲ CÁLCULOS DE UN NÚMERO Y ESCRITURA Y LECTURA DE ARCHIVOS ▲ ##########
