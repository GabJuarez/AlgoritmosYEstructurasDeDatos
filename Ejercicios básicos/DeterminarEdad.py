from datetime import datetime

print("Escribe tu año de nacimiento: ")
nacimiento = int(input())
actual = datetime.now().year
edad = actual - nacimiento
print(f"Usted tiene {edad} años")