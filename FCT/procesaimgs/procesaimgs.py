import ctypes
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def raton_dentro(e):
    e.widget['background'] = '#f2f2f2'

def raton_fuera(e):
    e.widget['background'] = '#ffffff'

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
                    print(elemento.name)
            if imagen == True:
                ruta_origen.configure(bg=color_fondo)
                error_directorio_origen.configure(text="")
            else:
                ruta_origen.configure(bg=color_error)
                error_directorio_origen.configure(text="*No contine imágenes con los formatos soportados")
        ruta_origen.configure(text=directorio)

def seleccionar_directorio_destino():
    directorio = filedialog.askdirectory()
    ruta_destino.configure(text=directorio)

def generar_imgs():
    print("Generando imagenes...")
                    
ctypes.windll.shcore.SetProcessDpiAwareness(2)
user32 = ctypes.windll.user32
anchura = user32.GetSystemMetrics(0)*0.6
altura = user32.GetSystemMetrics(1)*0.19

color_fondo = '#ffffff'
color_texto = '#000000'
color_error = '#ff4848'
mifuente = 'Verdana'


########## ▼ INTERFAZ DE USUARIO ▼ ##########

########## ▼ VENTANA PRINCIPAL ▼ ##########

raiz = tk.Tk()
raiz.title("Procesador de imágenes")
raiz.geometry('%dx%d' % (anchura, altura))
raiz.configure(bg=color_fondo)
estilo = ttk.Style()

########## ▲ VENTANA PRINCIPAL ▲ ##########

icono_directorio = tk.PhotoImage(file='directorio.png')

########## ▼ DIRECTORIO ORIGEN ▼ ##########

texto_directorio_origen = tk.Label(raiz, text="Directorio origen:", font=(mifuente,11), bg=color_fondo, fg=color_texto)
texto_directorio_origen.grid(sticky="w", row=0, column=0, padx=(15,0), pady=10)

btn_directorio_origen = tk.Button(raiz, image=icono_directorio, bg=color_fondo, borderwidth=0, command=lambda:seleccionar_directorio_origen())
btn_directorio_origen.grid(sticky="w", row=0, column=1, padx=(10,5), pady=10)
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
btn_directorio_destino.grid(sticky="w", row=1, column=1, padx=(10,5), pady=10)
btn_directorio_destino.bind('<Enter>', raton_dentro)
btn_directorio_destino.bind('<Leave>', raton_fuera)

ruta_destino = tk.Label(raiz, text="", font=(mifuente,11), bg=color_fondo, fg=color_texto)
ruta_destino.grid(sticky="w", row=1, column=2, padx=5, pady=10)

error_directorio_destino = tk.Label(raiz, text="", font=(mifuente,9), bg=color_fondo, fg=color_error)
error_directorio_destino.grid(sticky="w", row=1, column=3, padx=5, pady=10)

########## ▲ DIRECTORIO ORIGEN ▲ ##########

formatos = tk.Label(raiz, text="Formatos soportados: jpg", font=(mifuente,9), bg=color_fondo, fg=color_texto)
formatos.grid(sticky="w", row=2, column=0, columnspan=4, padx=(15,0), pady=(5,10))

estilo.configure('personalizado.TButton', font=(mifuente, 10))
btn_generar_imgs = ttk.Button(raiz, text="Generar imágenes", style='personalizado.TButton', command=lambda:generar_imgs())
btn_generar_imgs.grid(sticky="w", row=3, column=0, columnspan=4, padx=(15,0), pady=(5,10))

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
