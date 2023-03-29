import os
import datetime
import time
import tkinter as tk
from tkinter import ttk
from tkinter import *
import sys

sys.setrecursionlimit(5000)

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
def actualizar_ruta(lista_subdirectorios):
    seleccion_directorio = desplegable_directorio.get()
    if seleccion_directorio != "":
        lista_ruta.append(seleccion_directorio)                     # Se añade el elemento seleccionado a la lista de la ruta
    global nueva_ruta
    nueva_ruta = escribir_ruta(lista_ruta)
    ruta_actual.configure(text=nueva_ruta)                          # Se actualiza la ruta mostrada al usuario
    obtener_subdirectorios(nueva_ruta, lista_subdirectorios)        # Se obtienen los subdirectorios del nuevo directorio
    desplegable_directorio['values'] = lista_subdirectorios         # Se actualiza el menú desplegable
    
def directorio_anterior():
    if 'nueva_ruta' in globals():
        print(nueva_ruta)

def mostrar_ruta(ruta):
    nuevaruta = escribir_ruta(ruta)
    obtener_subdirectorios(nuevaruta, lista_subdirectorios)
    print(lista_subdirectorios)
    ruta_actual.configure(text=nuevaruta)                           # Se actualiza la ruta mostrada al usuario
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

# El color de fondo de los botones cambia cuando se les pasa el ratón por encima
def raton_dentro(e):
    e.widget['background'] = '#CCEBFF'
    
def raton_fuera(e):
    e.widget['background'] = '#FFFFFF'

# Lee las propiedades de un directorio especificado y de sus archivos y subdirectorios contenidos, y las vuelca en formato txt en un archivo
def insertar_txt(directorio, archivo_resultado, tab):
    resultado = os.scandir(directorio)
    archivo_resultado.write(tab + "Nombre:\t" + str(os.path.basename(directorio)) + "\n")
    archivo_resultado.write(tab + "Ubicación:\t" + str(os.path.dirname(directorio)) + "\n")
    archivo_resultado.write(tab + "Tamaño:\t" + str(os.path.getsize(directorio)) + " bytes\n")
    archivo_resultado.write(tab + "Creado:\t" + str(datetime.datetime.fromtimestamp(os.path.getctime(directorio))) + "\n")
    archivo_resultado.write(tab + "Modificado:\t" + str(datetime.datetime.fromtimestamp(os.path.getmtime(directorio))) + "\n")
    archivo_resultado.write(tab + "Contenido:\n\n")
    tab += "\t"
    for elemento in resultado:
        if elemento.is_file():
            archivo_resultado.write(tab + "Nombre:\t" + elemento.name + "\n")
            archivo_resultado.write(tab + "Ubicación:\t" + str(os.path.dirname(directorio)) + "\n")
            archivo_resultado.write(tab + "Tamaño:\t" + str(os.path.getsize(elemento.path)) + " bytes\n")
            archivo_resultado.write(tab + "Creado:\t" + str(datetime.datetime.fromtimestamp(os.path.getctime(elemento.path))) + "\n")
            archivo_resultado.write(tab + "Modificado:\t" + str(datetime.datetime.fromtimestamp(os.path.getmtime(elemento.path))) + "\n\n")
        if elemento.is_dir():
            insertar_txt(elemento.path, archivo_resultado, tab)     # Recursividad para analizar los subdirectorios

