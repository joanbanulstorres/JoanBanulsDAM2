import tkinter as tk                                                                # Importa la librería GUI
from tkinter import ttk                                                             # Importa el módulo TTK
import sqlite3 as bd                                                                # Importo la librería de SQLite
from tkinter.colorchooser import askcolor                                           # Para poder usar la fnc 'askcolor'
import time                                                                         # *NUEVO*

class Nota:                                                     # *NUEVO* - Declaramos una clase
    def __init__(self, texto, color, fecha):                    # Constructor
        self.texto = texto                                      # Propiedad texto
        self.color = color                                      # Propiedad color
        self.fecha = fecha                                      # Propiedad fecha

# CONEXIÓN A LA BASE DE DATOS

conexion = bd.connect("notas.sqlite")                                               # Indico el nombre de la base de datos
cursor = conexion.cursor()                                                          # Creo un cursor                  
# Sobre el cursor, ejecuto una petición para crear unas tablas que no existan anteriormente en la base de datos
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

# DECLARACIÓN DE FUNCIONES

def iniciaSesion():                                                                     # Función de inicio de sesión
    print("Vamos a iniciar sesión")                                                     # Imprime un mensaje en pantalla
    print("El nombre de usuario es: " + varusuario.get())                               
    print("La contraseña es: " + varcontrasena.get())                                   
    print("El email es: " + varemail.get())                                             
    # Se va a comprobar si existe in usuario en la BD
    cursor = conexion.cursor()                                                          # Crea un cursor
    cursor.execute('SELECT * FROM usuarios')                                            # Ejecuta una petición de seleccionar usuarios
    datos = cursor.fetchall()                                                           # Carga los datos
    numerousuarios = 0                                                                  # Crea una variable contador
    for i in datos:                                                                     # Por cada uno de los registros devueltos
        numerousuarios = numerousuarios + 1                                             # Se le suma un valor al contador
    if(numerousuarios == 0):                                                            # Si no hay usuarios
        print("Actualmente no hay ningún usuario en la base de datos")
        cursor.execute('''
                        INSERT
                        INTO usuarios
                        VALUES(
                        NULL,
                        "'''+varusuario.get()+'''",
                        "'''+varcontrasena.get()+'''",
                        "'''+varemail.get()+'''")
                        ''')                                                            # Inserto el usuario en la BD
        conexion.commit()                                                               # Ejecuta la inserción
    else:                                                                               # En caso de haberlos
        print("Sí que existe un usuario en la base de datos")
        cursor.execute('''
                        SELECT *
                        FROM usuarios
                        WHERE usuario = "'''+varusuario.get()+'''"
                        AND contrasena = "'''+varcontrasena.get()+'''"
                        AND email = "'''+varemail.get()+'''"
                        ''')                                                            # Realiza una consulta a la BD
        existe = False
        existe = True                                                                  # Fuerza para no tener que validar
        datos = cursor.fetchall()                                                       # Carga lo datos
        for i in datos:                                                                 # Para cada uno de los registros devueltos
            existe = True                                                               # Actualiza el valor
        if existe == True:                                                              # En caso de que exista
            print("El usuario es correcto")
            marco.destroy()                                                             # Elimina la ventana anterior
            marco2 = ttk.Frame(raiz)                                                    # Crea un nuevo marco
            marco2.pack()                                                               # Empaqueta el marco

            iconoaplicacion = tk.PhotoImage(file="./icono.png")                         # Carga una imagen
            etiquetaicono = ttk.Label(
                marco2,
                text="Notas v0.01",
                image= iconoaplicacion,
                compound = tk.TOP,
                font = ("Arial", 14)
                )                                                                       # Muestra la imagen en el label
            etiquetaicono.image = iconoaplicacion
            etiquetaicono.pack()                                                        # Empaqueta la etiqueta 

            botonnuevanota = ttk.Button(marco2, text="Nueva Nota", command=creaNota)    # Botón de iniciar sesión
            botonnuevanota.pack(pady=10)                                                # Empaqueta la entrada

            botonguardanotas = ttk.Button(marco2, text="Guardar Notas", command=guardaNotas)  # *NUEVO* - Botón de guardado de nota
            botonguardanotas.pack(pady=10)

            # *NUEVO* - CARGO LAS NOTAS DE LA BASE DE DATOS
            cursor.execute('SELECT * FROM notas')
            datos = cursor.fetchall()
            for i in datos:
                print("Hay una nota en la base de datos")
                cargaNota(i[1], i[2], i[3])
                #notas.append(Nota(i[1], i[2], i[3]))
                #identificador = identificador + 1
            for i in notas:                                                                     
                print(i.texto)
                print(i.color)
                print(i.fecha)  
            
        else:                                                                           # En caso de que no exista
            print("El usuario no es correcto ")
            raiz.after(3000, lambda:raiz.destroy())                                     # Cierra la ventana después de 3 segundos

def guardaNotas():                                                                                      # *NUEVO*
    for i in notas:                                                                                     # Para cada una de las notas
        print(i.texto)                                                                                  # Imprimo su contenido
        print(i.color)                                                                                  # Imprimo su color
        print(i.fecha)                                                                                  # Imprimo su fecha
        # Para que no hayan duplicados de una misma nota, no pueden haber dos notas con la misma fecha
        existe = False
        cursor.execute('SELECT * FROM notas WHERE fecha = "'+i.fecha+'"')
        datos = cursor.fetchall()
        for i in datos:
            existe = True
            print("La nota que intentas introducir exsite")
        if existe == False:    
            print("Como no existe, se guarda en la BD")
            cursor.execute("INSERT INTO notas VALUES(NULL,'"+i.texto+"','"+i.color+"','"+i.fecha+"');") # Inserto una a una las notas en la base de datos
        conexion.commit()                                                                               # Ejecuto la inserción
        

