# Dict (Diccionarios)

# La forma para tipar como vimos en los anteriores como list[], tuplas(), sets{}, pues algo peculiar, es que tambien los dicts son con {}, veamos un ejemplo:

mi_diccionario = dict()
mi_otro_dict = {}
print(type(mi_diccionario))
print(type(mi_otro_dict))

# Los diccionarios son almacenamientos de datos que funcionan clave-valor, son pares de datos, esto los hace rapido para acceder a su valor, mediante su clave. Los hace perfectos para las bases de datos o configuraciones de las aplicaciones, etc.

mi_diccionario = {"Nombre":"Josedevpp","Trabajo":"Freelance", "Edad":24}
# Esta correlacion de datos funciona mediante su valor, ahora veamos cuales operaciones podemos realizar, sus diferencias con el resto de estructuras de datos y sus limitaciones
mi_diccionario = {"Nombre":"Josedevpp", 
                  "Trabajo":"Freelance", 
                  "Edad":24,
                  244:"Java",
                  "Lenguajes fav": {"Kotlin", "C++"} # Esto es un set
                  } # Tambien lo podemos formatear
print(mi_diccionario)
print(mi_otro_dict)

"""Los diccionarios son muy versariles, podemos almacenar como valores, listas, sets ó incluso más diccionarios, otra peculariedad es la forma facil para acceder a sus datos, como recordabamos para acceder a los datos de una lista, lo haciamos por medio de su indice[0], para acceder a los valores de una tupla, lo haciamos mediante por medio del indice[0], en los sets no funciona una manera de acceder a un valor, porque es una lista desordenada, sus valores cambian y no mantienen un indice, pero si podiamos comprobar si existia un valor en el set mediante "valor" in set_name, pues acá no lo hacemos por medio de indice, sino por su clave con ["clave"], mediante esta solicitud, podemos ver los valores que contiene nuestro diccionario, veamos ejemplos:"""

print(mi_diccionario["Lenguajes fav"])

# Otra versatilidad es que podemos actualizar los valores de nuestras claves, ejemplo:

mi_diccionario["Nombre"] = "Saul"
print(mi_diccionario)

# Tambien podemos agregar valores, como lo hicimos en las listas .insert(indice, valor), en las tuplas .insert(indice, valor) y en los sets .add(valor) que no existe su indice, en los dict la forma es simple de agregar, veamos como:

mi_diccionario["Deporte fav"] = "Tenis"
print(mi_diccionario) # Se puede agregar directamente, asi como en el set con .union({valor}), sin crear variables

# Podemos eliminar claves y sus valores
#mi_diccionario.clear() # limpiar todo el diccionario
del mi_diccionario["Deporte fav"]
print(mi_diccionario)

"""Por esta estas razones, python es intuitivo, porque anteriormente la funcion del, nos eliminaba completamente la variable, en este caso, podemos darle como parametro nuestro valor y asi poder eliminar solamente esa clave-valor, ojo que tambien podemos eliminar completamente el diccionario, tiene ambas funciones. Veamos más operaciones"""

# Podemos comprobar si un valor existe ó acceder mediante su clave

print("Saul" in mi_diccionario) # Ojo, nos arroja falso porque lo que busca en el diccionario es la clave, no el valor, para que sea True, tendriamos que poner su clave
print("Nombre" in mi_diccionario)
# Y para acceder a su valor lo hacemos mediante su clave
print(mi_diccionario["Nombre"])

"""De igual manera los diccionarios tienen diferente operaciones que podemos realizar, no tiene tantas limitaciones, exploremos un par"""

print(mi_diccionario.items()) # Obtenemos clave-valor de todo el diccionario
print(mi_diccionario.values()) # Solo retorna los valores
#mi_diccionario.update
print(mi_diccionario.keys()) # Obtenemos solo las claves
#print(mi_diccionario.fromkeys()) # Con fromkeys lo que hacemos es una operacion más compleja, en forma sencilla de explicar, seria que creamos un nuevo diccionario con las claves anteriores, pero valores vacios.

new_diccionario = dict.fromkeys(mi_diccionario)
print(new_diccionario) # De esta manera podemos crear un nuevo diccionario y apartir de acá podemos editar nuestro nuevo diccionario ó incluso pasarle las claves sin una variable anteriormente definida

new_diccionario = dict.fromkeys(("Nombre", "Edad", "Puesto"))
print(new_diccionario)
new_diccionario = {"Nombre":"Jose, Matias", "Age":"23, 43", "Colorfav": "Azul, Verde"}
print(new_diccionario) #Ven lo tipado debil que es python, permite reasignar valores de las claves en este caso