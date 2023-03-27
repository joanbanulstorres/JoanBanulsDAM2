import os
import datetime
import tkinter as tk
from tkinter import ttk
import sys

sys.setrecursionlimit(1500)

########## ▼ DECLARACIÓN DE FUNCIONES ▼ ##########

# Añade a una lista todos los subdirectorios de un directorio especificado
def obtener_subdirectorios(directorio, lista_subdirectorios):  
    resultado = os.scandir(directorio)
    lista_subdirectorios.clear()
    for elemento in resultado:
        if elemento.is_dir():                                       # Se añaden a la lista únicamente los directorios
            lista_subdirectorios.append(elemento.name)
            
# Escribe una ruta a partir de los elementos de una lista  
def escribir_ruta(lista_ruta):
    ruta_escrita = "\\".join(lista_ruta)
    return ruta_escrita
    
# Capta la opción seleccionada del menú desplegable para actualizar la ruta mostrada al usuario así como los subdirectorios del menú   
def actualizar_ruta(seleccion, lista_subdirectorios):
    seleccion = desplegable.get()
    if seleccion != "":
        lista_ruta.append(seleccion)                                # Se añade el elemento seleccionado a la lista de la ruta
    global nueva_ruta
    nueva_ruta = escribir_ruta(lista_ruta)
    print(nueva_ruta)
    ruta_actual.configure(text=nueva_ruta)                          # Se actualiza la ruta mostrada al usuario
    obtener_subdirectorios(nueva_ruta, lista_subdirectorios)        # Se obtienen los subdirectorios del nuevo directorio
    desplegable['values'] = lista_subdirectorios                    # Se actualiza el menú desplegable

# Lee las propiedades de los archivos de un directorio especificado y de sus subdirectorios y las vuelca en un archivo especificado
def leer_directorios(nueva_ruta, archivo_resultado):
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

def crear_archivo_xml(directorio, archivo_resultado):
    # Variables
    nombre_directorio = str(os.path.basename(directorio))
    ubicacion_directorio = str(os.path.dirname(directorio))
    tamano_directorio = str(os.path.getsize(directorio)) + " bytes"
    creado_directorio = str(datetime.datetime.fromtimestamp(os.path.getctime(directorio)))
    modificado_directorio = str(datetime.datetime.fromtimestamp(os.path.getmtime(directorio)))
    # Inyecciones XML
    archivo_resultado.write("<?xml version=\"1.0\"?>" + "\n")
    archivo_resultado.write("<directorio>" + "\n")
    archivo_resultado.write("\t" + "<nombre>" + nombre_directorio + "</nombre>" + "\n")
    archivo_resultado.write("\t" + "<ubicacion>" + ubicacion_directorio + "</ubicacion>" + "\n")
    archivo_resultado.write("\t" + "<tamano>" + tamano_directorio + "</tamano>" + "\n")
    archivo_resultado.write("\t" + "<creado>" + creado_directorio + "</creado>" + "\n")
    archivo_resultado.write("\t" + "<modificado>" + modificado_directorio + "</modificado>" + "\n")
    archivo_resultado.write("\t" + "<contenido>" + "\n")
    resultado = os.scandir(directorio)
    for elemento in resultado:
        if elemento.is_file():   
            archivo_resultado.write("\t\t" + "<archivo>" + "\n")
            archivo_resultado.write("\t\t\t" + "<nombre>" + elemento.name + "</nombre>" + "\n")
            archivo_resultado.write("\t\t\t" + "<ubicacion>" + elemento.path + "</ubicacion>" + "\n")
            archivo_resultado.write("\t\t\t" + "<tamano>" + str(os.path.getsize(elemento.path)) + " bytes" + "</tamano>" + "\n")
            archivo_resultado.write("\t\t\t" + "<creado>" + str(datetime.datetime.fromtimestamp(os.path.getctime(elemento.name))) + "</creado>" + "\n")
            archivo_resultado.write("\t\t\t" + "<modificado>" + str(datetime.datetime.fromtimestamp(os.path.getctime(elemento.name))) + "</modificado>" + "\n")
            archivo_resultado.write("\t\t" + "</archivo>" + "\n")
    archivo_resultado.write("</contenido>" + "\n")
    
    
