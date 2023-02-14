import tkinter as tk                            # Importación de la librería 'tkinter'
from tkinter import *                           # Para poder usar iconos en los botones
from tkinter import ttk                         # Importación del módulo 'ttk'
from datetime import date                       # Importación de la clase 'date' del módulo 'datetime'
from datetime import datetime                   # Importación de la clase 'datetime' del módulo 'datetime'
import time                                     # Importación de la librería 'time'
from tkinter.colorchooser import askcolor       # Importación de la función 'askcolor' del módulo 'colorchooser'
import math                                     # Importación de la librería matemática
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
    global color_fondo
    color_fondo = "#ffffff"
    global color_texto
    color_texto = "#000000"
    raiz.configure(bg=color_fondo)
    fecha.configure(bg=color_fondo)
    hora.configure(bg=color_fondo)
    fecha.configure(fg=color_texto)
    hora.configure(fg="#ff6600")
    texto_actividad.configure(bg=color_fondo)
    tiempo_actividad.configure(bg=color_fondo)
    tiempo_actividad.configure(fg=color_texto)
    
def modo_oscuro():                              # Función que configura el estilo visual de la ventana en modo oscuro
    global color_fondo
    color_fondo = "#2d2d30"
    global color_texto
    color_texto = "#e5e5e5"
    raiz.configure(bg=color_fondo)
    fecha.configure(bg=color_fondo)
    fecha.configure(fg=color_texto)
    hora.configure(bg=color_fondo)
    hora.configure(fg="#ff9d5c")
    texto_actividad.configure(bg=color_fondo)
    tiempo_actividad.configure(bg=color_fondo)
    tiempo_actividad.configure(fg=colortexto)
    
def contador_tiempo(t):                         # Función que captura el tiempo total introducido y lo aplica como límite a un contador que crea 
    global contador
    global posy_txt_act
    global posy_prog
    global posx_tiempo_act
    global posy_tiempo_act
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
            
    global tiempo_actividad
    tiempo_actividad = tk.Label(raiz, text=tiempo, font=(mifuente, 11), bg=color_fondo, fg=color_texto) 
    tiempo_actividad.place(x=posx_tiempo_act, y=posy_tiempo_act)

    global nuevoprogreso
    nuevoprogreso = round((contador*30)/t)                                                  # 30 es la anchura de la barra de progreso
    actividad_progreso.configure(width=nuevoprogreso)

    def temporizador():
        global contador
        contador += 1

    if contador < t:
        tiempo_actividad.after(1000, lambda: [temporizador(), contador_tiempo(t)])          # Aumenta el contador y se muestra en la ventana el tiempo transcurrido
        
    else:
        tiempo_actividad.configure(text="Completado", font=(mifuente, 12))
        contador = 0
        posy_tiempo_act += 60
        posy_txt_act += 60
        posy_prog += 60
    
def enviar_tiempo(h, m, s):                                                                 # Función que captura y envía el tiempo introducido por el usuario
    horas = h.get()
    minutos = m.get()
    segundos = s.get()
    tiempo_total = int(horas)*3600 + int(minutos)*60 + int(segundos)
    #print("El tiempo definido es " + horas + "h: " + minutos + "min: " + segundos + "s")
    #print("El tiempo total en segundos es: " + str(tiempo_total) + " segundos")
    contador_tiempo(tiempo_total)

