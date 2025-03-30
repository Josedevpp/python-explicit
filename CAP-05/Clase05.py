#Listas

"""Las listas son otra estructura de datos más utilizadas para manipulación de datos, permiten almacenar cualquier tipo de dato y realizar cualquier operación con ellos, veamos como se comportan las listas."""
#Un punto importante es no confundir listas con arreglos, ya que los arreglos son estructuras de datos de tamaño fijo y solo pueden almacenar un tipo de dato, mientras que las listas son estructuras de datos dinámicas y pueden almacenar cualquier tipo de dato.

#Existen dos maneras de crear listas, la primera es utilizando corchetes [] y la segunda es utilizando la función list().

my_list = list()
my_other_list = []
print(type(my_other_list)) 
print(type(my_list)) 
# Verificamos que son tipo listas

#####################################################
# --> Podemos asignar cualquier tipo de dato a una lista, incluso listas dentro de listas.

my_list = [1, 2, 3, 4, 5]
my_other_list = [1, 1, 3, 5, 5, "Hola", True, int(1.5)]
print(my_list)
print(my_other_list)
print(len(my_list)) # Imprimimos la longitud de la list
print(len(my_other_list)) # Imprimimos la longitud de la lista

#Para acceder a un indice de la lista, se utiliza el mismo concepto que en los arreglos, es decir, se utiliza el nombre de la lista seguido del indice entre corchetes [].
print(my_list[0]) # Imprimimos el primer elemento de la lista, que es 1
print(my_list[-1]) # Imprimimos en orden inverso el último elemento de la lista, que es 5
#####################################################

# De igual manera como vimos en clase anterior con los str, podemos hacer uso de las funciones o metodos para realizar acciones concretas sobre las listas, como por ejemplo:

print(my_other_list.count(1)) # Imprimimos la cantidad de veces que se repite el 1 en la lista, que son 4 veces, porque True lo toma como 1, y el 1.5 cambiamos su tipo a int, por lo que es 1.
print(my_other_list.count(5)) # La cantidad de veces que se repite el 5 en la lista es 2 veces.
#####################################################

"""Podemos asignarle variables a cada uno de los elementos de la lista, y de esta manera acceder a cada uno de ellos, ejemplo:"""
a, b, c, d, e, f, g, h = my_other_list
print(a) #1     
print(b) #1
print(c) #3
print(d) #5
print(e) #5
print(f) #Hola  
print(g) #True
print(h) #1.5

#Algo menos eficiente, pero que funciona
a,b,c,d,e,f,g,h = my_other_list[1], my_other_list[2], my_other_list[3], my_other_list[0], my_other_list[5], my_other_list[6], my_other_list[7], my_other_list[4]
print(h) #Podemos cambiar el orden de las variables
#####################################################

#Podemos concatenar dos listas ó más, ejemplo:
print(my_list + my_other_list) #Concatenamos las dos listas, y nos devuelve una nueva lista con los elementos de ambas listas.
#####################################################

"""Ahora bien, tambien podemos añadir elementos de la lista, editar, cambiar, correr, eliminar, buscar, ordenar, etc. Veamos ejemplos de cada uno"""
#Añadir elementos a la lista -->

chocolate = ["negro", "blanco", "rojo"]

chocolate.append("rosa") # Añadimos el "rosa" al final de la lista (por defecto), y nos devuelve la lista con el nuevo elemento añadido.
print(chocolate) # ["chocolate", "blanco", "rojo", "rosa"]
chocolate.insert(0, "purpura") # Añadimos "purpura" al indice 0 de la lista.
chocolate[0] = "verde"
print(my_list) # ["verde", "chocolate", "blanco", "rojo", "rosa"]
cafe = ["taza"]
chocolate.extend(cafe)
print(chocolate) # ["verde", "chocolate", "blanco", "rojo", "rosa", "taza"]
#####################################################
#Eliminar elementos de la lista -->

chocolate.remove("verde") # Eliminamos el primer elemento que se repite en la lista.
print(chocolate) # ["chocolate", "blanco", "rojo", "rosa"]
chocolate.pop() # Sin argumento se elimina el último elemento de la lista, en este caso "taza"
print(chocolate) # ["chocolate", "blanco", "rojo", "rosa"]
#taza_pop = chocolate.pop() # En una nueva variable podemos almacenar el elemento eliminado "taza"
#print(taza_pop)
#chocolate.clear() # Borramos chocolate, pero guardamos en taza_pop
#print(chocolate)
del chocolate[2] # Eliminamos por indice 2("rojo), a diferencia de remove que elimina el primero valor encontrado
print(chocolate)
######################################################Busqueda de elementos en la lista -->

print(chocolate.index("blanco")) # Buscamos el indice de "blanco" en la lista
print(chocolate.count("negro")) #Busca la cantidad repetida del elemento "negro" es 1
print("rosa" in chocolate) # Verificamos si el "rosa" esta en la lista, devuelve True o False.
######################################################Ordenar y revertir

""".sort vs .reverse, cuando queremos ser eficientes con el uso de memoria, .sort modifica en su lugar y sorted crea una copia de la lista."""
 
chocolate.reverse() #Cambia los los elementos al reves
print(chocolate)
chocolate.sort() # Mueve los elementos en orden numerico de menor a mayor, pero si es es str, entonces en orden alfabetico.
print(chocolate) 

"""sorted vs reversed, lo ocupamos cuando necesitamos preservar los datos originales, reserved, es util para bucles cuando solo necesitas iterar"""
nuevos_sabores = sorted(chocolate) # Creamos una nueva lista con los elementos de la lista original ordenados de menor a mayor alfabetico ó numerico.
print(nuevos_sabores) 

chocolate = nuevos_sabores
for chocolate in reversed(chocolate):
 print(chocolate) # Devuelve un iterador (no una     lista) con los elementos en orden inverso
######################################################Copiar

chocolate = ["negro", "blanco"]
chocolate.copy()
nuevos_sabores = chocolate.copy()
print(nuevos_sabores) # Copiamos sin afectar a la original
list(chocolate)
print(chocolate) # Otra forma de crear copia
######################################################Utilidades

print(min(chocolate)) # Minima letra orden alfabetico
print(max(chocolate)) # Maxima letra orden alfabetico
print(len(str(chocolate))) # Longitud de letras con str
#print(sum(chocolate)) # No permite sumar str