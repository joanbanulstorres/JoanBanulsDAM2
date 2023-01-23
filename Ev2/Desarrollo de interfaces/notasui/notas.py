import tkinter as tk                                    # Importa la librería GUI
from tkinter import ttk                                 # Importa el módulo TTK

########## CREACIÓN DE LA VENTANA PRINCIPAL Y ESTILO DE LA VENTANA ##########

raiz = tk.Tk()                                          # Crea una interfaz gráfica de usuario
raiz.title("Notas v0.01")                               # Título de la ventana
raiz.geometry('400x400+50+50')                          # Geometría de la ventana y margen de la pantalla
raiz.attributes("-topmost", True)                       # Siempre encima del resto de las ventanas
raiz.attributes("-alpha", 0.9)                          # Transparencia de la ventana
raiz.resizable(0,0)                                     # Impide que el usuario pueda redimensionar la ventana
raiz.iconbitmap("./icono.ico")                          # Icono de la aplicación
raiz.option_add('*Font', 'Arial 16')
estilo = ttk.Style()                                    # Añade soporte para estilos
estilo.theme_use('default')                             # Selecciona el estilo por defecto de aplicaciones

# AÑADIMOS WIDGETS A LA VENTANA

version = tk.Label(raiz,text="Notas v0.01")             # Crea un label
version.pack()                                          # Lo añade a la ventana

inputusuario = ttk.Entry(raiz)                          # Crea una entrada para el nombre de usuario 
inputusuario.insert(0,'Introduce tu usuario')           # Instrucción para el usuario
inputusuario.pack(pady=10, ipadx=8)                     # Empaqueta la entrada 

inputcontrasena = ttk.Entry(raiz)                       # Crea una entrada para la contraseña
inputcontrasena.insert(0,'Introduce tu contrasena')     # Instrucción para el usuario
inputcontrasena.pack(pady=10, ipadx=8)                  # Empaqueta la entrada 

inputemail = ttk.Entry(raiz)                            # Crea una entrada para el email 
inputemail.insert(0,'Introduce tu email')               # Instrucción para el usuario
inputemail.pack(pady=10, ipadx=8)                       # Empaqueta la entrada 

botonlogin = ttk.Button(raiz, text="Enviar")            # Botón de iniciar sesión
botonlogin.pack(pady=10)                                # Empaqueta la entrada

# INTENTO INTRODUCIR ANTIALIAS EN WINDOWS Y LANZO EL BUCLE

try:                                                    # Intenta ejecutar
    from ctypes import windll                           # Importa la librería específica de GUI de Windows
    windll.shcore.SetProcessDpiAwareness(1)             # Activa el antialias para textos y demás cosas dentro de las interfaces
except Exception as e:                                  # Atrapa la excepción en caso de que se produzca
    print(e)                                            # Saca la excepción por pantalla
finally:                                                # En cualquier caso...
    raiz.mainloop()                                     # Detiene la ejecución y previene que la ventana se cierre
