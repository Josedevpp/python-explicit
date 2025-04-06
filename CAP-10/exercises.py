#1.Usa un bucle while par imprimir los valores de 1 al 10
print("\n")
numeros = 1
while numeros <=10:
    print(numeros)
    numeros += 1

#2.Usa un bucle for para recorrer la siguiente lista [10,20,30,40,50] e imprime cada uno de ellos
print("\n")
lista = [10,20,30,40,50]
for listas in lista:
    print(listas)

#3.Escribe un programa que usa un bucle while para sumar los numeros del 1 al 100 e imprime el resultado
print("\n")
numeros = 1
suma = 0
while numeros <= 100:
    suma += numeros
    numeros += 1
print(suma)


#4.Escribe un bucle for que imprima cada caracter de la cadena de texto "python"
print("\n")
name = "python"
for letra in name:
    print(letra)

#5.Usa el bucle while para encontrar el primer numero divisible por 7, entre 1 y 50
print("\n")
numero = 0
while numero <= 50:
    numero += 7
    if numero % 7 == 0:
        print(f"El numero {numero}, es divisible por 7")

#6.Usa un bucle for para recorrer el diccionario {"name": "josedevpp", "age": 24, "country": "mexico"} e imprime sus claves
print("\n")
diccionario = {"name": "josedevpp", "age": 24, "country": "mexico"}
for dic in diccionario:
    print(dic)

#7.Escribe un programa que use un bucle while para imprimir los numeros pares entre 1 y 20
print("\n")
valores = 1
while valores < 20:
    valores += 1
    if valores % 2 == 0:
        print(f"Los numeros pares son: {valores}")

#8.Usa un bucle for para la funcion range() para imprimir los numeros del 1 al 10 en orden inverso
print("\n")
valor = range(1,10)
for value in range(10,0,-1):
    print(value)

#9.Escribe un programa que use el bucle for para contar cuantas veces aparece el numero 10 en la lista [10,10,10,10,11,12,13,14]
print("\n")
list = [10,10,10,10,11,12,13,14]
counter = 0
for number in list:
    if number == 10:
        counter += 1
print(counter)

#10.Usa el bucle for para recorrer la lista de nombres y detener el bucle cuando encuentre el nombre josedevpp
print("\n")
lista_name = ["jose", "eduardo", "matias", "josedevpp"]
for name in lista_name:
    if name == "josedevpp":
        print(f"se encontro a: {name}")
        break
    print(name)