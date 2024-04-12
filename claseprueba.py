"""
Este documento posee diversos apuntes que, en su mayoría, 
no tienen concordancia, pero sin embargo son comprensibles. 
Es por esto que para ver y entender, hay que leer jajaja. 
En fin, son apuntes sobre clases.
"""


"""
    Métodos especiales en PYTHON
    Métodos especiales: Python proporciona una serie de métodos especiales
    (también conocidos como "métodos dunder" por empezar y terminar con doble guion bajo)
    que permiten definir comportamientos específicos para las instancias de una clase. 
    Algunos ejemplos comunes son __init__ para el constructor, 
    __str__ para representar el objeto como una cadena, __eq__ para comparar objetos, entre otros.
"""

# Definición de una clase simple
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Creación de objetos (instancias) de la clase Persona

#Para acceder a los atributos planteados no necesariamente tienen que estar preestablecidos, sin enmbargo, se debe respetar el orden en el que fueron declarados
persona1 = Persona(nombre=input("Digite su nombre: "), edad=int(input("Edad: ")))
#Tambíen se puede disponer de no sólo la terminal, sino del mismo cod para asignar atributos
persona2 = Persona("María", 25)

# Accediendo a los atributos y métodos de los objetos
#   Se puede acceder a un valor determinado:
print(persona1.nombre)  # Output: Juan
print(persona2.edad)    # Output: 25

persona1.saludar()  # Output: Hola, mi nombre es # y tengo # años.
persona2.saludar()  # Output: Hola, mi nombre es María y tengo 25 años.

#-----------------------------------    Más métodos de clases admitidos en PYTHON   ------------------------------------------#
#__init__: Método constructor, utilizado para inicializar una nueva instancia de la clase.
#python

class Persona:  # Se define una nueva clase llamada Persona.
    def __init__(self, nombre, edad):#Define el método especial __init__, que es el constructor de la clase. Toma tres parámetros: self, que hace referencia a la instancia de la clase, nombre y edad.
        """
        self.nombre = nombre y self.edad = edad: Asigna los valores 
        de nombre y edad a los atributos nombre y edad de la instancia 
        actual de la clase, respectivamente.
        """
        self.nombre = nombre
        self.edad = edad

persona = Persona("Juan", 30)
#----------------------------------------------------#
#__str__: Método que devuelve una representación de cadena legible de un objeto.
#python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self): #Define el método especial __str__, que devuelve una representación de cadena legible del objeto.
        #Retorna una cadena que contiene el nombre y la edad de la persona. Se usa el formato de f-strings para insertar los valores de nombre y edad.
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

persona = Persona("Juan", 30)
print(persona)  # Output: Persona(nombre=Juan, edad=30)
#----------------------------------------------------#
#__eq__: Método utilizado para comparar dos objetos y determinar si son iguales.
#python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, other):# Define el método especial __eq__ (Compara dos objetos de la clase persona)
        return self.nombre == other.nombre and self.edad == other.edad
"""
Retorna True si los nombres y las edades de ambas 
instancias son iguales, y False en caso contrario.
"""
persona1 = Persona("Juan", 30)
persona2 = Persona("Juan", 30)
print(persona1 == persona2)  # Output: True
#----------------------------------------------------#
#__len__: Método que devuelve la longitud de un objeto.
#python
class MiLista:
    def __init__(self, items):
        self.items = items

    def __len__(self):# Define el método especial __len__, que devuelve la longitud de la lista items.
        return len(self.items)#Retorna la longitud de la lista items utilizando la función len().

lista = MiLista([1, 2, 3, 4, 5])
print(len(lista))  # Output: 5








