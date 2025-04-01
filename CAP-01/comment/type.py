'''Como explicabamos en la guia de Notion
Los primeros pasos para empezar a codificar en python
Eran imprimiendo los tipos de datos
Seguido de como realizar comentarios'''
"""En este momento estamos viendo como realizar
comentarios multilinea de diferentes formas"""
#Todas las maneras estan correctas, aunque es...
#recomendado ser explicitos para comentar bloques
#de codigo

"""Explicamos la forma de ejecutar un print
   por medio de la terminal o pulsando Run python file
   en VScode"""
#Recordamos para imprimir en terminal, nos dirigimos
#al archivo.py y colocamos: python ejemplo.py
#Y la forma mas practica es pulsando Run python file
"""La sintaxis de print en python es sencilla, veamos
   un ejemplo de como funciona"""
#---> print("Valor a imprimir")
"""Partiendo de un punto de vista observativo, nos 
   damos cuenta que a diferencia de otros lenguajes
   en python no se utilizan cierres de :, ;, () ó {}
   y esto es simple de explicar, como explicamos
   la filosofia de python es ser legible, simple y explicito, eliminar los cierres de bloques de  codigo hace que sea mas simple ya que se tiene que parecer lo mas identico al lenguaje humano (ingles)pero en su lugar utiliza la indentación que seria como bloques de espacio para definir si una linea pertenece a un bloque de codigo, veamos un ejemplo:"""
# if 10 < 5
   #print("Esto seria false") <-- El espacio asignado
                                # define que print    es  parte del bloque de codigo
#print("Seria true") <-- Este print ya no pertenece a
                        #la condicion 
"""Entonces puede paracer confuso al momento de conocer otros lenguajes que si utilizan caracteres para delimitar bloques de codigo y acepten que el indentado este desordenado y aun asi se puede ejecutar el codigo"""
#Ahora veamos ejemplos de print -->

print("Ejemplo de print") #imprimiendo texto
print(23) #imprimendo enteros
print("true") #imprimiendo booleanos
print(2.3453) #imrprimiendo decimales
print(["manzana", "cereza", "pera"]) #imprimiendo listas ó arreglos
print(1 + 2j) #uso de operaciones con numeros complejos
print(None) #imprime un valor nulo
print({"rojo", "verde", "morado"}) #imprime set
print({"nombre": "jose", "edad": 25} )

#Si queremos validar que tipos de datos son
#basta con agregar type antes del valor, ejemplo -->

print(type("Ejemplo de print")) #str
print(type(23)) #int
print(type(True)) #bool
print(type(2.3453)) #float
print(type(["manzana", "cereza", "pera"])) #array/list
print(type(1 + 2j)) #complex
print(type(None)) #Nulltype
print(type({"rojo", "verde", "morado"})) #set
print(type({"nombre": "carlos", "edad": "35"})) #dict
print(type(range(10, 7, 6))) #range
#--------------------------------------------------#
'''Resumen: entonces aprendimos como realizar comentarios en nuestro codigo, luego hablamos de la sintaxis de python y por que no utiliza delimitadores de ;, (), {} ó [] y por ultimo vimos como imprimir valores de diferentes tipos y como verificar que tipos de datos estamos imprimiendo.'''

#Podemos cambiar los tipos de datos, por ejemplo:

#float to int
gravity = 9.31
print(int(gravity))
pasamos = int(gravity)
print(type(pasamos))

#int to float
metros = 100
print(float(metros))
cambiamos = float(metros)
print(type(cambiamos))

#int to str
goles = 10
print(goles)
convertion = str(goles)
print(type(convertion))

#str a float
name = 10.6
print(float(name))
print(type(name)) 
cambio = float(name)
print(type(cambio))

#str to list
first_name = 'nicole'
print(list(first_name))
letras = list(first_name)
print(type(letras))