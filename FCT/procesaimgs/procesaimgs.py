import ctypes
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def raton_dentro(e):
    e.widget['background'] = '#f2f2f2'

def raton_fuera(e):
    e.widget['background'] = '#ffffff'

def seleccionar_directorio():
    directorio = filedialog.askdirectory()
    if directorio != "":
        for elemento in os.scandir(directorio):
            dividir_nombre = os.path.splitext(elemento.name)
            extension_archvio = dividir_nombre[1]
            if extension_archvio == ".jpg":
                print(elemento.name)
    
ctypes.windll.shcore.SetProcessDpiAwareness(2)
user32 = ctypes.windll.user32
resolucion = user32.GetSystemMetrics(0)*0.5, user32.GetSystemMetrics(1)*0.5

color_fondo = '#ffffff'
color_texto = '#000000'
mifuente = 'Verdana'

########## ▼ INTERFAZ DE USUARIO ▼ ##########

########## ▼ VENTANA PRINCIPAL ▼ ##########

raiz = tk.Tk()
raiz.title("Procesador de imágenes")
raiz.geometry('%dx%d' % resolucion)
raiz.configure(bg=color_fondo)

########## ▲ VENTANA PRINCIPAL ▲ ##########


########## ▼ WIDGETS ▼ ##########

texto_seleccionar_directorio = tk.Label(raiz, text="Selecciona un directorio: ", font=(mifuente,11), bg=color_fondo, fg=color_texto)
texto_seleccionar_directorio.grid(row=1, column=1, padx=(10,0), pady=10)

icono_directorio = tk.PhotoImage(file='directorio.png')
btn_seleccionar_directorio = tk.Button(raiz, image=icono_directorio, bg=color_fondo, borderwidth=0, command=lambda:seleccionar_directorio())
btn_seleccionar_directorio.grid(row=1, column=2)
btn_seleccionar_directorio.bind('<Enter>', raton_dentro)
btn_seleccionar_directorio.bind('<Leave>', raton_fuera)

########## ▲ WIDGETS ▲ ##########


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
