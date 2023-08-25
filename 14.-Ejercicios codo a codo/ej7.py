# 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase:  Un constructor, donde los datos pueden estar vacíos.  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.  mostrar(): Muestra los datos de la cuenta.  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Persona:
    def __init__(self, nombre, edad, dni):
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

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def set_titular(self, titular):
        self.titular = titular

    def get_titular(self):
        return self.titular

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.cantidad = cantidad

    def get_cantidad(self):
        return self.cantidad

    def mostrar(self):
        print("Titular:", self.titular.nombre)
        print("Edad:", self.titular.edad)
        print("DNI:", self.titular.dni)
        print("Cantidad en la cuenta:", self.cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad

nombre_titular = input("Ingrese el nombre del titular: ")
edad_titular = int(input("Ingrese la edad del titular: "))
dni_titular = input("Ingrese el DNI del titular: ")

titular = Persona(nombre_titular, edad_titular, dni_titular)
cuenta = Cuenta(titular)

print("Cuenta creada para:", cuenta.get_titular().nombre)
cuenta.ingresar(1000)
cuenta.mostrar()

cantidad_retiro = float(input("Ingrese la cantidad a retirar: "))
cuenta.retirar(cantidad_retiro)
cuenta.mostrar()
