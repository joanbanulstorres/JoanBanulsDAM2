import tkinter as tk                                                                # Importa la librería GUI
from tkinter import ttk                                                             # Importa el módulo TTK
import sqlite3 as bd                                                                # *NUEVO* - Importo la librería de SQLite
from tkinter.colorchooser import askcolor                                           # *NUEVO* - Para poder usar la fnc 'askcolor'

# *NUEVO* - CONEXIÓN A LA BASE DE DATOS

conexion = bd.connect("notas.sqlite")                                               # *NUEVO* - Indico el nombre de la base de datos
cursor = conexion.cursor()                                                          # *NUEVO* - Creo un cursor                  
# *NUEVO* - Sobre el cursor, ejecuto una petición para crear unas tablas que no existan anteriormente en la base de datos
cursor.execute("""                                              
    CREATE TABLE IF NOT EXISTS 'notas'(
        'id' INTEGER,
        'texto' TEXT,
        'color' TEXT,
        'fecha' TEXT,
        PRIMARY KEY('id' AUTOINCREMENT)
    );
""")

cursor.execute("""                                              
    CREATE TABLE IF NOT EXISTS 'usuarios'(
        'id' INTEGER,
        'usuario' TEXT,
        'contrasena' TEXT,
        'email' TEXT,
        PRIMARY KEY('id' AUTOINCREMENT)
    );
""")

# *NUEVO* - DECLARACIÓN DE FUNCIONES

def iniciaSesion():                                                                     # *NUEVO* - Función de inicio de sesión
    print("Vamos a iniciar sesión")                                                     # *NUEVO* - Imprime un mensaje en pantalla
    print("El nombre de usuario es: " + varusuario.get())                               # *NUEVO*
    print("La contraseña es: " + varcontrasena.get())                                   # *NUEVO*
    print("El email es: " + varemail.get())                                             # *NUEVO*
    # Se va a comprobar si existe in usuario en la BD
    cursor = conexion.cursor()                                                          # *NUEVO* - Crea un cursor
    cursor.execute('SELECT * FROM usuarios')                                            # *NUEVO* - Ejecuta una petición de seleccionar usuarios
    datos = cursor.fetchall()                                                           # *NUEVO* - Carga los datos
    numerousuarios = 0                                                                  # *NUEVO* - Crea una variable contador
    for i in datos:                                                                     # *NUEVO* - Por cada uno de los registros devueltos
        numerousuarios = numerousuarios + 1                                             # *NUEVO* - Se le suma un valor al contador
    if(numerousuarios == 0):                                                            # *NUEVO* - Si no hay usuarios
        print("Actualmente no hay ningún usuario en la base de datos")
        cursor.execute('''
                        INSERT
                        INTO usuarios
                        VALUES(
                        NULL,
                        "'''+varusuario.get()+'''",
                        "'''+varcontrasena.get()+'''",
                        "'''+varemail.get()+'''")
                        ''')                                                            # *NUEVO* - Inserto el usuario en la BD
        conexion.commit()                                                               # *NUEVO* - Ejecuta la inserción
    else:                                                                               # *NUEVO* - En caso de haberlos
        print("Sí que existe un usuario en la base de datos")
        cursor.execute('''
                        SELECT *
                        FROM usuarios
                        WHERE usuario = "'''+varusuario.get()+'''"
                        AND contrasena = "'''+varcontrasena.get()+'''"
                        AND email = "'''+varemail.get()+'''"
                        ''')                                                            # *NUEVO* - Realiza una consulta a la BD
        existe = False
        #existe = True                                                                  # *NUEVO* - Fuerza para no tener que validar
        datos = cursor.fetchall()                                                       # *NUEVO* - Carga lo datos
        for i in datos:                                                                 # *NUEVO* - Para cada uno de los registros devueltos
            existe = True                                                               # *NUEVO* - Actualiza el valor
        if existe == True:                                                              # *NUEVO* - En caso de que exista
            print("El usuario es correcto")
            marco.destroy()                                                             # *NUEVO* - Elimina la ventana anterior
            marco2 = ttk.Frame(raiz)                                                    # *NUEVO* - Crea un nuevo marco
            marco2.pack()                                                               # *NUEVO* - Empaqueta el marco

            iconoaplicacion = tk.PhotoImage(file="./icono.png")                         # *NUEVO* - Carga una imagen
            etiquetaicono = ttk.Label(
                marco2,
                text="Notas v0.01",
                image= iconoaplicacion,
                compound = tk.TOP,
                font = ("Arial", 14)
                )                                                                       # *NUEVO* - Muestra la imagen en el label
            etiquetaicono.image = iconoaplicacion
            etiquetaicono.pack()                                                        # *NUEVO* - Empaqueta la etiqueta 

            botonnuevanota = ttk.Button(marco2, text="Nueva Nota", command=creaNota)    # *NUEVO* - Botón de iniciar sesión - *NUEVO*: 'command'
            botonnuevanota.pack(pady=10)                                                # *NUEVO* - Empaqueta la entrada
        else:                                                                           # *NUEVO* - En caso de que no exista
            print("El usuario no es correcto ")
            raiz.after(3000, lambda:raiz.destroy())                                     # *NUEVO* - Cierra la ventana después de 3 segundos

