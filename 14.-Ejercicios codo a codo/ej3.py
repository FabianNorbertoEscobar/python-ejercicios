# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia

cadena = input("Ingrese una cadena de caracteres: ")
resultado = contar_palabras(cadena)

print("Frecuencia de palabras:")
for palabra, count in resultado.items():
    print(f"'{palabra}': {count}")