# Lee las propiedades de un directorio especificado y de sus archivos y subdirectorios contenidos, y las vuelca en formato xml en un archivo
def insertar_xml(directorio, archivo_resultado, tab):
    archivo_resultado.write(tab + "<directorio id='" + (str(os.path.basename(directorio))).replace(" ", "")+ "'>" + "\n")
    tab += "\t" 
    archivo_resultado.write(tab + "<nombre>" + str(os.path.basename(directorio)) + "</nombre>" + "\n")
    archivo_resultado.write(tab + "<ubicacion>" + str(os.path.dirname(directorio)) + "</ubicacion>" + "\n")
    archivo_resultado.write(tab + "<tamano>" + str(os.path.getsize(directorio)) + " bytes" + "</tamano>" + "\n")
    archivo_resultado.write(tab + "<creado>" + str(datetime.datetime.fromtimestamp(os.path.getctime(directorio))) + "</creado>" + "\n")
    archivo_resultado.write(tab + "<modificado>" + str(datetime.datetime.fromtimestamp(os.path.getmtime(directorio))) + "</modificado>" + "\n")
    archivo_resultado.write(tab + "<contenido>" + "\n")
    tab += "\t"
    for elemento in os.scandir(directorio):
        if elemento.is_file():   
            archivo_resultado.write(tab + "<archivo>" + "\n")
            tab += "\t"
            archivo_resultado.write(tab + "<nombre>" + elemento.name + "</nombre>" + "\n")
            archivo_resultado.write(tab + "<ubicacion>" + str(os.path.dirname(elemento.path)) + "</ubicacion>" + "\n")
            archivo_resultado.write(tab + "<tamano>" + str(os.path.getsize(elemento.path)) + " bytes" + "</tamano>" + "\n")
            archivo_resultado.write(tab + "<creado>" + str(datetime.datetime.fromtimestamp(os.path.getctime(elemento.path))) + "</creado>" + "\n")
            archivo_resultado.write(tab + "<modificado>" + str(datetime.datetime.fromtimestamp(os.path.getmtime(elemento.path))) + "</modificado>" + "\n")
            tab = tab[:-1]
            archivo_resultado.write(tab + "</archivo>" + "\n")
        if elemento.is_dir():
            insertar_xml(elemento.path, archivo_resultado, tab)     # Recursividad para leer los subdirectorios
    tab = tab[:-1]
    archivo_resultado.write(tab + "</contenido>" + "\n")
    tab = tab[:-1]
    if tab != "":            
        archivo_resultado.write(tab + "</directorio>" + "\n")
    else:
        archivo_resultado.write(tab + "</directorio>")

# Lee las propiedades de un directorio especificado y de sus archivos y subdirectorios contenidos, y las vuelca en formato json en un archivo
def insertar_json(directorio, archivo_resultado, tab):
    archivo_resultado.write(tab + "{\"directorio\" : {\n")
    tab += "\t"
    archivo_resultado.write(tab + "\"nombre\" : \"" + str(os.path.basename(directorio)) + "\",\n")
    archivo_resultado.write(tab + "\"ubicacion\" : \"" + str(os.path.dirname(directorio)) + "\",\n")
    archivo_resultado.write(tab + "\"tamano\" : \"" + str(os.path.getsize(directorio)) + "\",\n")
    archivo_resultado.write(tab + "\"creado\" : \"" + str(datetime.datetime.fromtimestamp(os.path.getctime(directorio))) + "\",\n")
    archivo_resultado.write(tab + "\"modificado\" : \"" + str(datetime.datetime.fromtimestamp(os.path.getmtime(directorio))) + "\",\n")
    archivo_resultado.write(tab + "\"contenido\" : {\n")
    tab += "\t"
    resultado = os.scandir(directorio)
    #print(len(list(resultado)))
    print(list(resultado))
    #print(list(resultado)[0])
    
    for elemento in os.scandir(directorio):
        if elemento.is_file():
            print(list(os.scandir(directorio)).index(elemento))
            archivo_resultado.write(tab + "\"archivo\" : {\n")
            tab += "\t"
            archivo_resultado.write(tab + "\"nombre\" : \"" + elemento.name + "\",\n")
            archivo_resultado.write(tab + "\"ubicacion\" : \"" + str(os.path.dirname(elemento.path)) + "\",\n")
            archivo_resultado.write(tab + "\"tamano\" : \"" + str(os.path.getsize(elemento.path)) + "\",\n")
            archivo_resultado.write(tab + "\"creado\" : \"" + str(datetime.datetime.fromtimestamp(os.path.getctime(elemento.path))) + "\",\n")
            archivo_resultado.write(tab + "\"modificado\" : \"" + str(datetime.datetime.fromtimestamp(os.path.getmtime(elemento.path))) + "\"\n")
            tab = tab[:-1]
            # Para quitar la coma del último archivo{...},
            if list(resultado).index(elemento.name) != len(list(resultado)): 
                archivo_resultado.write(tab + "},\n")
            else:
                archivo_resultado.write(tab + "}\n")
    tab = tab[:-1]
    archivo_resultado.write(tab + "}\n")
    tab = tab[:-1]
    archivo_resultado.write(tab + "}")