def creaNota():                                                                         # *NUEVO*
    ventananuevanota = tk.Toplevel()                                                    # *NUEVO* - Toplevel -> se cierran al cerrar la ventana principal
    anchura = 350
    altura = 350
    ventananuevanota.geometry(str(anchura) + 'x' + str(altura) + '+100+100')
    texto = tk.Text(ventananuevanota, bg="white")
    texto.pack()
    selectorcolor = ttk.Button(ventananuevanota, text="Cambiar color", command=lambda:cambiaColor(ventananuevanota))
    selectorcolor.pack()

def cambiaColor(ventana):                                                               # *NUEVO*
    nuevocolor = askcolor(title="Selecciona un color")                                  # *NUEVO* - Muestra un selector de color
    ventana.configure(bg = nuevocolor[1])                                               # *NUEVO* - Cambia el color de fondo a la vantana seleccionada
    
# CREACIÓN DE LA VENTANA PRINCIPAL Y ESTILO DE LA VENTANA

raiz = tk.Tk()                                                                          # Crea una interfaz gráfica de usuario
raiz.title("Notas v0.01")                                                               # Título de la ventana
raiz.geometry('400x400+50+50')                                                          # Geometría de la ventana y margen de la pantalla
raiz.attributes("-topmost", True)                                                       # Siempre encima del resto de las ventanas
raiz.attributes("-alpha", 0.9)                                                          # Transparencia de la ventana
raiz.resizable(0,0)                                                                     # Impide que el usuario pueda redimensionar la ventana
raiz.iconbitmap("./icono.ico")                                                          # Icono de la aplicación
raiz.option_add('*Font', 'Arial 16')
estilo = ttk.Style()                                                                    # Añade soporte para estilos
estilo.theme_use('default')                                                             # Selecciona el estilo por defecto de aplicaciones

# *NUEVO* - DECLARACIÓN DE VARIABLES GLOBALES

varusuario = tk.StringVar()                                                             # *NUEVO* - Variable para almacenar el usuario
varcontrasena = tk.StringVar()                                                          # *NUEVO* - Variable para almacenar la contraseña
varemail = tk.StringVar()                                                               # *NUEVO* - Variable para almacenar el email

# AÑADIMOS WIDGETS A LA VENTANA

marco = ttk.Frame(raiz)                                                                 # *NUEVO*
marco.pack()                                                                            # *NUEVO*

version = tk.Label(marco,text="Notas v0.01")                                            # Crea un label
version.pack()                                                                          # Lo añade a la ventana

inputusuario = ttk.Entry(marco, textvariable = varusuario)                              # Crea una entrada para el nombre de usuario - *NUEVO*: 'textvariable'
inputusuario.insert(0,'Introduce tu usuario')                                           # Instrucción para el usuario
inputusuario.pack(pady=10, ipadx=8)                                                     # Empaqueta la entrada 

inputcontrasena = ttk.Entry(marco, textvariable = varcontrasena)                        # Crea una entrada para la contraseña - *NUEVO*: 'textvariable'
inputcontrasena.insert(0,'Introduce tu contrasena')                                     # Instrucción para el usuario
inputcontrasena.pack(pady=10, ipadx=8)                                                  # Empaqueta la entrada 

inputemail = ttk.Entry(marco, textvariable = varemail)                                  # Crea una entrada para el email- *NUEVO*: 'textvariable'
inputemail.insert(0,'Introduce tu email')                                               # Instrucción para el usuario
inputemail.pack(pady=10, ipadx=8)                                                       # Empaqueta la entrada 

botonlogin = ttk.Button(marco, text="Enviar", command=iniciaSesion)                     # Botón de iniciar sesión - *NUEVO*: 'command'
botonlogin.pack(pady=10)                                                                # Empaqueta la entrada

# INTENTO INTRODUCIR ANTIALIAS EN WINDOWS Y LANZO EL BUCLE

try:                                                                                    # Intenta ejecutar
    from ctypes import windll                                                           # Importa la librería específica de GUI de Windows
    windll.shcore.SetProcessDpiAwareness(1)                                             # Activa el antialias para textos y demás cosas dentro de las interfaces
except Exception as e:                                                                  # Atrapa la excepción en caso de que se produzca
    print(e)                                                                            # Saca la excepción por pantalla
finally:                                                                                # En cualquier caso...
    raiz.mainloop()                                                                     # Detiene la ejecución y previene que la ventana se cierre
