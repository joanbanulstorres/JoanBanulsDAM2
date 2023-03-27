import os
import datetime

ruta_inicial = r"C:\Users\joan\Desktop"
nombre_directorio = "Carpeta1"

# Esta función devuelve por consola las propiedades de los archivos de un directorio especificado y sus subdirectorios 
def leer_directorios_consola(ruta_inicial, nombre_directorio):
    ruta = ruta_inicial + "\\" + nombre_directorio
    resultado = os.scandir(ruta)
    print("\nContenido del directorio " + nombre_directorio + ":")
    for elemento in resultado:
        if elemento.is_file():

            print("\nNombre:\t" + elemento.name)

            print("Ruta:\t" + elemento.path)

            print("Tamaño:\t" + str(os.path.getsize(elemento.path)) + " bytes")

            fecha_creado_ms = os.path.getctime(elemento.path)
            fecha_modificado = datetime.datetime.fromtimestamp(fecha_creado_ms)
            print("Creado:\t", fecha_modificado)

            fecha_modificado_ms = os.path.getmtime(elemento.path)
            fecha_modificado = datetime.datetime.fromtimestamp(fecha_modificado_ms)
            print("Modificado:", fecha_modificado)
            
        if elemento.is_dir():
            #print("Contenido del subdirectorio", elemento.name)
            nombre_subdirectorio = elemento.name
            # Recursividad para los subdirectorios
            leer_directorios_consola(ruta, nombre_subdirectorio)           

# Esta función vuelca en un archivo las propiedades de los archivos de un directorio especificado y de sus subdirectorios 
def leer_directorios(archivo_resultado, ruta_inicial, nombre_directorio):
    ruta = ruta_inicial + "\\" + nombre_directorio
    print("La ruta es: " + ruta)
    resultado = os.scandir(ruta)
    for elemento in resultado:
        if elemento.is_file():

            archivo_resultado.write("\nNombre:\t" + elemento.name)

            archivo_resultado.write("\nRuta:\t" + elemento.path)

            archivo_resultado.write("\nTamaño:\t" + str(os.path.getsize(elemento.path)) + " bytes")

            fecha_creado_ms = os.path.getctime(elemento.path)
            fecha_modificado = str(datetime.datetime.fromtimestamp(fecha_creado_ms))
            archivo_resultado.write("\nCreado:\t" + fecha_modificado)

            fecha_modificado_ms = os.path.getmtime(elemento.path)
            fecha_modificado = str(datetime.datetime.fromtimestamp(fecha_modificado_ms))
            archivo_resultado.write("\nModificado:\t" + fecha_modificado)
            
            archivo_resultado.write("\n")
        if elemento.is_dir():
            nombre_subdirectorio = elemento.name
            archivo_resultado.write("\n\nContenido del subdirectorio " + nombre_subdirectorio + "\n")
            # Recursividad para los subdirectorios
            leer_directorios(archivo_resultado, ruta, nombre_subdirectorio)  

leer_directorios_consola(ruta_inicial, nombre_directorio)

# Se abre un archivo para escribir en el mismo, borrando previamente su contenido 
archivo_resultado = open("resultado.txt", "w")

archivo_resultado.write("Contenido del directorio " + nombre_directorio + ":\n")
leer_directorios(archivo_resultado, ruta_inicial, nombre_directorio)
archivo_resultado.close()
