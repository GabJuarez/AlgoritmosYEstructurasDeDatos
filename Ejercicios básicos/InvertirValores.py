a = float(input("Ingrese el primer número: "))  
b = float(input("Ingrese el segundo número: "))  
print(f"Antes del intercambio: a = {a}, b = {b}")
a, b = b, a
print("Intercambiando...")
print(f"Después del intercambio: a = {a}, b = {b}")
