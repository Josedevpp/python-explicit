# Tuplas    
"""Las tuplas en python son otra estructura de datos, similar a las listas que aprendimos en la anterior clase, similar en sintaxis, pero tienen sus diferencias, la principal es que las tuplas son inmutables, es decir, no se pueden modificar unas vez son creadas, esta caracteristica la hace ideal para almacenar datos que no cambian para almacenar datos a lo largo de la ejecución, veamos ejemplos:"""

chocololate = tuple() # Tiene sintaxis identica a las listas
chocololate = () # Su diferencia con listas es que empezaba con [], acá son ()
print(type(chocololate)) # Verificamos el tipo de dato

chocololate = (1, 3.5, "Josedevpp", True) #Almacena cualquier tipo de dato igual que las listas
print(chocololate[2]) #Tambien podemos acceder por medio de el indice
print(chocololate) # Imprimir todos los valores

"""Hasta el momento su principal diferencia es [] por (), con las listas, pero vamos paso por paso"""

# Si recuerdas cuando estabamos realizando operaciones con funciones como .reverse, .insert, etc. Pues acá existe limitación al realizar estas operaciones y ocurre por como mencionamos al principio, las tuplas no pueden pueden cambiar a lo largo de la ejecucion, no se pueden insertar valores, ni se pueden cambiar

chocololate = (1, 3.5, "Josedevpp", True)
# Supongamos que queremos cambiar el valor True a False

#chocololate[4] = False
#print(chocololate) # Si ejecutamos este codigo, nos muestra error, por lo mencionado anteriormente

# De igual manera para insertar un valor, no muestra las funciones y es porque no existen
# chocololate.insert(), no podemos revertir la lista con .reverse(), ni ordenas la lista son .sort()

"""Simplemente no se pueden realiazar estas operaciones, pero si se pueden ver el indice y contar cuantos elementos se repiten en nuestra tupla"""

print(chocololate.index("Josedevpp"))
print(chocololate.count(3.5))
# Podemos realizar un slice de nuestra tupla
print(chocololate[1:3]) #Entre el elemento 1 y 3, sin contar el 3

# Tambien podemos concatenar tuplas

chocololate = (1, 3.5, "Josedevpp", True)
my_tuple = (23, "User")
sum_tuple = chocololate + my_tuple
print(sum_tuple)

"""Ahora bien, como todo es posible en la programacion, tambien existe una forma de darle vuelta a las cosas, y aunque dijimos que no podemos modificar una tupla, si podemos darle vuelta y convertirla en una tupla "modificable", veamos un ejemplo:"""

chocololate = list(chocololate) # Primero tendriamos que cambiar nuestro tipo de dato de tupla a lista
print(type(chocololate)) # Ahora es una lista
# Por lo tanto, las listas son modificables, ya vimos todas las operaciones con funciones que podemos realizar

# Insertemos un valor
chocololate.insert(1, "Nuevo indice") #Insertamos en el indice 1
print(chocololate) # Verificamos 
# Podemos cambiar un valor
chocololate[0] = 1.1 # Cambiamos el indice 0 = 1, por 1.1
print(chocololate) # 

"""Por supuesto que siendo una lista podemos realizar todas las operaciones posibles, pero a ver, esto lo muestro con fines educativos, simplemente para que puedan ver la versatilidad de python, pero no es recomendado, primero porque debes analizar tus necesidades y evaluar que tipo de dato utilizar, es coherente que si quieres modificar los datos, para eso existen las listas, ahi pueden hacer todo, pero si utilizas valores constantes(No-cambian), pues para eso estan las tuplas, una vez creadas su valor se mantiene"""

chocololate = tuple(chocololate)
print(type(chocololate))
# Por ultimo, podemos eliminar la tupla, ma´s no un elemento por lo mismo de la inmutabilidad
#del chocololate[1] Error
del chocololate # del no es propio de lis(), tuple(), es una funcion en general
#print(chocololate) # Nos muestra error porque la variable chocololate no esta definida