# Crea un archivo del directorio y con el formato especificados
def generar_archivo(directorio):
    #barra_progreso = ttk.Progressbar(mode = "indeterminate")
    #barra_progreso.place(x=600, y=55)
    #barra_progreso.start()                  
    formato = desplegable_formato.get()
    if formato != "":
        try:
            error_formato.destroy()
        except Exception as e:
            print(e)
        finally:
            tab = ""
            if formato == "txt":
                archivo_resultado = open("resultado.txt", 'w')
                insertar_txt(directorio, archivo_resultado, tab)
            elif formato == "xml":
                archivo_resultado = open("resultado.xml", 'w')
                archivo_resultado.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>" + "\n")
                insertar_xml(directorio, archivo_resultado, tab)
            elif formato == "json":
                archivo_resultado = open("resultado.json", 'w')
                insertar_json(directorio, archivo_resultado, tab)
            else:
                print("Formato de archivo incorrecto")
            archivo_resultado.close()
            mensaje = tk.Label(raiz, text="✓", font=('Arial', 20), bg=color_fondo, fg='#03C04A')
            mensaje.place(x=810, y=63)
            #time.sleep(3)
            #barra_progreso.stop()
            #barra_progreso.destroy()
    else:
        error_formato = tk.Label(raiz, text="*Selecciona un formato", font=(mifuente, 11), bg=color_fondo, fg='#ff0000')
        error_formato.place(x=680 , y=100)
            
########## ▲ DECLARACIÓN DE FUNCIONES ▲ ##########
            
            
########## ▼ DECLARACIÓN DE VARIABLES GENERALES ▼ ##########

lista_subdirectorios = []          
lista_ruta = ['C:','Users']
lista_ruta_inicial = ['C:','Users']
lista_formatos = ['txt', 'xml', 'json']
#nueva_ruta = ""
ruta_inicial = escribir_ruta(lista_ruta)
seleccion = ""
mifuente = 'Verdana'
color_fondo = '#FFFFFF'
color_texto = '#000000'

# Definición de los directorios iniciales para el menú desplegable
obtener_subdirectorios(ruta_inicial, lista_subdirectorios)

########## ▲ DECLARACIÓN DE VARIABLES GENERALES ▲ ##########


########## ▼ INTERFAZ DE USUARIO ▼ ##########

raiz = tk.Tk()
raiz.title("Lector de directorios")
raiz.geometry('1000x150+100+100')
raiz.configure(bg=color_fondo)
#raiz.attributes('-topmost', True)
raiz.resizable(0,0)
estilo = ttk.Style()

# RUTA ACTUAL
ruta_actual = tk.Label(raiz, text=escribir_ruta(lista_ruta), font=(mifuente, 14), bg=color_fondo, fg=color_texto)
ruta_actual.place(x=20, y=20)

# SELECCIONAR DIRECTORIO
texto = tk.Label(raiz, text="Directorio:", font=(mifuente, 12), bg=color_fondo, fg=color_texto)
texto.place(x=20, y=70)

# MENÚ DESPLEGABLE DIRECTORIO
raiz.option_add('*TCombobox*Listbox*Font', (mifuente, 12))
desplegable_directorio = ttk.Combobox(state='readonly', values=lista_subdirectorios, font=(mifuente, 12))
desplegable_directorio.place(x=115, y=70)
# bind -> Cuando se registra un evento determinado, se ejecuta una funcion determinada
# El evento '<<ComboboxSelected>>' es enviado cada vez que se cambia la opción seleccionada
desplegable_directorio.bind('<<ComboboxSelected>>', lambda event: actualizar_ruta(lista_subdirectorios))   