##    for elemento in resultado:
##        if elemento.is_file():
##            #Nombre
##            archivo_resultado.write("\nNombre:\t" + elemento.name)
##            # Ruta
##            archivo_resultado.write("\nRuta:\t\t" + elemento.path)
##            # Tamaño
##            archivo_resultado.write("\nTamaño:\t" + str(os.path.getsize(elemento.path)) + " bytes")
##            # Fecha de creación
##            fecha_creado_ms = os.path.getctime(elemento.path)                                           # tiempo en ms
##            fecha_creado = str(datetime.datetime.fromtimestamp(fecha_creado_ms))                        # conversión a fecha
##            archivo_resultado.write("\nCreado:\t" + fecha_creado)
##            # Fecha de modificación
##            fecha_modificado_ms = os.path.getmtime(elemento.path)
##            fecha_modificado = str(datetime.datetime.fromtimestamp(fecha_modificado_ms))
##            archivo_resultado.write("\nModificado:\t" + fecha_modificado)
##            # Salto de línea
##            archivo_resultado.write("\n")
##        if elemento.is_dir():
##            nombre_subdirectorio = elemento.name
##            ruta_subdirectorio = elemento.path
##            archivo_resultado.write("\n\nContenido del subdirectorio " + nombre_subdirectorio + ":\n")
##            # Recursividad para analizar los subdirectorios
##            leer_directorios(ruta_subdirectorio, archivo_resultado)

    archivo_resultado.write("</directorio>")


# Abre un archivo, guarda en él cierta información mediante otra función, lo cierra y muestra un mensaje de éxito
def generar_archivo(nueva_ruta):
    archivo_resultado = open("resultado.xml", "w")
    crear_archivo_xml(nueva_ruta, archivo_resultado)
    archivo_resultado.close()
    mensaje = tk.Label(raiz, text="✓", font=("Arial", 20), bg=color_fondo, fg="#03C04A")
    mensaje.place(x=170, y=85)

def directorio_anterior():
    if 'nueva_ruta' in globals():
        print(nueva_ruta)

def mostrar_ruta(ruta):
    nuevaruta = escribir_ruta(ruta)
    obtener_subdirectorios(nuevaruta, lista_subdirectorios)
    print(lista_subdirectorios)
    ruta_actual.configure(text=nuevaruta)                          # Se actualiza la ruta mostrada al usuario
    desplegable['values'] = lista_subdirectorios

def reiniciar_ruta(lista_ruta_inicial, lista_ruta):
    if 'nueva_ruta' in globals(): 
##        global nueva_ruta
##        nueva_ruta = escribir_ruta(lista_ruta_inicial)
        print(lista_ruta)
        print(lista_ruta_inicial)
        lista_ruta = lista_ruta_inicial
        print(lista_ruta)
        return lista_ruta
##        print(nueva_ruta)
##        obtener_subdirectorios(nueva_ruta, lista_subdirectorios)
##        print(lista_subdirectorios)
##        ruta_actual.configure(text=nueva_ruta)                          # Se actualiza la ruta mostrada al usuario
##        desplegable['values'] = lista_subdirectorios
            
########## ▲ DECLARACIÓN DE FUNCIONES ▲ ##########
            
            
########## ▼ DECLARACIÓN DE VARIABLES GENERALES ▼ ##########

#ruta = r"C:\Users\joan"
lista_subdirectorios = []          
lista_ruta = ["C:","Users"]
lista_ruta_inicial = ["C:","Users"]
ruta_inicial = escribir_ruta(lista_ruta)
seleccion = ""
mifuente = "Verdana"
color_fondo = "#FFFFFF"
color_texto = "#000000"

if 'nueva_ruta' in globals():
    print(nueva_ruta)

# Definición de los directorios iniciales para el menú desplegable
obtener_subdirectorios(ruta_inicial, lista_subdirectorios)

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
desplegable = ttk.Combobox(state="readonly", values=lista_subdirectorios, style="customizado.TCombobox")
desplegable.place(x=220, y=53)
# bind -> Cuando se registra un evento determinado, se ejecuta una funcion determinada
# El evento '<<ComboboxSelected>>' es enviado cada vez que se cambia la opción seleccionada
desplegable.bind("<<ComboboxSelected>>", lambda event: actualizar_ruta(seleccion, lista_subdirectorios))   

estilo.configure("customizado.TButton", font=(mifuente, 12))    # Definición del estilo para los botones

# BOTÓN GENERAR ARCHIVO
icono_nuevodoc = tk.PhotoImage(file='nuevodoc.png')
boton_generar_archivo = ttk.Button(raiz, image=icono_nuevodoc, style="customizado.TButton", command=lambda:generar_archivo(nueva_ruta))
boton_generar_archivo.place(x=15, y=90, width=40, height=40)

# BOTÓN DIRECTORIO ANTERIOR
icono_anterior = tk.PhotoImage(file='anterior.png')
boton_directorio_anterior = ttk.Button(raiz, image=icono_anterior, command=lambda:directorio_anterior())
boton_directorio_anterior.place(x=910, y=10, width=40, height=40)

# BOTÓN REINICIAR RUTA
icono_eliminar = tk.PhotoImage(file='eliminar.png')
boton_reiniciar_ruta = ttk.Button(raiz, image=icono_eliminar, command=lambda:mostrar_ruta(reiniciar_ruta(lista_ruta_inicial, lista_ruta)))
boton_reiniciar_ruta.place(x=950, y=10, width=40, height=40)

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
