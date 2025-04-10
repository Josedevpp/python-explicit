#1.Crea una funcion llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, {nombre}". Si no se proporciona ningun nombre que imprima "Hola, Desconocido"
""" def personalized_greeting(nombre= "Desconocido"):
    print(f"Hola, {nombre}")

personalized_greeting("Josedevpp") """

#2.Escribe una funcion llamada "multiply", que reciba dos numeros como argumento y retorne la multiplicacion
""" def multiply(num1, num2):
    print(num1 * num2)
multiply(3,3) """

#3.Crea un funcion llamada "is_even" que reciba un numero entero como argumento y retorne True si es par y False si es impar
""" def is_even(num1):
    if num1 % 2 == 0:
        print(True)
    else:
        print(False)
is_even(1) """

#4.Escribe un funcion llamada "convert_to_uppercase", que reciba una cadena de texto y la retorne en mayusculas
""" def convert_uppercase(texto):
    print(texto.upper())

convert_uppercase("josedevpp") """

#5.Crea un funcion llamada "arbitrary_sum" que reciba un numero arbitrario de numeros como argumento y retorne la suma de todos
""" def arbitrary_sum(*numeros):
    print(sum(numeros))
arbitrary_sum(2,2,2,2,2) """

#6.Crea una funcion llamada "generate_full_greeting" que reciba dos argumentos. nombre y apellido y retorne un saludo "Hola, {nombre}, {apellido}"
""" def generate_full_greeting(nombre, apellido):
    print(f"Hola, {nombre} {apellido}")
generate_full_greeting("Jose", "Amaya") """

#7.Crea una funcion llamada "power" que reciba dos numeros, base y exponente y retorne su resultado exponencial
""" def power(base, exponente):
    print(base**exponente)
power(4,2) """

#8.Escribe una funcion llamada "calculate_average" que reciba tres numeros y retorne su promedio
""" def calculate_average(a,b,c):
    print((a+b+c)/3)
calculate_average(10,10,10)
 """

#9.Crea un funcion llamada "count_characters" que reciba una cadena de texto y retorne la cantidad de caracteres que contiene
""" def count_characters(caracteres):
    print(len(caracteres))

count_characters("Pedro") """

#10.Escribe una funcion llamada "display_messages" que reciba un numero indefinido de cadenas de texto y las imprima en mayusculas, una por una 
