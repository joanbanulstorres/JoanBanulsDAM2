import ctypes
import cv2
import os
import random
import time
import tkinter as tk
from datetime import datetime
from PIL import Image
from PIL import ImageFilter
from tkinter import filedialog
from tkinter import ttk

########## ▼ DECLARACIÓN DE FUNCIONES ▼ ##########

def raton_dentro(e):
    e.widget['background'] = '#f2f2f2'

def raton_fuera(e):
    e.widget['background'] = '#ffffff'

# Pide al usuario seleccionar un directorio (origen) y comprueba que no esté vacío y contenga imágenes en formato 'jpg'; si no es el caso, muestra los errores pertinentes
def seleccionar_directorio_origen():
    directorio = filedialog.askdirectory()
    if directorio != "":
        if not os.listdir(directorio):
            ruta_origen.configure(bg=color_error)
            error_directorio_origen.configure(text="*Vacío")
        else:
            imagen = False
            for elemento in os.scandir(directorio):
                dividir_nombre = os.path.splitext(elemento.name)
                extension_archvio = dividir_nombre[1]
                if extension_archvio == ".jpg":
                    imagen = True
            if imagen == True:
                ruta_origen.configure(bg=color_correcto)
                error_directorio_origen.configure(text="")
            else:
                ruta_origen.configure(bg=color_error)
                error_directorio_origen.configure(text="*No contine imágenes con los formatos soportados")
        ruta_origen.configure(text=directorio)
    habilitar_btn()
    estado.configure(text="")

# Pide al usuario seleccionar un directorio (destino)
def seleccionar_directorio_destino():
    directorio = filedialog.askdirectory()
    if directorio != "":
        ruta_destino.configure(text=directorio)
        ruta_destino.configure(bg=color_correcto)
    habilitar_btn()
    estado.configure(text="")

# Habilita el botón de generación de imágenes si los directorios de origen y destino están correctamente seleccionados
def habilitar_btn():
    if ruta_origen.cget("text") != "" and error_directorio_origen.cget("text") == "":       # Si el directorio origen está bien definido   
        if ruta_destino.cget("text") != "" and error_directorio_destino.cget("text") == "": # Si el directorio destino está bien definido
           btn_color_aleatorio["state"] = "normal"
           btn_escala_grises["state"] = "normal"
    else:
        btn_color_aleatorio["state"] = "disabled"
        btn_escala_grises["state"] = "disabled"

# Aplica un filtro de color aleatorio a unas imágenes dadas y las guarda en un directorio 
def color_aleatorio():
    contador = 1
    for elemento in os.scandir(ruta_origen.cget("text")):
        dividir_nombre = os.path.splitext(elemento.name)
        extension_archvio = dividir_nombre[1]
        if extension_archvio == ".jpg":
            ruta_img = elemento.path.replace(os.sep, '/')                               # Para cambiar los back-slashes por forward-slashes
            imagen = Image.open(ruta_img)
            tabla = []
            canales = 3
            tamano = 2
            longitud_tabla = canales * pow(tamano, 3)
            for i in range(longitud_tabla):
                tabla.append(random.randint(0,1))
            imagen_modificada = imagen.filter(ImageFilter.Color3DLUT(tamano, tabla))
            nombre_img = "img" + str(contador) + " " + datetime.now().strftime('%Y-%m-%d %H-%M-%S') + ".jpg"
            ruta = ruta_destino.cget("text") + "/" + nombre_img
            imagen_modificada.save(ruta, format='JPEG')
            contador += 1
    estado.configure(text="Completado")
            
# Convierte a escala de grises unas imágenes dadas y las guarda en un directorio 
def escala_grises():
    contador = 1
    for elemento in os.scandir(ruta_origen.cget("text")):
        dividir_nombre = os.path.splitext(elemento.name)
        extension_archvio = dividir_nombre[1]
        if extension_archvio == ".jpg":
            ruta_img = elemento.path.replace(os.sep, '/')                              # Para cambiar los back-slashes por forward-slashes
            imagen = cv2.imread(ruta_img)
            imagen_modificada = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
            nombre_img = "img" + str(contador) + " " + datetime.now().strftime('%Y-%m-%d %H-%M-%S') + ".jpg"
            ruta = ruta_destino.cget("text") + "/" + nombre_img
            cv2.imwrite(ruta, imagen_modificada)
            contador += 1
    estado.configure(text="Completado")
    
########## ▲ DECLARACIÓN DE FUNCIONES ▲ ##########
    

########## ▼ VARIABLES GENERALES ▼ ##########
    
ctypes.windll.shcore.SetProcessDpiAwareness(2)
user32 = ctypes.windll.user32
anchura = user32.GetSystemMetrics(0)*0.6
altura = user32.GetSystemMetrics(1)*0.19

