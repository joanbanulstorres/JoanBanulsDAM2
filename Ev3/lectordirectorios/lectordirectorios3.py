import os
import datetime
import tkinter as tk
from tkinter import ttk
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)

########## ▼ DECLARACIÓN DE FUNCIONES ▼ ##########

# Añade a una lista todos los subdirectorios de un directorio especificado
def obtener_subdirectorios(directorio, lista_directorios):  
    resultado = os.scandir(directorio)
    lista_directorios.clear()
    for elemento in resultado:
        if elemento.is_dir():                                       # Se seleccionan únicamente los directorios
            nombre_subdirectorio = elemento.name
            lista_directorios.append(nombre_subdirectorio)

# Escribe una ruta a partir de los elementos de una lista  
def escribir_ruta(lista_ruta):
    ruta_escrita = "\\".join(lista_ruta)
    return ruta_escrita
    
# Capta la opción seleccionada del menú desplegable para actualizar la ruta mostrada al usuario así como los subdirectorios del menú   
def actualizar_ruta(seleccion, lista_directorios):
    seleccion = desplegable.get()
    lista_ruta.append(seleccion)                                    # Se añade el elemento seleccionado a la lista de la ruta
    global nueva_ruta
    nueva_ruta = escribir_ruta(lista_ruta)                          # Se escribe la ruta en el formato adecuado
    ruta_actual.configure(text=nueva_ruta)                          # Se actualiza la ruta mostrada al usuario
    obtener_subdirectorios(nueva_ruta, lista_directorios)           # Se obtienen los subdirectorios del nuevo directorio
    desplegable['values'] = lista_directorios                       # Se actualiza el menú desplegable

# Lee las propiedades de los archivos de un directorio especificado y de sus subdirectorios y las vuelca en un archivo especificado
def leer_directorios(nueva_ruta, archivo_resultado):
    #ruta = ruta_inicial + "\\" + nombre_directorio
    resultado = os.scandir(nueva_ruta)
    for elemento in resultado:
        if elemento.is_file():
            #Nombre
            archivo_resultado.write("\nNombre:\t" + elemento.name)
            # Ruta
            archivo_resultado.write("\nRuta:\t\t" + elemento.path)
            # Tamaño
            archivo_resultado.write("\nTamaño:\t" + str(os.path.getsize(elemento.path)) + " bytes")
            # Fecha de creación
            fecha_creado_ms = os.path.getctime(elemento.path)                                           # tiempo en ms
            fecha_creado = str(datetime.datetime.fromtimestamp(fecha_creado_ms))                        # conversión a fecha
            archivo_resultado.write("\nCreado:\t" + fecha_creado)
            # Fecha de modificación
            fecha_modificado_ms = os.path.getmtime(elemento.path)
            fecha_modificado = str(datetime.datetime.fromtimestamp(fecha_modificado_ms))
            archivo_resultado.write("\nModificado:\t" + fecha_modificado)
            # Salto de línea
            archivo_resultado.write("\n")
        if elemento.is_dir():
            nombre_subdirectorio = elemento.name
            ruta_subdirectorio = elemento.path
            archivo_resultado.write("\n\nContenido del subdirectorio " + nombre_subdirectorio + ":\n")
            # Recursividad para analizar los subdirectorios
            leer_directorios(ruta_subdirectorio, archivo_resultado)

# Abre un archivo, guarda en él cierta información mediante otra función, lo cierra y muestra un mensaje de éxito
def generar_archivo(nueva_ruta):
    archivo_resultado = open("resultado.txt", "w")
    archivo_resultado.write("Contendio del directorio seleccionado:")
    leer_directorios(nueva_ruta, archivo_resultado)
    archivo_resultado.close()
    mensaje = tk.Label(raiz, text="✓", font=("Arial", 20), bg=color_fondo, fg="#03C04A")
    mensaje.place(x=170, y=85)

def eliminar_ruta():
    print("Ruta eliminada")
            
########## ▲ DECLARACIÓN DE FUNCIONES ▲ ##########
            
            
########## ▼ DECLARACIÓN DE VARIABLES GENERALES ▼ ##########

#ruta = r"C:\Users\joan"
lista_directorios = []                          # Subdirectorios contenidos en un directorio          
lista_ruta = ["C:","Users"]      
ruta_inicial = escribir_ruta(lista_ruta)        # Ruta inicial
seleccion = ""
mifuente = "Verdana"
color_fondo = "#FFFFFF"
color_texto = "#000000"

# Definición de los directorios iniciales para el menú desplegable
obtener_subdirectorios(ruta_inicial, lista_directorios)

########## ▲ DECLARACIÓN DE VARIABLES GENERALES ▲ ##########


########## ▼ INTERFAZ DE USUARIO ▼ ##########

raiz = tk.Tk()
raiz.title("Lector de directorios")
raiz.geometry('1000x150+100+100')
raiz.configure(bg=color_fondo)
raiz.attributes("-topmost", True)
#raiz.attributes("-alpha", 0.95)
raiz.resizable(0,0)
estilo = ttk.Style()

# RUTA ACTUAL
ruta_actual_texto = tk.Label(raiz, text="Ruta actual:", font=(mifuente, 14), bg=color_fondo, fg="#F28C28")
ruta_actual_texto.place(x=10, y=10)
ruta_actual = tk.Label(raiz, text=escribir_ruta(lista_ruta), font=(mifuente, 14), bg=color_fondo, fg=color_texto)
ruta_actual.place(x=130, y=10)

# SELECCIONAR DIRECTORIO
texto = tk.Label(raiz, text="Selecciona un directorio:", font=(mifuente, 12), bg=color_fondo, fg=color_texto)
texto.place(x=10, y=50)

# MENÚ DESPLEGABLE
estilo.configure("customizado.TCombobox", font=(mifuente, 12))  # Definición del estilo para el menú desplegable
desplegable = ttk.Combobox(state="readonly", values=lista_directorios, style="customizado.TCombobox")
desplegable.place(x=220, y=53)
# bind -> Cuando se registra un evento determinado, se ejecuta una funcion determinada
# El evento '<<ComboboxSelected>>' es enviado cada vez que se cambia la opción seleccionada
desplegable.bind("<<ComboboxSelected>>", lambda event: actualizar_ruta(seleccion, lista_directorios))   

# BOTÓN GENERAR ARCHIVO
estilo.configure("customizado.TButton", font=(mifuente, 12))    # Definición del estilo para los botones
boton_generar_archivo = ttk.Button(raiz, text="Generar archivo", style="customizado.TButton", command=lambda:generar_archivo(nueva_ruta))
boton_generar_archivo.place(x=15, y=90, width=150, height=30)

# BOTÓN DIRECTORIO ANTERIOR
icono_anterior = tk.PhotoImage(file='anterior.png')
boton_ruta_anterior = tk.Button(raiz, image=icono_anterior, command=eliminar_ruta, bg=color_fondo, borderwidth=0)
boton_ruta_anterior.pack(anchor=tk.NE, padx=100, pady=10)

# BOTÓN ELIMINAR RUTA
icono_eliminar = tk.PhotoImage(file='eliminar.png')
boton_eliminar_ruta = tk.Button(raiz, image=icono_eliminar, command=eliminar_ruta, bg=color_fondo, borderwidth=0)
boton_eliminar_ruta.pack(anchor=tk.NE, padx=10, pady=10)

########## ▲ INTERFAZ DE USUARIO ▲ ##########


########## ▼ ANTIALIASING TK ▼ ##########

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except Exception as e:
    print(e)
finally:
    raiz.mainloop

########## ▲ ANTIALIASING TK ▲ ##########
