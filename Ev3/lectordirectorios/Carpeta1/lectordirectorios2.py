import os
import datetime
import tkinter as tk
from tkinter import messagebox, ttk

########## ▼ DECLARACIÓN DE FUNCIONES ▼ ##########

# Esta función añade a una lista todos los subdirectorios de un directorio especificado
def obtener_subdirectorios(directorio, lista_directorios):  
    resultado = os.scandir(directorio)
    for elemento in resultado:
        if elemento.is_dir():                           # Se seleccionan únicamente los directorios
            nombre_subdirectorio = elemento.name
            lista_directorios.append(nombre_subdirectorio)

# Esta función capta la opción seleccionada del menú desplegable y actualiza la ruta 
def actualizar_ruta(seleccion, ruta):
    seleccion = desplegable.get()
    print("Se ha seleccionado: " + seleccion)
    # Se cambia la ruta que ve el usuario
    ruta = ruta + "\\" + seleccion  
    ruta_actual.configure(text=ruta)
    # Se muestran los nuevos subdirectorios en el menú desplegable
    
    
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
            fecha_creado = datetime.datetime.fromtimestamp(fecha_creado_ms)
            print("Creado:\t", fecha_creado)

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
    resultado = os.scandir(ruta)
    for elemento in resultado:
        if elemento.is_file():
            #Nombre
            archivo_resultado.write("\nNombre:\t" + elemento.name)
            # Ruta
            archivo_resultado.write("\nRuta:\t" + elemento.path)
            # Tamaño
            archivo_resultado.write("\nTamaño:\t" + str(os.path.getsize(elemento.path)) + " bytes")
            # Fecha de creación
            fecha_creado_ms = os.path.getctime(elemento.path)                                           # tiempo en ms
            fecha_creado = str(datetime.datetime.fromtimestamp(fecha_creado_ms))                        # conversión a fecha
            archivo_resultado.write("\nCreado:\t" + fecha_creado)
            #Fecha de modificación
            fecha_modificado_ms = os.path.getmtime(elemento.path)
            fecha_modificado = str(datetime.datetime.fromtimestamp(fecha_modificado_ms))
            archivo_resultado.write("\nModificado:\t" + fecha_modificado)
            # Salto de línea
            archivo_resultado.write("\n")
        if elemento.is_dir():
            nombre_subdirectorio = elemento.name
            archivo_resultado.write("\n\nContenido del subdirectorio " + nombre_subdirectorio + "\n")
            # Recursividad para analizar los subdirectorios
            leer_directorios(archivo_resultado, ruta, nombre_subdirectorio)
            
########## ▲ DECLARACIÓN DE FUNCIONES ▲ ##########
            
            
########## ▼ DECLARACIÓN DE VARIABLES GENERALES ▼ ##########

ruta = r"C:\Users\joan"
lista_directorios = []
seleccion = ""
nombre_directorio = "Users"
mifuente = "Arial"
color_fondo = "#ffffff"
color_texto = "#000000"

# Definición de los directorios iniciales para el menú desplegable
obtener_subdirectorios(ruta, lista_directorios)

########## ▲ DECLARACIÓN DE VARIABLES GENERALES ▲ ##########


########## ▼ INTERFAZ DE USUARIO ▼ ##########

raiz = tk.Tk()
raiz.title("Lector de directorios")
raiz.geometry('600x150+100+100')
raiz.configure(bg=color_fondo)
raiz.attributes("-topmost", True)
#raiz.attributes("-alpha", 0.95)
raiz.resizable(0,0)
estilo = ttk.Style()

ruta_actual_texto = tk.Label(raiz, text="Ruta actual:", font=(mifuente, 14), bg=color_fondo, fg=color_texto)
ruta_actual_texto.place(x=10, y=10)

ruta_actual = tk.Label(raiz, text=ruta, font=(mifuente, 14), bg=color_fondo, fg=color_texto)
ruta_actual.place(x=120, y=10)

texto = tk.Label(raiz, text="Selecciona un directorio:", font=(mifuente, 12), bg=color_fondo, fg=color_texto)
texto.place(x=10, y=40)

estilo.configure("customizado.TCombobox", font=(mifuente, 12))  # Definición del estilo para el menú desplegable
desplegable = ttk.Combobox(state="readonly", values=lista_directorios, style="customizado.TCombobox")
desplegable.place(x=15, y=70)

# bind -> Cuando se registra un evento determinado, se ejecuta una funcion determinada
# El evento '<<ComboboxSelected>>' es enviado cada vez que se cambia la opción seleccionada
desplegable.bind("<<ComboboxSelected>>", lambda event: actualizar_ruta(seleccion, ruta))   

estilo.configure("customizado.TButton", font=(mifuente, 12))    # Definición del estilo para los botones
boton_generar_archivo = ttk.Button(raiz, text="Generar archivo", style="customizado.TButton")
boton_generar_archivo.place(x=15, y=100, width=150, height=30)

########## ▲ INTERFAZ DE USUARIO ▲ ##########


#leer_directorios_consola(ruta, nombre_directorio)
 
archivo_resultado = open("resultado.txt", "w")
archivo_resultado.write("Contenido del directorio " + nombre_directorio + ":\n")
#leer_directorios(archivo_resultado, ruta, nombre_directorio)
archivo_resultado.close()


########## ▼ ANTIALIASING TK ▼ ##########

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except Exception as e:
    print(e)
finally:
    raiz.mainloop

########## ▲ ANTIALIASING TK ▲ ##########