# SELECCIONAR FORMATO
texto = tk.Label(raiz, text="Formato de archivo:", font=(mifuente, 12), bg=color_fondo, fg=color_texto)
texto.place(x=375, y=70)

# MENÚ DESPLEGABLE FORMATO
desplegable_formato = ttk.Combobox(state='readonly', values=lista_formatos, font=(mifuente, 12))
desplegable_formato.place(x=550, y=70, width=100)

# BOTÓN CREAR ARCHIVO TXT
#icono_crear_archivo = tk.PhotoImage(file='img/archivo_nuevo.png')
estilo.configure('personalizado.TButton', font=(mifuente, 12),)
boton_crear_archivo = ttk.Button(raiz, text="Crear archivo", style='personalizado.TButton', command=lambda:generar_archivo(nueva_ruta))
boton_crear_archivo.place(x=680, y=67, width=120, height=30)
#boton_crear_archivo.bind("<Enter>", raton_dentro)
#boton_crear_archivo.bind("<Leave>", raton_fuera)

#estilo.configure("customizado.TButton", font=(mifuente, 12))    # Definición del estilo para los botones

### BOTÓN GENERAR ARCHIVO TXT
##icono_archivo_txt = tk.PhotoImage(file='img/nuevodoc_txt.png')
##boton_archivo_txt = tk.Button(raiz, image=icono_archivo_txt, bg=color_fondo, borderwidth=0, command=lambda:generar_archivo(nueva_ruta, "txt"))
##boton_archivo_txt.place(x=550, y=65, width=40, height=40)
##boton_archivo_txt.bind("<Enter>", raton_dentro)
##boton_archivo_txt.bind("<Leave>", raton_fuera)
##
### BOTÓN GENERAR ARCHIVO XML
##icono_archivo_xml = tk.PhotoImage(file='img/nuevodoc_xml.png')
##boton_archivo_xml = tk.Button(raiz, image=icono_archivo_xml, bg=color_fondo, borderwidth=0, command=lambda:generar_archivo(nueva_ruta, "xml"))
##boton_archivo_xml.place(x=590, y=65, width=40, height=40)
##boton_archivo_xml.bind("<Enter>", raton_dentro)
##boton_archivo_xml.bind("<Leave>", raton_fuera)
##
### BOTÓN GENERAR ARCHIVO JSON
##icono_archivo_json = tk.PhotoImage(file='img/nuevodoc_json.png')
##boton_archivo_json = tk.Button(raiz, image=icono_archivo_json, bg=color_fondo, borderwidth=0, command=lambda:generar_archivo(nueva_ruta, "json"))
##boton_archivo_json.place(x=630, y=65, width=40, height=40)
##boton_archivo_json.bind("<Enter>", raton_dentro)
##boton_archivo_json.bind("<Leave>", raton_fuera)

# BOTÓN DIRECTORIO ANTERIOR
icono_anterior = tk.PhotoImage(file='img/anterior.png')
boton_directorio_anterior = tk.Button(raiz, image=icono_anterior, bg=color_fondo, borderwidth=0, command=lambda:directorio_anterior())
boton_directorio_anterior.place(x=900, y=15, width=40, height=40)
boton_directorio_anterior.bind('<Enter>', raton_dentro)
boton_directorio_anterior.bind('<Leave>', raton_fuera)

# BOTÓN REINICIAR RUTA
icono_reiniciar = tk.PhotoImage(file='img/reiniciar.png')
boton_reiniciar_ruta = tk.Button(raiz, image=icono_reiniciar, bg=color_fondo, borderwidth=0, command=lambda:mostrar_ruta(reiniciar_ruta(lista_ruta_inicial, lista_ruta)))
boton_reiniciar_ruta.place(x=940, y=15, width=40, height=40)
boton_reiniciar_ruta.bind('<Enter>', raton_dentro)
boton_reiniciar_ruta.bind('<Leave>', raton_fuera)


########## ▼ ANTIALIASING TKINTER ▼ ##########

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except Exception as e:
    print(e)
finally:
    raiz.mainloop

########## ▲ ANTIALIASING TKINTER ▲ ##########
    

########## ▲ INTERFAZ DE USUARIO ▲ ##########
