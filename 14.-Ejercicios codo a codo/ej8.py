# 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase:  Un constructor.  Los setters y getters para el nuevo atributo.  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.  Además, la retirada de dinero sólo se podrá hacer si el titular es válido.  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

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

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def set_bonificacion(self, bonificacion):
        if bonificacion >= 0:
            self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    def es_titular_valido(self):
        return self.get_titular().es_mayor_de_edad() and self.get_titular().get_edad() < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)

    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print("Bonificación:", self.bonificacion, "%")

nombre_titular = input("Ingrese el nombre del titular: ")
edad_titular = int(input("Ingrese la edad del titular: "))
dni_titular = input("Ingrese el DNI del titular: ")
bonificacion = float(input("Ingrese la bonificación (%): "))

titular = Persona(nombre_titular, edad_titular, dni_titular)
cuenta_joven = CuentaJoven(titular, bonificacion=bonificacion)

print("Cuenta creada para:", cuenta_joven.get_titular().nombre)
cuenta_joven.ingresar(1000)
cuenta_joven.mostrar()

cantidad_retiro = float(input("Ingrese la cantidad a retirar: "))
cuenta_joven.retirar(cantidad_retiro)
cuenta_joven.mostrar()
