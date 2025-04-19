# Classes

"""Las classes en python son como plantillas para crear objetos, un ejemplo sencillo de ver, seria imaginarte que quieres crear un juego y necesitas crear muchos personajes similares, pero con atributos diferentes o imaginate que quieres crear una casa, pues los planos serian serian la clase (una plantilla) y cada casa creada es tu objeto (una instancia de la clase)."""

# Veamos la sintaxis de una clase:

# --> Definir una clase
# --> El constructor: se ejecuta cuando creas un nuevo objeto de la clase
# --> Atributos publicos y privados: características del objeto
# --> Métodos: acciones que puede realizar el objeto
# --> Herencia: crear una nueva clase a partir de otra
# --> Encapsulamiento: ocultar detalles internos de la clase
# --> Polimorfismo: usar el mismo método en diferentes clases

# Definimos la clase
class Personaje:
    # Constructor: se ejecuta al crear un nuevo personaje
    def __init__(self, nombre, salud, fuerza):
        # Atributos: características del personaje
        self.nombre = nombre    # Guardamos el nombre que recibimos
        self.salud = salud      # Guardamos la salud que recibimos
        self.fuerza = fuerza    # Guardamos la fuerza que recibimos
        self.nivel = 1          # Atributo con valor predeterminado
        
    # Método: acción que puede realizar el personaje
    def atacar(self, enemigo):
        # 'self' es el personaje que ataca
        # 'enemigo' es otro personaje que recibe el ataque
        daño = self.fuerza * self.nivel  # Calculamos el daño
        enemigo.salud -= daño            # Restamos el daño a la salud del enemigo
        return f"{self.nombre} atacó a {enemigo.nombre} causando {daño} puntos de daño"
    
    # Otro método para subir de nivel
    def subir_nivel(self):
        self.nivel += 1
        self.fuerza += 5
        self.salud += 20
        return f"{self.nombre} subió al nivel {self.nivel}!"

# Creamos dos personajes (objetos) basados en la clase Personaje
mario = Personaje("Mario", 100, 15)    # nombre="Mario", salud=100, fuerza=15
bowser = Personaje("Bowser", 200, 10)  # nombre="Bowser", salud=200, fuerza=10

# Usamos el método atacar
print(mario.atacar(bowser))  
# Imprime: "Mario atacó a Bowser causando 15 puntos de daño"

# Subimos de nivel a Mario
print(mario.subir_nivel())  
# Imprime: "Mario subió al nivel 2!"

# Ahora Mario es más fuerte
print(mario.atacar(bowser))  
# Imprime: "Mario atacó a Bowser causando 20 puntos de daño"

# Verificamos la salud de Bowser después de dos ataques
print(f"Salud de {bowser.nombre}: {bowser.salud}")  
# Imprime: "Salud de Bowser: 165"


""""En pocas palabras las classes nos permiten crear objetos que tienen atributos y métodos, lo que nos permite organizar mejor nuestro código y hacerlo más fácil de entender y mantener. En este caso, hemos creado una clase Personaje que tiene atributos como nombre, salud y fuerza, y métodos como atacar y subir_nivel. Luego hemos creado dos personajes (Mario y Bowser) basados en esta clase y hemos utilizado sus métodos para interactuar entre ellos, veamos otro ejemplo sencillo."""

class Stark:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    # Atributos de la clase Lannister

my_lord = Stark("Jon Snow", "Bastard")
print(my_lord.name) # Jon Snow
print(my_lord.surname) # Bastard
# Tambien podemos representar lso atributos como un solo atributo, en este caso el nombre completo
class Stark:
    def __init__(self, name, surname):
        self.fullname = f"{name} {surname}"
    # Atributos de la clase Lannister
my_lord = Stark("Jon Snow", "(Bastard)")
print(my_lord.fullname) # Jon Snow
# En este caso, hemos creado una clase Stark que tiene un atributo fullname que combina el nombre y el apellido. Al crear un objeto de la clase Stark, podemos acceder al nombre completo directamente.

# Como mencionamos las propiedades tambien pueden ser privadas, significa que no podemos modificar su valor directamente desde fuera de la clase, para ello usamos el prefijo __ (doble guion bajo) para indicar que es privado. Por ejemplo:

class Lannister:
    def __init__(self, name, apellido):
        self.name = name # Atributo público
        self.__apellido = apellido #Atributo privado
    def get_surname(self):
        return self.__apellido
    # Método para acceder al apellido privado
my_queen = Lannister("Cersei", "Lannister")
print(my_queen.name) # Cersei
print(my_queen.get_surname()) # Lannister
# En este caso, el atributo __apellido es privado y no se puede acceder directamente desde fuera de la clase. Para acceder a él, hemos creado un método get_surname que devuelve el apellido.
# Esto es útil para proteger los datos y evitar que se modifiquen accidentalmente desde fuera de la clase.

""" 
Clase: Plantilla o plano (ej: Personaje)
Objeto: Instancia creada a partir de una clase (ej: mario, bowser)
Constructor: Método __init__ que se ejecuta al crear un objeto
Atributos: Características de los objetos (nombre, salud, fuerza)
Métodos: Acciones que pueden realizar los objetos (atacar, subir_nivel)
self: Referencia al objeto actual, siempre es el primer parámetro de cada método
Parámetros: Valores que pasas a los métodos, igual que en las funciones normales 
"""