def creaNota():                                                                          
    global notas                                                                        # *NUEVO* - 'global' para traer la variable
    global identificador                                                                # *NUEVO*
    fecha = str(int(time.time()))                                                       # *NUEVO*
    notas.append(Nota('', '', fecha))                                                   # *NUEVO* - Se añade una nota a la lista

    for i in notas:                                                                     # *NUEVO*
        print("Texto: " + i.texto)
        print("Color: " + i.color)
        print("Fecha: " + i.fecha)  

    ventananuevanota = tk.Toplevel()                                                    # Toplevel -> se cierran al cerrar la ventana principal
    anchura = 350
    altura = 610
    ventananuevanota.geometry(str(anchura) + 'x' + str(altura) + '+100+100')
    texto = tk.Text(ventananuevanota, bg="white")
    texto.pack()
    identificadorpropio = identificador
    selectorcolor = ttk.Button(ventananuevanota, text="Cambiar color", command=lambda:cambiaColor(ventananuevanota, texto, identificadorpropio))     # *NUEVO*: 'texto', 'identificadorpropio' en cambiaColor
    selectorcolor.pack()

    identificador = identificador + 1                                                   # *NUEVO*

def cargaNota(mitexto, color, fecha):                                                   # *NUEVO*                                                                       
    global notas                                                                        
    global identificador                                                                
    notas.append(Nota(mitexto, color, fecha))                                                   

    for i in notas:                                                                     
        print(i.texto)
        print(i.color)
        print(i.fecha)  

    ventananuevanota = tk.Toplevel()
    anchura = 350
    altura = 610
    ventananuevanota.geometry(str(anchura) + 'x' + str(altura) + '+100+100')
    texto = tk.Text(ventananuevanota, bg="white")
                    
    try:
        texto.configure(bg = color)                                                     # *NUEVO*
        texto.insert("1.0", mitexto)                                                    # *NUEVO* - Para recuperar el texto de una nota guardada
        ventananuevanota.configure(bg = color)                                          # *NUEVO* - Para recuperar el color de una nota guardada
    except Exception as e:
        print(e)
    texto.pack()
    identificadorpropio = identificador
    selectorcolor = ttk.Button(ventananuevanota, text="Cambiar color", command=lambda:cambiaColor(ventananuevanota, texto, identificadorpropio))     # *NUEVO*: 'texto', 'identificadorpropio' en cambiaColor
    selectorcolor.pack()

    identificador = identificador + 1      

def cambiaColor(ventana, texto, identificador):                                         # *NUEVO*: 'texto', 'identificador'                                            
    nuevocolor = askcolor(title="Selecciona un color")                                  # Muestra un selector de color
    ventana.configure(bg = nuevocolor[1])                                               # Cambia el color de fondo a la vantana seleccionada
    texto.configure(bg = nuevocolor[1])                                                 # *NUEVO* - Cambia el color del cuadro de texto
    notas[identificador].color = nuevocolor[1]
    notas[identificador].texto = texto.get("1.0", tk.END)                               # *NUEVO* - Se guarda el texto escrito al cambiar de color

    print("El identificador es: " + str(identificador))                                 # *NUEVO*   
    for i in notas:                                                                     # *NUEVO*
        print(i.texto)
        print(i.color)
        print(i.fecha) 
    
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

# DECLARACIÓN DE VARIABLES GLOBALES

varusuario = tk.StringVar()                                                             # Variable para almacenar el usuario
varcontrasena = tk.StringVar()                                                          # Variable para almacenar la contraseña
varemail = tk.StringVar()                                                               # Variable para almacenar el email
notas = []                                                                              # *NUEVO*
identificador = 0                                                                       # *NUEVO* - Se inicializa un identificador

# AÑADIMOS WIDGETS A LA VENTANA

marco = ttk.Frame(raiz)                                                                 
marco.pack()                                                                            

version = tk.Label(marco,text="Notas v0.01")                                            # Crea un label
version.pack()                                                                          # Lo añade a la ventana

inputusuario = ttk.Entry(marco, textvariable = varusuario)                              # Crea una entrada para el nombre de usuario
inputusuario.insert(0,'Introduce tu usuario')                                           # Instrucción para el usuario
inputusuario.pack(pady=10, ipadx=8)                                                     # Empaqueta la entrada 

inputcontrasena = ttk.Entry(marco, textvariable = varcontrasena)                        # Crea una entrada para la contraseña
inputcontrasena.insert(0,'Introduce tu contrasena')                                     # Instrucción para el usuario
inputcontrasena.pack(pady=10, ipadx=8)                                                  # Empaqueta la entrada 

inputemail = ttk.Entry(marco, textvariable = varemail)                                  # Crea una entrada para el email
inputemail.insert(0,'Introduce tu email')                                               # Instrucción para el usuario
inputemail.pack(pady=10, ipadx=8)                                                       # Empaqueta la entrada 

botonlogin = ttk.Button(marco, text="Enviar", command=iniciaSesion)                     # Botón de iniciar sesión
botonlogin.pack(pady=10)                                                                # Empaqueta la entrada

# INTENTO INTRODUCIR ANTIALIAS EN WINDOWS Y LANZO EL BUCLE

try:                                                                                    # Intenta ejecutar
    from ctypes import windll                                                           # Importa la librería específica de GUI de Windows
    windll.shcore.SetProcessDpiAwareness(1)                                             # Activa el antialias para textos y demás cosas dentro de las interfaces
except Exception as e:                                                                  # Atrapa la excepción en caso de que se produzca
    print(e)                                                                            # Saca la excepción por pantalla
finally:                                                                                # En cualquier caso...
    raiz.mainloop()                                                                     # Detiene la ejecución y previene que la ventana se cierre