def enviar(nombre):                             # Función que crea una actividad a partir del nombre, pidiendo al usuario que eliga una duración y un color para la misma

    ########## ▼ BARRA DE PROGRESO ▼ ##########
    global posx_txt_act
    global posy_txt_act
    global posx_prog
    global posy_prog
    nombre_actividad = nombre.get()             # Captura el texto introducido por el usuario

    color_actividad = askcolor(title = "Selecciona un color para la actividad - " + nombre_actividad) 

    global texto_actividad
    texto_actividad = tk.Label(raiz, text=nombre_actividad, font=('Arial', 14), width=0, bg=color_fondo, fg=color_actividad[1], pady=-1)
    texto_actividad.place(x=posx_txt_act, y=posy_txt_act)

    actividad_fondo = tk.Label(raiz, font=(mifuente, 14), bg="#e8e8e8", width=30, pady=-1)                                                   # Fondo de la barra de progreso
    actividad_fondo.place(x=posx_prog, y=posy_prog)

    global actividad_progreso
    actividad_progreso = tk.Label(raiz, font=(mifuente, 14), width=0, bg=color_actividad[1], fg="#000000", pady=-1)                          # Barra de progreso de la actividad
    actividad_progreso.place(x=posx_prog, y=posy_prog)

    ########## ▲ BARRA DE PROGRESO ▲ ##########
    
    ########## ▼ TIEMPO ▼ ##########

    ventana_seleccion_tiempo = tk.Toplevel()
    ventana_seleccion_tiempo.geometry('300x200+650+100')
    ventana_seleccion_tiempo.configure(bg=color_fondo)
    ventana_seleccion_tiempo.attributes("-topmost", True)
    ventana_seleccion_tiempo.resizable(0, 0)             

    selecciona_tiempo = tk.Label(ventana_seleccion_tiempo, text="Selecciona una duración", font=(mifuente, 14), bg=color_fondo, fg=color_texto)
    selecciona_tiempo.place(x=10, y=10)

    # Horas
    horas = tk.Entry(ventana_seleccion_tiempo, font=(mifuente, 12))
    horas.place(x=10, y=50)
    texto_horas = tk.Label(ventana_seleccion_tiempo, text="h", font=(mifuente, 10), bg=color_fondo, fg=color_texto)
    texto_horas.place(x=200, y=50)

    # Minutos
    minutos = tk.Entry(ventana_seleccion_tiempo, font=(mifuente, 12))
    minutos.place(x=10, y=80)
    texto_minutos = tk.Label(ventana_seleccion_tiempo, text="min", font=(mifuente, 10), bg=color_fondo, fg=color_texto)
    texto_minutos.place(x=200, y=80)

    # Segundos
    segundos = tk.Entry(ventana_seleccion_tiempo, font=(mifuente, 12))
    segundos.place(x=10, y=110)
    texto_segundos = tk.Label(ventana_seleccion_tiempo, text="s", font=(mifuente, 10), bg=color_fondo, fg=color_texto)
    texto_segundos.place(x=200, y=110)

    boton_enviar_tiempo = tk.Button(ventana_seleccion_tiempo, text="Aceptar", font=(mifuente, 12), command= lambda: [enviar_tiempo(horas, minutos, segundos), ventana_seleccion_tiempo.destroy()])
    boton_enviar_tiempo.place(x=10, y=140)

    '''
    if destruir==True:
       ventana_seleccion_tiempo.destroy() 
    '''   
    
    ########## ▲ TIEMPO ▲ ##########
    
def nueva_actividad():
    global contador
    if contador == 0:
        entrada = tk.Entry(raiz, font=('Arial', 12))
        entrada.place(x=172, y=95)
        boton_enviar = tk.Button(raiz, text="Aceptar", font=(mifuente, 12), command= lambda: [enviar(entrada), entrada.destroy(), boton_enviar.destroy()])
        boton_enviar.place(x=374, y=90)
    else:
        print("Aún no se ha completado la actividad actual")
        ventana_mensaje = tk.Toplevel()
        ventana_mensaje.geometry('400x40+650+100')
        ventana_mensaje.configure(bg=color_fondo)
        ventana_mensaje.attributes("-topmost", True)
        ventana_mensaje.resizable(0, 0) 
        mensaje = tk.Label(ventana_mensaje, text="Aún no se ha completado la actividad actual", font=(mifuente, 14), bg=color_fondo, fg="#ff0000")
        mensaje.pack()
        
########### ▲ DECLARACIÓN DE FUNCIONES ▲ ##########


########## ▼ DECLARACIÓN DE VARIABLES GLOBALES ▼ ##########
    
contador = 0
color_fondo = "#ffffff"
color_texto = "#000000"
mifuente = "Arial"
## Posiciones
# Nombre de la actividad
posx_txt_act = 20
posy_txt_act = 140
# Barra de brogreso
posx_prog = 20
posy_prog = 165
# Tiempo
posx_tiempo_act = 370
posy_tiempo_act = 165

########## ▲ DECLARACIÓN DE VARIABLES GLOBALES ▲ ##########


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


########### ▼ WIDGETS ▼ ##########

"""
marco = tk.Frame(raiz)                          # Widget principal que va a contener el resto de widgets
marco.configure(bg = '#ffffff')
marco.pack()
"""

# FECHA
hoy = date.today()
fecha_actual = hoy.strftime("%d/%m/%Y")
fecha = tk.Label(raiz, text=fecha_actual, font=(mifuente, 18), bg='#ffffff', fg="#000000", pady=-1, borderwidth=0, relief="solid")
fecha.place(x=20, y=10)

# HORA
hora = tk.Label(raiz, font=(mifuente, 18), bg='#ffffff', fg="#ff6600", pady=-1, borderwidth=0, relief="solid")
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
boton_nueva_actividad = tk.Button(raiz, text="Nueva actividad +", font=(mifuente, 12), command=nueva_actividad)
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
