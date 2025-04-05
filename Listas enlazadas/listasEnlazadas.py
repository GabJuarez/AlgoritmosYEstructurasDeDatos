class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.enlace = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def insertar(self, nuevoDato):
        nuevoNodo = Nodo(nuevoDato)
        nuevoNodo.enlace = self.cabeza
        self.cabeza = nuevoNodo
    
    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.enlace
        print("None")  

# Uso de la lista enlazada
lista = ListaEnlazada()
 
print("ingresa datos y cuando querras parar ingresa espacio (" ")")
while True:
    print("ingresa dato")
    dato = input()
    if dato == " ":
        break
    else:
        lista.insertar(dato)

print ("La lista resultante es: ")
print(lista)

