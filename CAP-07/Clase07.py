# Sets o conjuntos
"""Los set con otra estructura de dato, similar a las listas y tuplas en cuanto a su sintexis, por ejemplo:"""
#Nosotros definiamos una lista de esta forma
my_list = list()
my_lista = []
print(type(my_lista))
#Definiamos tuplas de esta forma
my_tupla = tuple()
my_tuple = ()
print(type(my_tuple))

# Entonces para definir un set es de esta forma
my_set = set() #Igual que las listas y tuplas
my_set_ejemplo = {} # se hace con corchetes, diferente a las demas
print(type(my_set)) #Observamos que es tipo set, pero en la segunda variable hay un detalle
print(type(my_set_ejemplo)) # Nos muestra que es tipo dict( diccionario) pero, por que?
"""Bueno principalmente es cuestion del lenguaje, asi esta definido en python, no tiene mucha explicacion, aveces el lenguaje tiene su sintaxis que confunde, pero si agregamos valores a nuestra variable, el tipado cambia, veamos ejemplos para entender esto"""
my_set_ejemplo = {1, 2.4, "Josedevpp"}
print(type(my_set_ejemplo)) # Como podemos observar la variable que inicialmente declaro como dict, ahora con datos agregados mostro que es un set

# Bien, una vez explicado esto, podemos ver que operaciones se pueden realizar con los sets
print(len(my_set_ejemplo))

# Si queremos agregar un valor
my_set_ejemplo.add("Nuevo element") # Vemos que a diferencia de las listas para agregar un valor era .insert en el indice que seleccionamos, pero acá no existe eso
print(my_set_ejemplo) # Observamos que al imprimir, todos los valores cambian, en forma desordenada, expliquemos porque.

"""Las listas son elementos ordenados, es lo contrario con los sets, son elementos desordenados, al momento de insertar un valor en las listas lo haciamos indicando el indice, pero en una lista desordenada como son los sets, no se puede indicar el indice porque los valores se insertan en cualquier orden por cada print, entonces su principal diferencia es el ordenamiento de datos, otra diferencia es que no permite valores repetidos, veamos un claro ejemplo"""

my_set_ejemplo.add("Josedevpp")
print(my_set_ejemplo) # Como podemos visualizar, cambiar el orden de los valores y no imprime "Josedevpp", simplemente no admite valores repetidos
############################################################# Podemos realizar busquedas
print("Josedevpp" in my_set_ejemplo)
print("Hola" in my_set_ejemplo)

"""De igual manera si recuerdan como se hacia con str para comprobar si una cadena de texto contenia un caracter usando in y not in ó buscando un caracter usando .find() y .index(), en las listas podiamos buscar por medio del indice el elemento que contenia [1], en las tuplas tambien podemos acceder por medio del indice [2]"""

# Recordamos que las tuplas no se pueden modificar, las listas si, pero en los sets si se pueden eliminar algun elemento, cosa que no podiamos en las tuplas, si se puede hacer con listas y sets, veamos ejemplos:

my_set_ejemplo.remove("Nuevo element")
print(my_set_ejemplo) # Se elimina el elemento, accion que si se puede hacer con las listas, pero no con las tuplas, por lo mismo de la inmutabilidad

"""Tambien podemos de igual manera con las listas, vaciar las listas con .clear() y eliminar definitivamente los tipados como las listas, tuplas y los sets hasta el momento, utilizando la funcion del, porque como mencionamos del, no esta relacionada ni con list, tuples o sets, es algo propio del lenguaje"""

my_set_ejemplo.clear()
print(my_set_ejemplo) #vemos que arroja un conjunto vacio
print(len(my_set_ejemplo))

#del my_set_ejemplo
#print(my_set_ejemplo)

"""Cuando realizamos operaciones ., podemos observar que existen muchas más, pero en media, las mostradas son las más superficiales y comunes de menor medida, es cuestio de abarcar poco a poco los conceptos e ir interiorizando todo, practica y practica cada una de ellas"""
#Ejemplos

sets_lenguajes = {"python", "c++", "java"}
sets_futbol = {"barcelona", "madrid", "sevilla"}
new_sets = sets_lenguajes.union(sets_futbol) # El operador .union() sirve para una forma de unir o concatenar dos sets
print(new_sets)
# Si pensaste que haciendo solo un print set1 + set2 simplemente unia los dos sets, estas equivocado, aunque buena observacion, pero no se puede, porque no podemos concatenar los sets, solamente cadenas de texto
#print(sets_lenguajes + sets_futbol)
print(str(sets_lenguajes) + str(sets_futbol)) # De esta manera si se pueden unir, con la principal diferncia que solo se agregan las cadenas con sus respectivos {} y usando .union(), crea una nueva variable.

# Pero no podemos duplicar, ejemplo:
print(new_sets.union(new_sets)) # Los valores no se repiten, como se observa
print(new_sets.union({"javascript", "C"}))

"""Observando, si se pueden añadir elementos directamente en el print, sin necesidad de crear una variable, son cuestiones del lenguaje que permite por su tipado que suele ser fuerte y aveces debil"""

# Veamos otra funcion
print(new_sets.difference(sets_futbol)) # Se observa que se eliminaron las variables de futbol, por que?
# .difference(), como su nombre lo dice, diferencia los sets en este caso de futbol, si fuera al reves tendiamos las variables de fulbol y no de lenguaje.

# Es cuestión de explorar cada una de las variables, las principales son las mostradas en esta clase, pero pueden ir insvestigando cada una de ellas y ver su acción