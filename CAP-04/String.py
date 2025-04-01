# Strings

"""En python las cadenas de texto son un tipo de dato mas utilizado dentro del lenguaje, ya que manipulamos texto de diferentes formas, basta con decclaras con como comillas simples o dobles, y podemos hacer operaciones con ellas como concatenar, repetir, etc."""


#Operaciones que podemos hacer
#1.Concatenar cadenas de texto usando +, tambien obtener la longitud de la cadena usando len()
#2.Repetir cadenas de texto usando *.
#3.Convertir cadenas de texto a mayusculas usando upper() y a minusculas usando lower()
#4.Convertir cadenas de texto a listas usando split()
#5.Formatear cadenas de texto usando format(), operador % y f-strings que es la forma mas moderna de hacerlo.
#6.Eliminar espacios en blanco al inicio y al final de la cadena usando strip()
#7.Saltos de linea y tabulaciones usando \n y \t respectivamente.
#8.Descomponer cadenas de texto usando slicing, que es una forma de acceder a una parte de la cadena usando [inicio:fin] o [inicio:fin:paso].
#9.Contar la cantidad de veces que aparece un caracter en una cadena usando count()
#10.Reemplazar un caracter por otro usando replace()
#11.Buscar un caracter en una cadena usando find() y index()
#12.Comprobar si una cadena empieza o termina con un caracter usando startswith() y endswith()
#13.Comprobar si una cadena contiene un caracter usando in y not in.
#14.Comprobar si una cadena es alfanumerica usando isalnum()
#15.Comprobar si una cadena es numerica usando isdigit() ó isnumeric()
#16.Comprobar si una cadena es alfabetica usando isalpha()

#Estos ejercicios y muchos más podemos realizar con cadenas de texto, pero no es necesario aprenderlos todos, ya que con los ejemplos anteriores podemos ver como funcionan y aprender a usarlos en el momento que los necesitemos.

"""Como observaste en python existen funciones definidas para realizar una accion especifica, como len() para obtener la longitud de una cadena, o upper() para convertir una cadena a mayusculas, etc. Estas funciones son parte de la libreria estandar de python y podemos usarlas en cualquier momento."""

#Para ver las librerias que tenemos instaladas en nuestro sistema, podemos usar el comando pip list en la terminal, o pip freeze para ver las versiones de cada libreria instalada.

#Para ver las funciones, dirigirte a /CAP-04/img/builtin-funtions-png

#Veamos ejemplos para tener mas clara las funciones

#Concatenar con string
nombre = "Juan"
apellido = "Pérez"
print(f"Hola {nombre} {apellido}") #Hola Juan Pérez
print(nombre + " " + apellido) #Hola Juan Pérez
#Concatenar con integer
#nombre = 10
#apellido = 20
#print(f"Hola {nombre} {apellido}") #Hola 10 20
#print(nombre + " " + apellido) #Hola 10 20
#Concatenar con float
#nombre = 10.5
#apellido = 20.5
#print(f"Hola {nombre} {apellido}") #Hola 10.5 20.5
"""Estamos concatenando cadenas de texto, pero si intentamos concatenar un numero con una cadena de texto, nos dara un error, ya que no podemos concatenar diferentes tipos de datos, por lo que debemos convertir el numero a cadena de texto usando str() o convertir la cadena de texto a numero usando int() o float(). Para eso funciona formatter strings, de lo contrario tendriamos que declarar su tipo, ejemplo:"""

#nombre = 10.5
#apellido = 20.5
#print("Hola", str(nombre), str(apellido))

#Obtener longitud de la cadena
print(len(nombre)) #4
print(len(apellido)) #5

#Comvertir a mayusculas
print(nombre.upper()) #JUAN
print(apellido.upper()) #PÉREZ

#Convertir a minusculas
print(nombre.lower()) #juan
print(apellido.lower()) #perez

#Convertir a listas
print(nombre.split()) #['Juan']
print(apellido.split()) #['Pérez']

#Formatear cadenas
print("Hola {} {}".format(nombre, apellido)) #Hola Juan Pérez
print("Hola %s %s" % (nombre, apellido)) #Hola Juan Pérez
print(f"Hola {nombre} {apellido}") # <-- Lo más usado
print("Hola " + nombre + " " + apellido) # <-- Lo menos usado

#Eliminar espacios en blanco al inicio y al final de la cadena
print(nombre.strip()) #Juan

#Saltos de linea y tabulaciones
print(nombre + " " + apellido) #Espacio
print(nombre + "\t" + apellido) #Tabulación
print(nombre + "\n" + apellido) #Salto de linea

#División [0...3] Juan = 4 caracteres
print(nombre[0:2]) #Ju
print(nombre[0:3]) #Jua
#Descomponer cadenas de texto usando slicing
lenguaje = "python"
a,b,c,d,e,f = lenguaje
print(a) #p
print(b) #y
print(c) #t
print(d) #h
print(e) #o
print(f) #n
#reverse
print(lenguaje[::-1]) #¿Por que de -1? esto indica que queremos recorrer la cadena de derecha a izquierda, y el : indica que queremos recorrer toda la cadena.[::-2] para invertir cada 2 caracteres.
print(lenguaje[::-2])
print(lenguaje[-2]) #-2 indica que queremos el segundo caracter de derecha a izquierda.
print(lenguaje[0:6:2]) #pyhn, [0:6] indica que queremos recorrer toda la cadena, y [::2] indica que queremos recorrer cada 2 caracteres.

#Cantidad de veces que aparece un caracter en una cadena
print(nombre.count("a")) #1
print(apellido.count("é")) #1, no 2 porque una esta tildada y la otra no

#Reemplazar un caracter por otro
print(nombre.replace("a", "o")) #Juon

#Buscar un caracter en una cadena
print(nombre.find("a")) #1
print(nombre.index("a")) #1, si no lo encuentra devuelve un error

#Comprobar si una cadena empieza o termina con un caracter
print(nombre.startswith("J")) #True
print(nombre.endswith("n")) #True

#Comprobar si una cadena contiene un caracter
print("a" in nombre) #True
print("a" not in nombre) #False

#Comprobar si una cadena es alfanumerica
print(nombre.isalnum()) #True
#Es alfanumerica si contiene letras y numeros, pero no espacios ni caracteres especiales

#Comprobar si una cadena es numerica
print(nombre.isdigit()) #False
print(nombre.isnumeric()) #False

#Comprobar si una cadena es alfabetica
print(nombre.isalpha()) #True

"""Los ultimos ejercicios son metodos ó funciones, estas se pueden utilizar para realizar tareas simples, para ello llamaremos a la variable y pondremos .Name_funtion() y podemos utilizar todas las anteriores y más"""

#print(lenguaje.Name_funtion())