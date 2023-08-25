# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase: - Un constructor, donde los datos pueden estar vacíos. - Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos. - mostrar(): Muestra los datos de la persona. - Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_edad(self, edad):
        if edad < 0:
            print("La edad no puede ser negativa.")
        else:
            self.edad = edad

    def get_edad(self):
        return self.edad

    def set_dni(self, dni):
        if len(dni) < 9:
            print("El DNI debe tener menos de 9 caracteres.")
        else:
            self.dni = dni

    def get_dni(self):
        return self.dni

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

    def es_mayor_de_edad(self):
        return self.edad >= 18

nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
dni = input("Ingrese el DNI: ")

persona = Persona()
persona.set_nombre(nombre)
persona.set_edad(edad)
persona.set_dni(dni)

persona.mostrar()
if persona.es_mayor_de_edad():
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")
