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

    def cantvocales(self):
        codigos_vocales = [
            65, 69, 73, 79, 85,         # A, E, I, O, U
            97, 101, 105, 111, 117,     # a, e, i, o, u
            193, 201, 205, 211, 218,    # Á, É, Í, Ó, Ú
            225, 233, 237, 243, 250,    # á, é, í, ó, ú
            220, 252                    # Ü, ü
        ]
        actual = self.cabeza
        contador = 0
        lista_vocales = []

        while actual is not None:
            if ord(actual.dato) in codigos_vocales:
                contador += 1
                lista_vocales.append(actual.dato)
            actual = actual.enlace

        print(f"Las vocales de tu nombre son: {lista_vocales}")
        print(f"En tu nombre hay {contador} vocales")


# Uso de la lista enlazada
lista = ListaEnlazada()

print("Ingrese su nombre letra por letra, para terminar ingrese espacio (' ')")
while True:
    print("Letra:")
    dato = input()
    if dato == " ":
        break
    else:
        lista.insertar(dato)

lista.cantvocales()
