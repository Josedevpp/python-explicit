#¿Qué son las variables?
"""Las variables en python y en los lenguajes de programación en general son espacio de almacenamiento que se guardan en la memoria de forma temporal, es decir; ocupan recursos de la computadora para ejecutarlas en tiempo real, las variables pueden recibir nombres, y pueden contener valor o un valor vació, por supuesto que hay reglas generales para nombrar variables, veamos ejemplos:"""

#Variables permitidas

nombre = ""
edad = ""
peso = ""
cantidad = ""
genero = ""
'''Como podemos observar, las variables pueden recibir cualquier nombre, siempre y cuando no sean palabras reservadas por el lenguaje'''

#Variables no permitidas

#3.14323Variable = ""
#Alumno sexto = ""
#MIVARIABLE = ""
#MiVariable = ""
#mivariable = ""
#MI_VARIABLE = ""
#mi-varieble = ""

"""Como puedes observar las variables que contengan ,más de una palabra, python se queja de el espacio que continen, para brindar solución, tienes que hacer uso de _ conocida como (snake_case), y por recomendación siempre utiliza minusculas"""

#Solución

mi_nombre = ""
mi_edad = ""

"""Una de las curiosidades de python, es un lenguaje de tipado dinamico y tipado fuerte, es decir, las variables pueden modificarse en tiempo de ejecución y pueden cambiar de valor, veamos ejemplos"""

#age = 24
#print(age)

age = 20 
print(age)

#Entonces el tipo de dato, se determina en tiempo de ejecución y no tienes que declararlo explicitamente

name = "josedevpp"
print(type(name))

#name = 24
#print(type(name))

#Al momento de ejecutar, primero nos dice que es un str y luego un int, a esto se le conoce como tipado dinamico, existen los tipados estaticos, estos no se pueden cambiar en tiempos de ejecución, si tu asignas que es cadena de texto, entonces asi se quedara. Preo en lenguajes de programación como python o javascript son tipado dinamico.

#Tipado fuerte, es decir; python no realiza conversiones de tipos de manera automitica, veamos ejemplos:

#print(10 + "2") # si ejecutamos esto nos lanza error,
                # porque no puede sumar un int + 

"""Algo que si podriamos hacer, seria unar las f (formatter string literal) y esta se coloca antes de lo que vamos a imprimir, ejemplo:"""

print(f"Hola👋 {name} tienes {age} años de edad!")
#Esto devuelve su valor y lo "formatea" para mostrarlo
#Tambien podemos hacer operaciones dentro de estas
print(f"Hola👋 {name} dentro de 5 años tendras {age + 5}")

"""En python no existen las constantes, las constantes como en JavaScript son valores que no seran reasignado, no cambia, pero en python puedes simular o hacer su función, creado una clase, etc."""

#Nosotros podemos asignarle tipado al valor de una variable, por ejemplo:

mi_nombre_es_jose: bool = True
print(mi_nombre_es_jose)
#Ahora si cambiamos True por un valor entero, veamos si se sigue ejecutando
mi_nombre_es_jose = 24
print(mi_nombre_es_jose)
"""Por qué si estamos asignando a True como bool, nos sigue ejecutando True y 24, si 24 es int. Y esto se debe porque python en tiempo de ejecución no revisa los tipos, entonces el bool que colocamos, simplemente funciona como comentario"""
#Si nosotros queremos evaluar los tipos, en VScode podemos habilitar una opción para que el mismo editos nos revise la declaración que hicimos anteriormente

#Nos dirigimos a ajustes Ctrl + , y buscamos typecheck
#habilitamos el modo strict, de esta manera nos mostrara el editor un error porque estamos declarando que es tipo bool y luego que es un int, pero se seguira ejecutando, porque como digimos, python en tiempo de ejecución ignora y no evalua los tipados.

