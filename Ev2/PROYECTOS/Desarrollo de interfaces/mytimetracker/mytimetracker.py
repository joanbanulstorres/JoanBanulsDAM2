import tkinter as tk                            # Importación de la librería 'tkinter'
from tkinter import *                           # Para poder usar iconos en los botones
from tkinter import ttk                         # Importación del módulo 'ttk'
from datetime import date                       # Importación de la clase 'date' del módulo 'datetime'
from datetime import datetime                   # Importación de la clase 'datetime' del módulo 'datetime'
from tkinter.colorchooser import askcolor       # Importación de la función 'askcolor' del módulo 'colorchooser' 
'''
import PIL
from PIL import Image, ImageTk
print(PIL.__version__)
'''

########### ▼ DECLARACIÓN DE FUNCIONES ▼ ##########

def registrar_hora():                           # Función recursiva que registra la hora actual cada segundo
    ahora = datetime.now()
    hora_actual = ahora.strftime("%H:%M:%S")
    hora.config(text = hora_actual)
    hora.after(1000, registrar_hora)

def modo_claro():                               # Función que configura el estilo visual de la ventana en modo claro
    raiz.configure(bg="#ffffff")
    fecha.configure(bg="#ffffff")
    hora.configure(bg="#ffffff")
    fecha.configure(fg="#000000")
    hora.configure(fg="#ff6600")
    color_fondo = "#ffffff"                     # Para la ventana de selección de tiempo

def modo_oscuro():                              # Función que configura el estilo visual de la ventana en modo oscuro
    raiz.configure(bg="#2d2d30")
    fecha.configure(bg="#2d2d30")
    fecha.configure(fg="#e5e5e5")
    hora.configure(bg="#2d2d30")
    hora.configure(fg="#ff9d5c")
    color_fondo = "#2d2d30"
    
def contador_tiempo():
    global contador
    if contador < 60:
        segundos = contador
        tiempo = str(segundos) + " s"
    else:
        if contador < 3600:
            minutos = contador // 60
            segundos = contador % 60
            tiempo = str(minutos) + " min: " + str(segundos) + " s"
        else:
            horas = contador // 3600
            if (contador % 3600) < 60:
                minutos = 0
                segundos = contador % 3600
                tiempo = str(horas) + " h: " + str(minutos) + " min: " + str(segundos) + " s"
            else:
                minutos = (contador % 3600) // 60
                segundos = (contador % 3600) % 60
                tiempo = str(horas) + " h: " + str(minutos) + " min: " + str(segundos) + " s"
            
    tiempo_actividad = tk.Label(raiz, text=tiempo, font=('Arial', 11), bg=color_fondo, fg="#000000") 
    tiempo_actividad.place(x=370, y =140)
    contador += 1
    tiempo_actividad.after(1000, contador_tiempo)

def enviar_tiempo(h, m, s):                     # Función que captura el tiempo introducido por el usuario
    contador_tiempo()
    horas = h.get()
    minutos = m.get()
    segundos = s.get()
    tiempo_total = int(horas)*3600 + int(minutos)*60 + int(segundos)
    print("El tiempo definido es: " + horas + "h: " + minutos + "min: " + segundos + "s")
    print("El tiempo total en segundos es: " + str(tiempo_total) + " segundos")

    destruir = True

