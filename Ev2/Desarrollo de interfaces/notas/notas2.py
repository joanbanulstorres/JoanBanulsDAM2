#Programa Notas (c) 2022 Joan Banuls Torres

import sqlite3 as bd                                            # *NUEVO* - Importo la librería de SQLite
import time                                                     # *NUEVO* - Importo la librería de tratamiento de fechas
import re                                                       # *NUEVO* - Importo la librería de expresiones regulares

conexion = bd.connect("notas.sqlite")                           # *NUEVO* - Indico el nombre de la base de datos
cursor = conexion.cursor()                                      # *NUEVO* - Creo un cursor                  
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

#Créditos iniciales
print("Programa notas")                                         # Indico el nombre del programa
print("(c) 2022 Joan Banuls Torres")                            # Indico el nombre del autor

class Nota:                                                     # Declaramos una clase
    def __init__(self, contenido, color, fecha):                # Constructor
        self.contenido = contenido                              # Propiedad texto
        self.color = color                                      # Propiedad color
        self.fecha = fecha                                      # Propiedad fecha

usuario = "Esta es mi primera nota"                             # Creo un valor inicial para la variable
notas = []                                                      # Creo una lista vacía

print("Introduce el usuario")                                                                   # *NUEVO* - Le solicito al usuario un nombre de usuario
usuario = input()                                                                               # *NUEVO* - Entrada del usuario
print("El usuario es: " + usuario)                                                              # *NUEVO* - Le muestro el usuario
print("Introduce la contraseña")                                                                # *NUEVO* - Le solicito al usuario la contraseña
contrasena = input()                                                                            # *NUEVO* - Entrada de la contraseña
print("Introduce el email")                                                                     # *NUEVO* - Le solicito al usuario el email
email = input()                                                                                 # *NUEVO* - Entrada del email

expresion = re.compile(r'([A-Za-z0-9]+[.-])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+')           # *NUEVO* - Creo una expresión regular para un correo elctrónico
if re.fullmatch(expresion,email):                                                                   # *NUEVO* - Si el correo electrónico introducido es correcto
    print("Tu correo electrónico es válido")                                                        # *NUEVO* - Le digo que es correcto
    cursor.execute("INSERT INTO usuarios VALUES(NULL,'"+usuario+"','"+contrasena+"','"+email+"');") # *NUEVO* - Inserto el usuario en la BD
    conexion.commit()                                                                               # *NUEVO* - Ejecuto la inserción
else:                                                                                               # *NUEVO* - Si el correo electrónico introducido es incorrecto
    print("Tu correo electrónico no es válido")                                                     # *NUEVO* - Le digo que es incorrecto

for i in range(0, 4):                                           # Permito al usuario introducir varias notas
    print("Introduce el contenido de la nota")                  # Le solicito al usuario el contenido de la nota
    entrada = input()                                           # Capturo la entrada
    print("Introduce el color de la nota")                      # Le solicito al usuario el color de la nota
    color = input()                                             # Capturo la entrada
    #print("Introduce la fecha de la nota")                     # Le solicito al usuario la fecha de la nota
    fecha = str(int(time.time()))                               # *NUEVO*
    if entrada == "salir":                                      # Si lo que introduce el usuario es "salir"
        break                                                   # Salgo del bucle
    else:                                                       # En caso contrario   
        notas.append(Nota(contenido, color, fecha))             # Añado una nueva nota vacía a la lista

print("El contenido de las notas es: ")                         
for i in notas:                                                                                     # Para cada una de las notas
    print(i.contenido)                                                                              # Imprimo su contenido
    print(i.color)                                                                                  # Imprimo su color
    print(i.fecha)                                                                                  # Imprimo su fecha
    cursor.execute("INSERT INTO notas VALUES(NULL,'"+i.contenido+"','"+i.color+"','"+i.fecha+"');") # *NUEVO* - Inserto una a una las notas en la base de datos
    conexion.commit()                                                                               # *NUEVO* - Ejecuto la inserción
