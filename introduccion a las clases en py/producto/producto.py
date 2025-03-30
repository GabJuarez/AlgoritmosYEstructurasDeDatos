#practicando clases y gestionamiento de arhivos (json)
import json

productos = []
diccionario = {}

class Producto:
    def __init__(self, code, nombre, cantidad, precio):
        self.code = code
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def mostrarInfo(self):
        return f"Id: {self.code}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

def solicitarInfo():
    code = int(input("Ingrese el ID del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad en stock del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    return Producto(code, nombre, cantidad, precio)


try:
    with open("productos.json", "r") as archivoJson:
        dic_atributos = json.load(archivoJson)
except (FileNotFoundError, json.JSONDecodeError):
    dic_atributos = {}

cant = int(input("Ingrese la cantidad de productos que desea registrar: "))

for i in range(cant):
    print(f"Ingrese los datos del producto {i+1}: ")
    producto = solicitarInfo()
    productos.append(producto)
    print("\n")

"""para que cuando guardemos un producto nuevo este no repita las keys del json
desde el inicio hacemos que los nuevos productos se guarden tomando el valor correspondiente
de la key que sigue en el json, esto con start=len(dic_actributos)"""

for i, producto in enumerate(productos, start=len(dic_atributos)):
    dic_atributos[i] = producto.__dict__

# guardando
with open("productos.json", "w") as archivoJson:
    json.dump(dic_atributos, archivoJson, indent=4)

print("Los productos se guardaron correctamente en el json")
print("-" * 15)
print("mostrando todos los datos registrados:")

#leyendo los datos del archivo para printearlos
with open("productos.json", "r") as archivoJson:
    datos = json.load(archivoJson)

print(datos)
