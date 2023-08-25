# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.

# implementacion iterativa

def get_int_iterative():
    while True:
        try:
            valor = int(input("Ingrese un valor entero: "))
            return valor
        except ValueError:
            print("Valor inválido. Intente nuevamente.")

entero = get_int_iterative()
print("El valor entero ingresado es:", entero)

# implementacion recursiva

def get_int_recursive():
    try:
        valor = int(input("Ingrese un valor entero: "))
        return valor
    except ValueError:
        print("Valor inválido. Intente nuevamente.")
        return get_int_recursive()

entero = get_int_recursive()
print("El valor entero ingresado es:", entero)
