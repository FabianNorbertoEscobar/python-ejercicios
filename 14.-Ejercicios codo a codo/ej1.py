# 1. Escribir una función que calcule el máximo común divisor entre dos números.

def gcd(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Ambos números deben ser positivos.")
    
    while b:
        a, b = b, a % b
    return a

try:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    
    resultado = gcd(num1, num2)
    print(f"El máximo común divisor entre {num1} y {num2} es {resultado}")
except ValueError as e:
    print(f"Error: {e}")
