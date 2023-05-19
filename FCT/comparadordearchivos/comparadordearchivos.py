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

# Al hacer click en el botón pertinente, pide seleccionar archivo y escribe su nombre y contenido el la interfaz del programa 
def seleccionar_archivo(archA, archB, ruta, ambival_arch):
    ruta_archivo = askopenfilename()
    if ruta_archivo != "":
        ruta.grid()
        ruta.configure(text=ruta_archivo)
        archA.grid()
        nombre_archA = str(os.path.basename(ruta_archivo))
        archA.configure(text=nombre_archA, font=mifuente2)
        archB.configure(font=(mifuente, tamano_fuente))
        escribir_contenido(ruta_archivo, ambival_arch)

# Selecciona línea a línea el contenido de un archivo y las escribe en la interfaz del programa
def escribir_contenido(ruta_archivo, ambival_arch):
    texto.delete('1.0', END)    # Limpia el área de texto
    if ambival_arch == "doc1":
        lista_lineas1.clear()
    if ambival_arch == "doc2":
        lista_lineas2.clear()
##    lista_lineas = []
    archivo = open(ruta_archivo, "r")
    lineas = archivo.readlines()
    for i, linea in enumerate(lineas):
        if ambival_arch == "doc1":
            lista_lineas1.append(linea.strip())
        if ambival_arch == "doc2":
            lista_lineas2.append(linea.strip())
        
        texto.insert(END, linea)
##        texto.configure(state="disabled")
##        lista_lineas.append(texto)
##        lista_lineas[i].grid(sticky="w", row=i, column=0)   #?
                
##    print(lista_lineas1)
##    print(lista_lineas2)
    
def cambiar_contenido(archA, archB, ruta):
    archA.configure(font=mifuente2)
    archB.configure(font=(mifuente, tamano_fuente))
    escribir_contenido(ruta, "")

# No se usa
def comparar0(lineasA, lineasB):
    lista_lineas = []
    for i, lineaA in enumerate(lineasA):
        mismalinea = False
        for lineaB in lineasB:
            if lineaA == lineaB:
                mismalinea = True
        if mismalinea == True:
            lista_lineas.append(tk.Label(codigo, text=lineaA, bg=color_fondo_widgets, font=(mifuente, tamano_fuente), anchor="nw"))
            lista_lineas[i].grid(sticky="w", row=i, column=0)
        else:
            lista_lineas.append(tk.Label(codigo, text=lineaA, bg='#98FB98', font=(mifuente, tamano_fuente), anchor="nw"))
            lista_lineas[i].grid(sticky="w", row=i, column=0)

def comparar(lineasA, lineasB):
    texto.delete('1.0', END)    # Limpia el área de texto
    for i, lineaA in enumerate(lineasA):
        mismalinea = False
        for lineaB in lineasB:
            if lineaA == lineaB:
                mismalinea = True
        if mismalinea == True:
            texto.insert(END, lineaA + "\n", 'mismalinea')
        else:
            texto.insert(END, lineaA + "\n", 'nuevalinea')
    
########## ▲ DECLARACIÓN DE FUNCIONES ▲ ##########

########## ▼ DIMENSIONES DE LA VENTANA ▼ ##########

ctypes.windll.shcore.SetProcessDpiAwareness(2)
user32 = ctypes.windll.user32
resolucion = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
anchura_ventana = (user32.GetSystemMetrics(0))
altura_ventana = (user32.GetSystemMetrics(1))

########## ▲ DIMENSIONES DE LA VENTANA ▲ ##########

color_fondo = '#4C4A48' # '#DDDDDD'
color_borde = '#000000' # '#7B7B7B'
color_texto = 'black'
color_fondo_widgets = 'white'
grosor_borde = 3
margen1 = 10
margen2 = 5
mifuente = 'Verdana 11'
mifuente2 = 'Verdana 11 bold'
tamano_fuente = 11

lista_lineas1 = []
lista_lineas2 = []

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

########## ▼ DOC 1 ▼ ##########

boton_doc1 = tk.Button(menu, image=icono_directorio, bg=color_fondo_widgets, borderwidth=0, command=lambda:seleccionar_archivo(doc1, doc2, ruta_doc1, "doc1"))
boton_doc1.grid(sticky="w", row=0, column=0)
boton_doc1.bind('<Enter>', raton_dentro)
boton_doc1.bind('<Leave>', raton_fuera)

ruta_doc1 = tk.Label(menu, text="", font=(mifuente, tamano_fuente), bg=color_fondo_widgets)
ruta_doc1.grid(sticky="w", row=1, column=1)
ruta_doc1.grid_remove()

doc1 = tk.Button(menu, text="", font=(mifuente, tamano_fuente), borderwidth=0, bg=color_fondo_widgets, command=lambda:cambiar_contenido(doc1, doc2, ruta_doc1.cget("text")))
doc1.grid(sticky="w", row=0, column=1)
doc1.grid_remove()

########## ▲ DOC 1 ▲ ##########

separador = tk.Label(menu, text="-", font=(mifuente, tamano_fuente), bg=color_fondo_widgets)
separador.grid(sticky="w", row=0, column=2, padx=(0, 3))

########## ▼ DOC 2 ▼ ##########

boton_doc2 = tk.Button(menu, image=icono_directorio, bg=color_fondo_widgets, borderwidth=0, command=lambda:seleccionar_archivo(doc2, doc1, ruta_doc2, "doc2"))
boton_doc2.grid(sticky="w", row=0, column=3)
boton_doc2.bind('<Enter>', raton_dentro)
boton_doc2.bind('<Leave>', raton_fuera)

doc2 = tk.Button(menu, text="", font=(mifuente, tamano_fuente), borderwidth=0, bg=color_fondo_widgets, command=lambda:cambiar_contenido(doc2, doc1, ruta_doc2.cget("text")))
doc2.grid(sticky="w", row=0, column=4)
doc2.grid_remove()

ruta_doc2 = tk.Label(menu, text="", font=(mifuente, tamano_fuente), bg=color_fondo_widgets)
ruta_doc2.grid(sticky="w", row=1, column=4)
ruta_doc2.grid_remove()

########## ▲ DOC 2 ▲ ##########

boton_comparar = tk.Button(menu, image=icono_comparar, bg=color_fondo_widgets, borderwidth=0, command=lambda:comparar(lista_lineas1, lista_lineas2))
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
codigo.pack(padx=0, pady=0, side=RIGHT)
codigo.pack_propagate(False)

texto = tk.Text(codigo, height=40, highlightcolor='red', padx=5, pady=5, bg=color_fondo_widgets, borderwidth=0, font=(mifuente, tamano_fuente))
barra_desplz = tk.Scrollbar(texto, orient='vertical', command=texto.yview)
texto.config(yscrollcommand=barra_desplz.set)
barra_desplz.pack(side=RIGHT, fill='y')
texto.pack(expand=True, fill=BOTH)

texto.tag_config('mismalinea', background=color_fondo_widgets, foreground='black')
texto.tag_config('nuevalinea', background='#98FB98', foreground='black')
texto.tag_config('lineaeliminada', background='#ff0000', foreground='black')

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
