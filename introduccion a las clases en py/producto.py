"""el codigo no es eficiente, solamente es una practica con las clases, 
listas y diccionarios"""
import json
productos = []

class  Producto:
    def __init__(self, code, nombre, cantidad, precio):
        self.code = code
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def mostrarInfo(self):
       return print(f"Id: {self.code}, nombre: {self.nombre}, cantidad: {self.cantidad}, precio: {self.precio}")

def solicitarInfo():
    code = int(input("ingrese el ID del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad en stock que hay del producto: "))
    precio = float(input("ingrese el precio del producto: "))
    producto =Producto(code, nombre, cantidad, precio)
    return producto

cant = int(input("Ingrese la cantidad de productos que desea regitrar: "))

for i in range(cant):
    print(f"Ingrese los datos del producto {i+1}: ")
    producto = solicitarInfo()
    productos.append(producto)
    print("\n")

diccionario = {}
for i, producto in enumerate(productos):
    diccionario[i] = producto

dic_atributos= {}
for key, producto in diccionario.items():
    dic_atributos[key] = producto.__dict__

with open("productos.json", "w") as archivoJson:
    json.dump(dic_atributos, archivoJson, indent = 4)

print("Los productos se guardaron de manera correcta en el json...")

