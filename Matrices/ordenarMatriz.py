from random import randint
from tabulate import tabulate
from collections import Counter

contador = 0 #contador de comparaciones

#definiendo el tamaño de la matriz
filas = 10
columnas = 10

matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(randint(1,100))
    matriz.append(fila)
    
print("Matriz sin ordenar:")
for fila in matriz:
    print(fila)

print("\n")
print("Matriz ordenada:")

"""se crea una sola lista con todos los elementos de todas 
las filas de la matriz para poder ordenar facilmente"""

rawMatrix = [num for fila in matriz for num in fila] #usando list comprehension para tener una sola lista
rawMatrix.sort(key = None, reverse = False)

sortedMatrix = []
for i in range(0, len(rawMatrix), 10):
    fila = rawMatrix[i:i+10]
    sortedMatrix.append(fila)

for fila in sortedMatrix:
    print(fila)
print("\n")

#creando tabla de frecuencias
#se usa tabulate del modulo tabulate y counter del modulo collections
frecuencias = Counter(rawMatrix)

#preparando los datos para la tabla
tablaFrecuencias= [[numero, frecuencia] for numero, frecuencia in sorted(frecuencias.items())]
print("Tabla de frecuencias: ")
print(tabulate(tablaFrecuencias, headers=["Número", "Frecuencia"], tablefmt="fancy_grid"))
