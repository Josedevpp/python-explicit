# Funciones en python

"""
Las funciones en python, son bloques de codigo, reutilizables de codigo que reaizan una tarea concreta
--> la sintaxis basica de las funciones es muy limpia en python
def nombre_funcion (parametro1, parametro2...):
 #cuerpo de la funcion 
 #codigo que se ejecutara cuando la funcion sea llamada
 return resultado_final #opcional

 En python una funcion se declara como def --> definicion, como ya sabemos python es muy verboso, veamos ejemplos:
"""
print("\nejemplo")
def saludar(): # Funcion sin parametro
    print("Hola, saludos!")

def suma(a, b): # Funcion con parametro
    return a + b
# Llamamos a las funciones
saludar()
resultado = suma(5, 5)

print("\nmultiples funciones, reutilizable")
def saludos(nombre):
    print(f"Hola👋👋 {nombre} ")

saludos("Josedevpp")
saludos("Curso de python")
saludos("Emilia")

print("\nparametros por defecto")
def saludo(nombre="Cursante"):
    print(f"Hola, {nombre}")
# Llamada a la funcion
saludo()
saludo("Josedevpp")
# Otro ejemplo
def multiplicar(a, b = 2): # Definimos por defecto que b = 2
    return a * b
print(multiplicar(2)) # El valor es opcional, pero tambien lo puedes declarar
print(multiplicar(2, 3))
# Llamada a la funcion

print("\nparametro posicional vs nombre")
def describirme(nombre, edad, genero):
    print(f"{nombre}, tiene {edad} y es {genero}")

describirme("Josedevpp", 24, "Maculino") # por posicion
describirme(edad= 24, genero= "Maculino", nombre= "Josedevpp") # por nombre

print("\nparametro por longitud de variable (*arg)")
def sumar_num(*arg): # definimos el nombre de la funcion y con el argumento *arg
    suma = 0 # Creamos una variable suma que inicia en 0
    for numeros in arg: # Creamos un ciclo para iterar numeros(donde se almacena), los arg(argumentos o parametros)
        suma += numeros # Iteramos, como suma valia 0, y numeros(argumentos vale 1), ahora suma vale 1 y asi hasta sumar todos los numeros
    return suma # Retorna el valor de suma con cada iteracion hecha
print(sumar_num(1,2,4,5,6))
print(sumar_num(1,2,4,4,4,4,5,6,6))
print(sumar_num(3,5,2,4,6,5,6))

print("\nargumentos de clave-valor (**kwargs)")
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items(): # iteramos para clave y valor en kwargs.items() (todos los items por defecto)
        print(f"{clave}: {valor}")
mostrar_info(nombre="Josedevpp", hobbi="Correr", edad=24)
print("\n")
mostrar_info(comida_fav="pizza", nombre="Matias", peso="78kg")
print("\n")
mostrar_info(altura=1.70, deporte="natacion", nombre="Carmen")

"""
Por supuesto que tenemos que tener buenas practicas, por ejemplo:
-usar nombres descriptivos que indiquen que hace la funcion
-incluir docstrings (documentacion), explica el proposito del parametro y valor de retorno
-mantener las funciones lo mas optimizado posible, es decir evitar sobrecargar de tareas
"""
print("\n")
# El docstring se coloca abajo de la declaracion de la funcion, ejemplo:
def suma(a, b): # Entonces, cuando nos posicionemos en el nombre de la funcion, podemos apreciar el docstring
    """Declaracion de paremetros de suma"""

# Podemos acceder a la descripcion de la funcion, en python, vemos un ejemplo:
print(suma.__doc__) # Si ejecutamos nos muestra el docstring

