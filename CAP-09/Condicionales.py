# Condicionales
"""Las condicionales son estructuras de control que permiten ejecutar un bloque de código u otro dependiendo de si se cumple una condición o no. Existen tres tipos de condicionales en Python: if, elif y else.
if: Se utiliza para evaluar una condición. Si la condición es verdadera, se ejecuta el bloque de código correspondiente.
elif: Se utiliza para evaluar una segunda condición si la primera no se cumple. Puede haber múltiples elif en una estructura condicional.
else: Se utiliza para ejecutar un bloque de código si ninguna de las condiciones anteriores se cumple.
Las condicionales pueden manejar valores booleanos, que son valores que pueden ser True o False. También se pueden utilizar operadores de comparación, como ==, !=, <, >, <= y >=, para evaluar condiciones.
Además, se pueden combinar múltiples condiciones utilizando operadores lógicos como and, or y not.
Realizar operaciones aritmeticas, etc."""

# Ejemplo de condicionales
# if (si...)

edad = 18 # Variable que contiene la edad del usuario
if edad >= 18: # Condición que verifica si la edad es mayor o igual a 18
    # Si la condición es verdadera, se ejecuta el bloque de código correspondiente
    print("Eres mayor de edad.") # La condicion se cumplio, pero que pasa si no se cumple?

# else (si...sino...)
edad = 17
if edad >= 18:
    print("Eres mayor de edad.")
else:print("Eres menor de edad.") # La condicion no se cumplio, se ejecuta el bloque de codigo correspondiente al else.

"""Ahora supongamos que queremos evaluar multiples condiciones a ver cual de ellas se cumple. Para eso utilizamos el elif."""

# elif (si...o si...sino...)
calificaciones = 9
if calificaciones >= 9: # Evalua la primera condicion y si cumple imprime el mensaje correspondiente, sino pasa a la siguiente condicion.
    print("Excelente")
elif calificaciones >= 7: # En este caso como la primera fue True, no se sigue ejecutando las siguientes condiciones.
    print("Bueno")
elif calificaciones >= 5:
    print("Regular")
else:
    print("Reprobado") # else funciona como un bloque de codigo por defecto, si ninguna de las condiciones anteriores se cumple, se ejecuta este bloque.

"""Existen los condicionales anidados y estos ocurren cuando tenemos condicionales dentro de otras condicionales. Esto puede ser util para evaluar condiciones mas complejas."""
# Condicionales anidados

edad = 18
permiso = False
if edad >= 18: # Elavua la primera condicion, si cumple ejecuta el bloque de codigo correspondiente.
    print("Eres mayor de edad.")
    if permiso: # Si la primera condicion se cumple, se evalua la segunda condicion.
        print("Estas adentro.")
    else: # Si la segunda condicion no se cumple, se ejecuta el bloque de codigo correspondiente.
        print("No puedes entrar.")
else: # Si la primera condicion no se cumple, se ejecuta el bloque de codigo correspondiente.
    print("Regresa pronto.")

"""Como mencionamos, podemos hacer uso de operaciones de comparacion, si queremos comparar dos valores, ó incluso usar operadores logicos para evaluar condiciones mas complejas."""
# Ejemplos and

edad = 18
licencia = True
if edad >= 18 and licencia: # La condicion se cumple si ambas condiciones son verdaderas.
    print("Puedes conducir.")
else:
    print("No puedes conducir.")

# Ejemplos or
fin_de_semana = True
dia_feriado = True
if fin_de_semana or dia_feriado: # La condicion se cumple si al menos una de las condiciones es verdadera.
    print("Puedes descansar.")
else:
    print("A trabajar.")


# Por ultimo, escucharas el operador ternario, que es una forma compacta de escribir una condicional. Este operador se utiliza para asignar un valor a una variable dependiendo de si una condicion es verdadera o falsa.

# Operador ternario
# Sintaxis: variable = valor1 if condicion else valor2
edad = 14
pasaje = "Pagas $0.50" if edad >= 18 else "No pagas"
print(pasaje) # Si la condicion se cumple, se asigna el valor 25 a la variable pasaje, de lo contrario se asigna "No pagas".

"""Algunos consejos claves, los hemos mencionado a lo largo del curso, pero recuerda tener cuidado sobre la indentacion, no olvidar los : al final de la condicion, respeta la jerarquia ó el orden de las condiciones if-elif-else, y legibilidad, usa parentesis en condiciones complejas"""