def enviar(nombre):                             # Función que crea una actividad a partir del nombre, pidiendo al usuario que eliga una duración y un color para la misma
    nombre_actividad = nombre.get()             # Captura el texto introducido por el usuario
    print(nombre_actividad)

    color_actividad = askcolor(title = "Selecciona un color para la actividad") 
    actividad = tk.Label(raiz, text=nombre_actividad, font=('Arial', 14), width=30, bg=color_actividad[1], fg="#000000", pady=-1)
    actividad.place(x=20, y=140)

    ########## ▼ TIEMPO ▼ ##########

    ventana_seleccion_tiempo = tk.Toplevel()
    ventana_seleccion_tiempo.geometry('300x200+650+100')
    ventana_seleccion_tiempo.configure(bg=color_fondo)
    ventana_seleccion_tiempo.attributes("-topmost", True)
    ventana_seleccion_tiempo.resizable(0, 0)             

    selecciona_tiempo = tk.Label(ventana_seleccion_tiempo, text="Selecciona una duración", font=('Arial', 14), bg=color_fondo, fg="#000000")
    selecciona_tiempo.place(x=10, y=10)

    # Horas
    horas = tk.Entry(ventana_seleccion_tiempo, font=('Arial', 12))
    horas.place(x=10, y=50)
    texto_horas = tk.Label(ventana_seleccion_tiempo, text="h", font=('Arial', 10), bg=color_fondo, fg="#000000")
    texto_horas.place(x=200, y=50)

    # Minutos
    minutos = tk.Entry(ventana_seleccion_tiempo, font=('Arial', 12))
    minutos.place(x=10, y=80)
    texto_minutos = tk.Label(ventana_seleccion_tiempo, text="min", font=('Arial', 10), bg=color_fondo, fg="#000000")
    texto_minutos.place(x=200, y=80)

    # Segundos
    segundos = tk.Entry(ventana_seleccion_tiempo, font=('Arial', 12))
    segundos.place(x=10, y=110)
    texto_segundos = tk.Label(ventana_seleccion_tiempo, text="s", font=('Arial', 10), bg=color_fondo, fg="#000000")
    texto_segundos.place(x=200, y=110)

    boton_enviar_tiempo = tk.Button(ventana_seleccion_tiempo, text="Aceptar", font=('Arial', 12), command= lambda: enviar_tiempo(horas, minutos, segundos))
    boton_enviar_tiempo.place(x=10, y=140)

    '''
    if destruir==True:
       ventana_seleccion_tiempo.destroy() 
    '''   
    
    ########## ▲ TIEMPO ▲ ##########
    
def nueva_actividad():
    entrada = tk.Entry(raiz, font=('Arial', 12))
    entrada.place(x=172, y=95)
    boton_enviar = tk.Button(raiz, text="Aceptar", font=('Arial', 12), command= lambda: enviar(entrada))
    boton_enviar.place(x=374, y=90)

    
########### ▲ DECLARACIÓN DE FUNCIONES ▲ ##########


########### ▼ VENTANA PRINCIPAL ▼ ##########

raiz = tk.Tk()                                  # Se crea la raíz o base de la interfaz gráfica
raiz.title("MyTimeTracker")
raiz.geometry('500x500+100+100')                # Dimensiones de la raíz
color_fondo = "#ffffff"
raiz.configure(bg=color_fondo)
raiz.attributes("-topmost", True)               # Siempre encima del resto de ventanas
#raiz.attributes("-alpha", 0.95)                # Transparencia
raiz.resizable(0, 0)                            # Impide redimensionar la ventana
#raiz.iconbitmap('')

########### ▲ VENTANA PRINCIPAL ▲ ##########

contador = 0

########### ▼ WIDGETS ▼ ##########

"""
marco = tk.Frame(raiz)                          # Widget principal que va a contener el resto de widgets
marco.configure(bg = '#ffffff')
marco.pack()
"""

# FECHA
hoy = date.today()
fecha_actual = hoy.strftime("%d/%m/%Y")
fecha = tk.Label(raiz, text=fecha_actual, font=('Arial', 18), bg='#ffffff', fg="#000000", pady=-1, borderwidth=0, relief="solid")
fecha.place(x=20, y=10)

# HORA
hora = tk.Label(raiz, font=('Arial', 18), bg='#ffffff', fg="#ff6600", pady=-1, borderwidth=0, relief="solid")
hora.place(x=20, y=41)
registrar_hora()

# BOTONES MODO CLARO Y MODO OSCURO
icono_sol = PhotoImage(file='sol.png')
boton_claro = tk.Button(raiz, image=icono_sol, command=modo_claro)
boton_claro.place(x=395, y=10)

icono_luna = PhotoImage(file='luna.png')
boton_oscuro = tk.Button(raiz, image=icono_luna, command=modo_oscuro)
boton_oscuro.place(x=440, y=10)

# BOTON AÑADIR ACTIVIDAD
icono_enviar = PhotoImage(file='enviar.png')
boton_nueva_actividad = tk.Button(raiz, text="Nueva actividad +", font=('Arial', 12), command=nueva_actividad)
boton_nueva_actividad.place(x=20, y=90)

########### ▲ WIDGETS ▲ ##########

# SE INTENTA INTRODUCIR ANTIALIAS EN WINDOWS Y SE LANZA EL BUCLE

try:                                            # Intenta ejecutar
    from ctypes import windll                   # Importa la librería específica de GUI de Windows
    windll.shcore.SetProcessDpiAwareness(1)     # Activa el antialias para textos y demás cosas dentro de las interfaces
except Exception as e:                          # Atrapa la excepción en caso de que se produzca
    print(e)                                    # Saca la excepción por pantalla
finally:                                        # En cualquier caso...
    raiz.mainloop()                             # Detiene la ejecución y previene que la ventana se cierre
