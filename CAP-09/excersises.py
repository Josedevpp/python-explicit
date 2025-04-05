#1.Escribe un programa que verifique si un numero es positivo, negativo o cero.
""" numero = -2
if numero > 0:
    print("El numero es positivo.")
elif numero < 0:
    print("El numero es negativo.") 
else: 
    print("El numero es cero.)"""
#🆗

#2.Solicite al usuario que ingrese su altura y muestre indicando si la es altura mediam alta o baja.
# La altura media es de 1.70m para hombres y 1.60m para mujeres.
""" altura = float(input("Ingrese su altura: "))
if altura >= 1.70:
    print("Su altura es arriba de media")
    print("Eres alto")
elif altura < 1.70:
        print("Tu altura es menor que el promedio") """
#🆗

#3.Escribe un programa que verifique si una cadena de texto esta vacia y muestre un mensaje indicando si la cadena es vacia o no.
""" texto = input("Ingresa un texto: ")
if not texto:
     print("Esta vacia")
else:
     print("Tiene texto") """
#🆗

#4.Crea un programa que solicite dos numeros al usuario y compare cual es mayor o si son iguales y muestra resultado.
""" numero = int(input("Ingrese un numero: "))
numerodos = int(input("Ingrese otro numero: "))
if numero > numerodos:
     print("Numero uno es > a numero dos.")
elif numero < numerodos:
     print("Numero uno es < a numeros dos.")
elif numero == numerodos:
     print("Ambos numeros son iguales.")
else: 
     print("Valor invalido") """
#🆗
#5.Escribe un programa que verifique si un numero es divisible entre 3 y 5 y muestre un mensaje indicando si es divisible o no.
""" numero = int(input("Ingrese un numero: "))
if (numero % 3) == 0 and (numero % 5) == 0:
    print("El numero es divisible entre 3 y 5.")
else:
    print("El valor ingresado no es divisible.") """

#6.Solicite al usuario que verifique si un numero es par o impar y muestre un mensaje indicando si es par o impar.
""" numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("Es impar") """

#7.Escribe un programa que verifique si una persona es acta para votar. Para ser acta para votar, la persona debe tener al menos 18 años y ser ciudadana del pais.
""" edad = 17
pais = True
if edad >= 18 and pais == True:
    print("Eres mayor de edad y eres de El Salvador")
else:
    print("Eres de El Salvador, pero no puedes votar") """
#🆗  

#8.Crea un programa que solicite una contraseña al usuario y verifique si conincide con una contraseña almacenada. Si la contraseña es correcta, muestra un mensaje de bienvenida. Si no, muestra un mensaje de error.
""" contraseña = int(input("Ingrese contraseña: "))
default = 1234
if contraseña == default:
    print("Contraseña valida")
else:
    print("Contraseña invalida")
 """
#🆗
#9.Escribe un programa que verifique si un numero esta entre 5 y 10. Si el numero esta dentro de ese rango, muestra un mensaje indicando que el numero es valido. Si no, muestra un mensaje indicando que el numero es invalido.
""" numero = 13
if 10 <= numero <= 20:
    print("Numero entre el rango.")
else:
    print("Numero fuera de rango.") """

#10.Escribe un programa que simule un semaforo. Solicite al usuario que ingrese un color (rojo, amarillo o verde) y muestre un mensaje indicando si el semaforo esta en rojo (detenerse), amarillo (precaucion) o verde (puede avanzar). Si el color ingresado no es valido, muestra un mensaje de error.
""" color = input("Ingrese color: ")
if color == "rojo":
    print("Detente")
elif color == "verde":
    print("Avanza")
elif color == "amarillo":
    print("Precaución")
else:
    print("Color invalido") """
#🆗