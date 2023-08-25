# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números

def gcd(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Ambos números deben ser positivos.")
    
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Ambos números deben ser positivos.")

    return a * b // gcd(a, b)
    
'''
otra implementacion:

def lcm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Ambos números deben ser positivos.")

    max_val = max(a, b)
    min_val = min(a, b)
    
    multiple = max_val
    while multiple % min_val != 0:
        multiple += max_val
    
    return multiple
'''

print(f"El mínimo común múltiplo entre {num1} y {num2} es {resultado}")

try:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    
    resultado = lcm(num1, num2)
    print(f"El máximo común divisor entre {num1} y {num2} es {resultado}")
except ValueError as e:
    print(f"Error: {e}")
