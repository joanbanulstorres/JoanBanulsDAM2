import tkinter as tk
from tkinter import ttk
import ctypes

color_fondo = '#ffffff'
color_texto = '#000000'

ctypes.windll.shcore.SetProcessDpiAwareness(2)

user32 = ctypes.windll.user32
resolucion = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(resolucion)


########## ▼ INTERFAZ DE USUARIO ▼ ##########

raiz = tk.Tk()
##anchura_ventana = raiz.winfo_screenwidth()
##altura_ventana = raiz.winfo_screenheight()

raiz.title("Comparador de archivos")
raiz.state('zoomed')
raiz.geometry('%dx%d' % resolucion)
raiz.configure(bg=color_fondo)

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


