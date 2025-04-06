# Bucles

"""Los bucles en python, son estructuras de datos, para repetir bloques de codigo, sin tener que reescribir el mismo codigo, cuando tenemos tareas repetitivas, existen dos tipos, for(para) y while(mientras)"""

# while --> se usa cuando queremos repetir codigo mientras la condicion se cumpla, no precisamente tenemos que saber cuantas veces se tiene que repetir
# for --> es util cuando sabemos cuantas vesces queremos repetir el codigo

# ejemplos, while:
# La sintaxis es muy limpia
#1. variable y su valor
#2. mientras (comparacion) (valor)
#3. imprime esto
#4. variables += (valor), evita bucle infinito

# contador = 0 # Nuesto contador inicia en 0
# while contador < 10: # Mientras contador sea menor a 10, entonces
#     print(contador) # Imprime contador
#     contador += 1 # Evitamos un bucle infinito, ya que ira incrementando de 1 en 1 hasta que se cumpla la condicion.

"""Existe otro metodo para frenar un bucle infinito y se llama break, veamos su sintaxis"""

# contador = 0
# while contador < 10: # Compara y sino cumple, entonces ejecuta el codigo
#     contador += 1 # Incrementa de 0 a 1
#     print(contador) # Imprime el nuevo valor 1
#     if contador == 10: # Compara si es igual que 10, sino vuelve a comparar
#         break # Si es igual que 10 entonces para

"""Generalmente el break se utiliza cuando tenemos demasiados elementos y no sabemos cuando tiene que recorrer el bucle, para eso funciona el break, veamos un ejemplo mas claro"""

# contador = 0
# while contador <= 100:
#     print(contador)
#     contador += 1
#     if contador == 50: # En este caso, tenemos una lista de recorre 100 elementos y queremos encontrar el 50
#         print("Encontre el numero: 50")
#         break
# Ejemplo claro para que sirve el break

"""Tambien podemos saltarnos iteraciones en concreto, para eso existe el continue --> basicamente es omite imprimir los valores que solicitemos en la condicion, veamos ejemplos"""
 # Supongamos que de la lista solo queremos los numeros pares

# contador = 0
# while contador < 20:
#     contador += 1
#     if contador % 2 == 0: # decimos que los numeros que sean multiplos de 2, se los salte con la instruccion continue
#         continue # si la condicion se cumple, entonces salta y vuelve a comparar e iterar
#     print(contador) #

"""Ahora veamos un caso practico de entrada de datos por parte del usuario y veremos como en programacion, tenemos que tener en cuenta todas las posibilidades a ejecutar."""

# Pidele a el usuario que ingrese un numero positivo

# numero = -1 # Iniciamos en -1 para garantizar que al menos una vez se ejecute el siguiente bucle
# while numero < 0: # Entonces como -1 es menor a 0, y no se cumple, entra en bucle
#     numero = int(input("Ingrese un numero positivo: ")) # Ahora pedimos que ingrese un numero
#     if numero < 0: # Si ingresa un numero positivo y compara numero < 0, como es False, entonces omite este bloque y vuelve a comparar
#         print("Dije, numero positivo y no negativo :V") # Pero sino ingresaste un numero positivo, y si un negativo, entonces el if es True y muestra el print del if
# print(f"El numero que has introducido {numero}") # Ahora como ingresamos un numero > 0, es True, ejecuta este print mencionando el numero que ingresaste

"""Por ahora todo bien, nustro programa funciona, pero que pasa en la situacion que nuestro usuario se rebelde e ingrese un digito que no sea numero, por ejemplo una letra. Prueba y me dices que pasa"""

"""Como pudiste observar el programa se corrompe, y esto se debe porque cuando solicitamos el numero al usuario, estamos tipando el valor de nuestra variable (numero) a entero, para esto existe una solución y se llama (Try except) lo que hace es envolver nuestro codigo que puede generar problemas y pasarle una solucion, en este caso seria recordarle al usuario que ingrese un numero, no otro caracter diferente."""
# numero = -1 
# while numero < 0: 
#     try: # Envolvemos el bloque que genera conflicto
#         numero = int(input("Ingrese un numero positivo: ")) 
#         if numero < 0: 
#             print("Dije, numero positivo y no negativo :V")
#     except: # Y pasamos la solucion que evitara que la ejecucion de error
#         print("Te dije que numero, no entiendes!") 
# print(f"El numero que has introducido {numero}")
########################################

# for
# El bucle for cumple más una funcion de iteracion , es decir va iterando de valor en valor hasta llegar al final o donde nosotros queremos o sabemos que hay que llegar, veamos ejemplos

