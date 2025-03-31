numero = int(input("Ingrese un numero: "))
fact = 1

def factorial(numero, factorial):
    for i in range(1, numero+1):
        factorial = factorial *i 
    print(f"el factorial es {factorial}")

factorial(numero, fact)
        