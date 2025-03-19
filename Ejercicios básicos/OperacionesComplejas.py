import math
print("Ingrese un numero")
num = float(input())

if num < 0:
    print(f"{num**5}, No hay raiz de numero negativo ,{abs(num)}, Los logaritmos no pueden tener argumento negativo ")
else:
     print(f"{num**5},{math.sqrt(num)} ,{abs(num)}, {math.log(num)}")