color_fondo = '#ffffff'
color_texto = '#000000'
color_correcto = '#90ff90'
color_error = '#ff6860'
mifuente = 'Verdana'

########## ▲ VARIABLES GENERALES ▲ ##########


########## ▼ INTERFAZ DE USUARIO ▼ ##########

########## ▼ VENTANA PRINCIPAL ▼ ##########

raiz = tk.Tk()
raiz.title("Procesador de imágenes")
raiz.geometry('%dx%d' % (anchura, altura))
raiz.resizable(0, 0)
raiz.configure(bg=color_fondo)
estilo = ttk.Style()

########## ▲ VENTANA PRINCIPAL ▲ ##########

icono_directorio = tk.PhotoImage(file='directorio.png')
icono_colores = tk.PhotoImage(file='coloraleatorio.png')
icono_grises = tk.PhotoImage(file='escalagrises.png')

########## ▼ DIRECTORIO ORIGEN ▼ ##########

texto_directorio_origen = tk.Label(raiz, text="Directorio origen:", font=(mifuente,11), bg=color_fondo, fg=color_texto)
texto_directorio_origen.grid(sticky="w", row=0, column=0, padx=(15,0), pady=10)

btn_directorio_origen = tk.Button(raiz, image=icono_directorio, bg=color_fondo, borderwidth=0, command=lambda:seleccionar_directorio_origen())
btn_directorio_origen.grid(sticky="w", row=0, column=1, padx=5, pady=10)
btn_directorio_origen.bind('<Enter>', raton_dentro)
btn_directorio_origen.bind('<Leave>', raton_fuera)

ruta_origen = tk.Label(raiz, text="", font=(mifuente,11), bg=color_fondo, fg=color_texto)
ruta_origen.grid(sticky="w", row=0, column=2, padx=5, pady=10)

error_directorio_origen = tk.Label(raiz, text="", font=(mifuente,9), bg=color_fondo, fg=color_error)
error_directorio_origen.grid(sticky="w", row=0, column=3, padx=5, pady=10)

########## ▲ DIRECTORIO ORIGEN ▲ ##########

########## ▼ DIRECTORIO DESTINO ▼ ##########

texto_directorio_destino = tk.Label(raiz, text="Directorio destino:", font=(mifuente,11), bg=color_fondo, fg=color_texto)
texto_directorio_destino.grid(sticky="w", row=1, column=0, padx=(15,0), pady=(15,10))

btn_directorio_destino = tk.Button(raiz, image=icono_directorio, bg=color_fondo, borderwidth=0, command=lambda:seleccionar_directorio_destino())
btn_directorio_destino.grid(sticky="w", row=1, column=1, padx=5, pady=10)
btn_directorio_destino.bind('<Enter>', raton_dentro)
btn_directorio_destino.bind('<Leave>', raton_fuera)

ruta_destino = tk.Label(raiz, text="", font=(mifuente,11), bg=color_fondo, fg=color_texto)
ruta_destino.grid(sticky="w", row=1, column=2, padx=5, pady=10)

error_directorio_destino = tk.Label(raiz, text="", font=(mifuente,9), bg=color_fondo, fg=color_error)
error_directorio_destino.grid(sticky="w", row=1, column=3, padx=5, pady=10)

########## ▲ DIRECTORIO ORIGEN ▲ ##########

formatos = tk.Label(raiz, text="Formatos soportados: jpg", font=(mifuente,9), bg=color_fondo, fg=color_texto)
formatos.grid(sticky="w", row=2, column=0, columnspan=4, padx=(15,0), pady=(5,10))

########## ▼ BOTONES PARA APLICAR FILTROS ▼ ##########

marco_botones = tk.Frame(raiz, bg=color_fondo)

btn_color_aleatorio = tk.Button(marco_botones, image=icono_colores, bg=color_fondo, borderwidth=0, command=lambda:color_aleatorio())
btn_color_aleatorio.pack(side="left", fill=None, expand=False)
btn_color_aleatorio.bind('<Enter>', raton_dentro)
btn_color_aleatorio.bind('<Leave>', raton_fuera)
btn_color_aleatorio["state"] = "disabled"

btn_escala_grises = tk.Button(marco_botones, image=icono_grises, bg=color_fondo, borderwidth=0, command=lambda:escala_grises())
btn_escala_grises.pack(side="left", fill=None, expand=False)
btn_escala_grises.bind('<Enter>', raton_dentro)
btn_escala_grises.bind('<Leave>', raton_fuera)
btn_escala_grises["state"] = "disabled"

estado = tk.Label(marco_botones, text="", font=(mifuente,9), bg=color_fondo, fg=color_correcto)
estado.pack(side="left", fill=None, expand=False, padx=5)

marco_botones.grid(sticky="w", row=3, column=0, padx=(15,0), pady=(5,10))

########## ▲ BOTONES PARA APLICAR FILTROS ▲ ##########

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