# Supongamos que tenemos una lista

coches = ["Mercedes", "Nissan", "Toyota", "BMW"] # Nuetra lista de elementos
for marcas in coches: # para cada marca iterar coches, seria una forma limpia y clara de ver su sintaxis
    print(marcas) # Imprime cada iteracion en marcas

# Tambien podemos iterar elementos uno por uno

nombre = "Josedevpp"
for letra in nombre: # Hace lo mismo pero esta vez itera cada caracter del elemento
    print(letra)

# Podemos recuperar por indice.
print("\nrecuperar por indice:")
coches = ["Mercedes", "Nissan", "Toyota", "BMW"]
for indice, marcas in enumerate(coches): # creamos la variable indice que almacena enumerate y la variable marcas que itera los coches uno por uno
    print(f"El indice {indice}, pertenece a {marcas}") # Imprimos con el formatter string y nos muestra el indice de cada elemento

# Podemos anidar bucles
print("\nanidar bucles:")
marcas = ["Mercedes", "Nissan", "Toyota", "BMW"]
precios = [19.000, 20.000, 30.000, 40.00]
for coches in marcas:
    for valor in precios:
        print(f"{coches}= ${valor}")

# Tambien tenemos el break

colores = ["rojo", "verde", "azul", "morado"]
for color in colores:
    print(color)
    if color == "azul": # Funciona igualmente para detener la iteracion cuando color sea igual que "azul,"
        break # Frena el programa

# De igual manera podemos jugar con los indices, que si el if encuentra el azul, nos muestre el indice o cualquier valor
print("\n con break:")
colores = ["rojo", "verde", "azul", "morado"]
for indice, color in enumerate(colores):
    if color == "azul": # Funciona igualmente para detener la iteracion cuando color sea igual que "azul,"
        print(f"El indice de {color} es {indice}") # Mostramos el valor que buscamos.
        break # Frena el programa
 # En este punto podemos ignorar el break, si queremos encontrar el valor pero queremos seguir ejecutando el bucle, simplemente no colocamos el break
print("\nsin break:")
colores = ["rojo", "verde", "azul", "morado"]
for indice, color in enumerate(colores):
    print(color)
    if color == "azul":
        print(f"El indice de {color} es {indice}") 

"""Realmente tienes que optimizar tu logica, porque si solamente buscamos un elemento, es totalmente innecesario seguir ejecutando el bucle."""
"""Tambien podemos usar continue, si queremos omitir un valor y que no se imprima, pero siga ejecutandose el bucle"""
print("\ncontinue:")
colores = ["rojo", "verde", "azul", "morado"]
for indice, color in enumerate(colores):
    if color == "azul":
        continue # Al encontrar el color azul, salta la iteracion y sigue con el bucle
    print(color)

# Comprension de listas con for

# Supogamos que tenemos una lista con elementos en minuscula y los queremos transformar en mayusculas
print("\ncomprehension list with for and funtion upper.():")
nombre = ["jose", "marcos", "elias", "samuel"]
nombres_mayus = [mayus.upper() for mayus in nombre] # Creamos una lista "nombre_mayus" donde se va almacenar la nueva lista con la operacion .upper() que cambia a mayusculas cada elemento e iteramos cada elemento con for
print(nombres_mayus) # e imprimimos la lista creada con los elementos transformados

# Podemos hacer comprension de listas con condicionales, if, veamos un ejemplo

# Un ejemplo muy tipico y sencillo es devolver los numeros pares de una lis
print("\ncomprehension list with if:")
nueva_lista = [num for num in [1,2,3,4,5,6,7,8,9] if num % 2 == 0]
print(nueva_lista)

"""Algo mas optimo para no crear esa lista de numeros en medio del for, existe range(), ya vimos que es, veamos un ejemplo para aclarar"""

""" print("\nrange:")
numeros = range(5) """ # range no crea una lista, sino que genera un rango que parte de (0...5), pero genera los elementos en base a la demanda, a diferencia de las listas que tienes crear los valores y definirlos

# print("\nrange en for:")
# for nums in numeros:
#     print(nums)
# # ó directamente el range
# print("\ndirectamente en for range():")
# for nums in range(5):
#     print(nums)
# print("\nrango entre definicion:")
# for nums in range(5,10):
#     print(nums)
# print("\npor pasos:")
# for nums in range(0,10,2): # pasos de 2 en 2
#     print(nums)
# print("\nrangos negativos:")
# for nums in range(-10,0):
#     print(nums)
print("\nrangos inverso con pasos de 3:")
for nums in range(10,0,-1):
    print(nums)
