#Operadores aritmeticos, logicos y comparativos

#Dentro de los lenguajes de programación, existen operaciones matematicas, situaciones de comparación y logica, que utilizaremos para solucionar problemas

"""Todos los lenguajes poseen estas 3 operaciones, porque son fundamentales y esenciales para resolver problemas, para sumar, dividir, comparar si un numero es mayor que otro, hacer uso de logica AND, OR Y NOT( Y, O, NO)"""

#Veamos los aritmeticos basicos
#Suma (Adición)
#Resta (Sustracción)
#Multiplicación (Producto)
#División (Sin residuo)
#División Entera (Aproximación)
#Modulo (Residuo)
#Potencia (Multiplica un numero n veces)

#Veamos sus ejemplos:
print('Adición:', 5 + 9)
print('Suatracción:', 5 - 4)
print('Producto:', 8 * 7)
print('Residuo:', 8 / 2)
print('Modulo:', 3 % 2)
print('Potencia:', 2 **3)

#Ejemplos reales

a = int (input('Ingrese un numero:'))
b = int (input('Ingrese otro numero:'))
suma = a + b
resta = a - b,
multi = a * b,
divi = a / b,
modul = a % b,  
potenciado = a ** b,
seleccionar = suma, resta, multi, divi, modul, potenciado
print("El resultado solicitado es:", seleccionar)

#Operadores de comparación
#Mayor que
#Menor que
#Mayor o igual que
#Menor o igual que 
#Igual que
#Diferente que

print(5 > 3)
print(5 < 6)
print(5 >= 5)
print(5 <= 5)
print(9 == 9)
print(8 != 9)

#Ejemplos reales

print(len('mango') > len('uva'))
print(len('cereza') < len('manzana'))
print(len('ocho') >= len('pala'))
print(len('uva') <= len('ola'))
print(len('peso') == len('casa'))
print(len('casa') != len('arbol'))

#Operadores logicos

# AND, retorna True si ambos elementos son True
# OR, Retorna True si uno de los dos elementos es True o ambos son True
# NOT, revierte el resultado, de True a False y viceversa
#XOR, devuelve True si al menos uno de los dos es True

#Veamos ejemplos
#AND
print(3 > 2 and 4 > 3)
#OR
print(4 >= 4 or 7 > 5)
#NOT
print(not True)
#XOR
print(5 < 5 | 8 > 5)
print(5 < 5 ^ 8 > 5)

#Simbologia discreta de booleanos

# AND --> ^
# NOT --> ¬ Ó ~
# OR --> v
# XOR --> ^ Ó ! =
 
# importante: si conoces las tablas de verdad, sabras que existen las implición y la bicondicional, no tiene aplicación directa con python, pero si se puede expresar con convinaciones de NOT, OR Y ==.



