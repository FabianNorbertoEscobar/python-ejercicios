# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

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

def palabra_mas_repetida(diccionario):
    palabra_max = None
    frecuencia_max = 0
    
    for palabra, frecuencia in diccionario.items():
        if frecuencia > frecuencia_max:
            palabra_max = palabra
            frecuencia_max = frecuencia
    
    return palabra_max, frecuencia_max

cadena = input("Ingrese una cadena de caracteres: ")
resultado_contar = contar_palabras(cadena)
palabra, frecuencia = palabra_mas_repetida(resultado_contar)

print("Frecuencia de palabras:")
for palabra, count in resultado_contar.items():
    print(f"'{palabra}': {count}")

print(f"La palabra más repetida es '{palabra}' con una frecuencia de {frecuencia}")
