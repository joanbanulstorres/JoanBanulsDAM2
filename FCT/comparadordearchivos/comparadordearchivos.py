import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import os
import ctypes

def seleccionar_archivo(menu, nombre_archivo_texto):
    ruta = askopenfilename()
    nombre_archivo = str(os.path.basename(ruta))
    nombre_archivo_texto.configure(text=nombre_archivo)
    #archivo = open(ruta, 'r')
    
    
color_fondo = '#ffffff'
color_texto = '#000000'
color_fondo_marco = "#f9f9f9"
color_linea_marco = "#000000"

ctypes.windll.shcore.SetProcessDpiAwareness(2)

user32 = ctypes.windll.user32
resolucion = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

anchura_marco = (user32.GetSystemMetrics(0))
altura_marco = (user32.GetSystemMetrics(1))

########## ▼ INTERFAZ DE USUARIO ▼ ##########

raiz = tk.Tk()
raiz.title("Comparador de archivos")
raiz.state('zoomed')
raiz.geometry('%dx%d' % resolucion)
raiz.configure(bg=color_fondo)

########## ▼ MENÚ ▼ ##########

menu = tk.Frame(raiz)
menu.config(width=anchura_marco, height=80, bg=color_fondo_marco, highlightbackground=color_linea_marco, highlightthickness=2)
menu.pack(padx=10, pady=(10,5), anchor="w")

boton_archivo1 = ttk.Button(menu, text="Seleccionar archivo", command=lambda: seleccionar_archivo(menu, nombre_archivo1))
boton_archivo1.grid(row=1, column=1)
boton_archivo2 = ttk.Button(menu, text="Seleccionar archivo", command=lambda: seleccionar_archivo(menu, nombre_archivo2))
boton_archivo2.grid(row=2, column=1)

nombre_archivo1 = tk.Label(menu, text="", bg=color_fondo_marco)
nombre_archivo1.grid(row=1, column=2)
nombre_archivo2 = tk.Label(menu, text="", bg=color_fondo_marco)
nombre_archivo2.grid(row=2, column=2)

########## ▲ MENÚ ▲ ##########


########## ▼ CÓDIGO ▼ ##########

cuadro = tk.Frame(raiz)
cuadro.config(bg="#b0b0b0", highlightbackground=color_linea_marco, highlightthickness=2)
cuadro.pack(padx=10, pady=(5, 10), side=LEFT)

numeros = tk.Frame(cuadro)
numeros.config(width=30, height=altura_marco, bg=color_fondo_marco, highlightbackground=color_linea_marco, highlightthickness=2)
numeros.pack(padx=(5, 2.5), pady=(5, 5), side=LEFT)

codigo = tk.Frame(cuadro)
codigo.config(width=anchura_marco, height=altura_marco, bg=color_fondo_marco, highlightbackground=color_linea_marco, highlightthickness=2)
codigo.pack(padx=(2.5, 5), pady=(5, 5), side=RIGHT)

#numeros = tk.Label(codigo, text)

########## ▲ CÓDIGO ▲ ##########


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
