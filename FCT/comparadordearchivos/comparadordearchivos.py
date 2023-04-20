import ctypes
import os
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import *

########## ▼ DECLARACIÓN DE FUNCIONES ▼ ##########

def raton_dentro(e):
    e.widget['background'] = '#f2f2f2'

def raton_fuera(e):
    e.widget['background'] = '#ffffff'

def seleccionar_archivo(nombre_archivo_texto):
    ruta = askopenfilename()
    nombre_archivo = str(os.path.basename(ruta))
    nombre_archivo_texto.configure(text=nombre_archivo)
    #archivo = open(ruta, 'r')
    seleccionar_contenido(ruta)

def comparar():
    print("Comparar")

def seleccionar_contenido(archivo):
    print(archivo)
    archivo = open(archivo, "r")
    lineas = archivo.readlines()
    contador = 0
    for linea in lineas:
        lineas1.append(tk.Label(codigo, text=linea, bg="#0000ff", font=(mifuente, 9), anchor="nw"))
        print(lineas1[contador]['text'])
        lineas1[contador].grid(sticky="w", row=0, column=0)     
    

########## ▲ DECLARACIÓN DE FUNCIONES ▲ ##########

########## ▼ DIMENSIONES DE LA VENTANA ▼ ##########

ctypes.windll.shcore.SetProcessDpiAwareness(2)
user32 = ctypes.windll.user32
resolucion = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
anchura_ventana = (user32.GetSystemMetrics(0))
altura_ventana = (user32.GetSystemMetrics(1))

########## ▲ DIMENSIONES DE LA VENTANA ▲ ##########

color_fondo = '#DDDDDD'
color_borde = '#7B7B7B'
color_texto = 'black'
color_fondo_widgets = "white"
grosor_borde = 2
margen1 = 10
margen2 = 5
mifuente = 'Verdana'
lineas1 = []
lineas2 = []

########## ▼ INTERFAZ DE USUARIO ▼ ##########

########## ▼ VENTANA PRINCIPAL ▼ ##########

raiz = tk.Tk()
raiz.title("Comparador de archivos")
raiz.state('zoomed')                                                                                                    # Pantalla completa
raiz.geometry('%dx%d' % resolucion)
raiz.resizable(True, True)
raiz.minsize(int(anchura_ventana/1.5), int(altura_ventana/1.5))

ventana = tk.Frame(raiz)
ventana.config(width=anchura_ventana, height=anchura_ventana, bg=color_fondo)
ventana.pack()

########## ▲ VENTANA PRINCIPAL ▲ ##########

########## ▼ MENÚ ▼ ##########

menu = tk.Frame(ventana)
menu.config(width=anchura_ventana, height=80, bg=color_fondo_widgets, highlightbackground=color_borde, highlightthickness=grosor_borde)
menu.pack(padx=margen1, pady=(margen1, margen2), anchor="w")

icono_directorio = tk.PhotoImage(file='directorio.png')
icono_comparar = tk.PhotoImage(file='comparar.png')

boton_doc1 = tk.Button(menu, image=icono_directorio, bg=color_fondo_widgets, borderwidth=0, command=lambda:seleccionar_archivo(doc1))
boton_doc1.grid(sticky="w", row=0, column=0)
boton_doc1.bind('<Enter>', raton_dentro)
boton_doc1.bind('<Leave>', raton_fuera)

doc1 = tk.Label(menu, text="", bg=color_fondo_widgets, font=(mifuente, 9))
doc1.grid(sticky="w", row=0, column=1)

separador = tk.Label(menu, text="-", bg=color_fondo_widgets, font=(mifuente, 9))
separador.grid(sticky="w", row=0, column=2, padx=(0, 3))

boton_doc2 = tk.Button(menu, image=icono_directorio, bg=color_fondo_widgets, borderwidth=0, command=lambda:seleccionar_archivo(doc2))
boton_doc2.grid(sticky="w", row=0, column=3)
boton_doc2.bind('<Enter>', raton_dentro)
boton_doc2.bind('<Leave>', raton_fuera)

doc2 = tk.Label(menu, text="", bg=color_fondo_widgets, font=(mifuente, 9))
doc2.grid(sticky="w", row=0, column=4)

boton_comparar = tk.Button(menu, image=icono_comparar, bg=color_fondo_widgets, borderwidth=0, command=lambda:comparar())
boton_comparar.grid(sticky="w", row=0, column=5, padx=(3,0))
boton_comparar.bind('<Enter>', raton_dentro)
boton_comparar.bind('<Leave>', raton_fuera)

########## ▲ MENÚ ▲ ##########

########## ▼ CAJA DEL CÓDIGO ▼ ##########

cuadro = tk.Frame(ventana)
cuadro.config(bg=color_fondo)
cuadro.pack(padx=margen1, pady=(margen2, margen1), side=LEFT)

numeros = tk.Frame(cuadro)
numeros.config(width=30, height=altura_ventana, bg=color_fondo_widgets, highlightbackground=color_borde, highlightthickness=grosor_borde)
numeros.pack(padx=(0, 5), pady=0, side=LEFT)

codigo = tk.Frame(cuadro)
codigo.config(width=anchura_ventana, height=altura_ventana, bg=color_fondo_widgets, highlightbackground=color_borde, highlightthickness=grosor_borde)
codigo.pack(padx=(5, 0), pady=0, side=RIGHT)
codigo.grid_propagate(False)

##ejemplo = tk.Label(codigo, text="ejemplo", bg=color_fondo_widgets, font=(mifuente, 9), anchor="nw")
##ejemplo.grid(sticky="w", row=0, column=0)

#numeros = tk.Label(codigo, text)

########## ▲ CAJA DEL CÓDIGO ▲ ##########

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
