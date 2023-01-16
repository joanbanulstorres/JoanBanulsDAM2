#Programa Notas (c) 2022 Joan Banuls Torres

#Créditos iniciales
print("Programa notas")                                     # Indico el nombre del programa
print("(c) 2022 Joan Banuls Torres")                        # Indico el nombre del autor

class Nota:                                                 # Declaramos una clase
    def __init__(self, contenido, color, fecha):            # Constructor
        self.contenido = contenido                          # Propiedad contenido
        self.color = color                                  # Propiedad color
        self.fecha = fecha                                  # Propiedad fecha

nota = "Esta es mi primera nota"                            # Creo un valor inicial para la variable
notas = []                                                  # Creo una lista vacía

print("Introduce el contenido de tu nota")                  # Creo un valor inicial para la variable
nota = input()                                              # Almaceno la entrada del usuario en la variable
print("El contenido de tu nota es: " + nota)                # La muestro por pantalla

for i in range(0, 4):                                       # Permito al usuario introducir varias notas
    print("Introduce el contenido de la nota")              # Le solicito al usuario el contenido de la nota
    contenido = input()                                     # Capturo la entrada
    print("Introduce el color de la nota")                  # Le solicito al usuario el color de la nota
    color = input()                                         # Capturo la entrada
    print("Introduce la fecha de la nota")                  # Le solicito al usuario la fecha de la nota
    fecha = input()                                         # Capturo la entrada
    if contenido == "salir":                                # Si lo que introduce el usuario es "salir"
        break                                               # Salgo del bucle
    else:                                                   # En caso contrario   
        notas.append(Nota(contenido, color, fecha))         # Añado una nueva nota vacía a la lista

print("El contenido de las notas es: ")                         
for i in notas:                                             # Para cada una de las notas
    print(i.contenido)                                      # Imprimo su contenido
    print(i.color)                                          # Imprimo su color
    print(i.fecha)                                          # Imprimo su fecha
 
