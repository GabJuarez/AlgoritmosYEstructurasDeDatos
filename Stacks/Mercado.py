'''
En un mercado de Chinandega, los sacos con productos se cargan en camiones uno encima de otro. 
Al llegar a destino, el primer saco que se descarga es el último que se cargó. Simula este proceso 
con una pila que permita apilar sacos (push), descargar uno (pop) y visualizar el que está encima (peek).
'''

class Mercado:
    
    def __init__(self):
        self.sacos = []  
    
    def pedir_sacos(self):
        seq = int(input('Cuantos sacos desea agregar: '))
        for i in range(seq):
            nombre = input(f'Ingrese el nombre del saco {i+1}: ')
            self.sacos.append(nombre)
        print("\n")
        print("Sacos apilados:", self.sacos)
    
    def descargar_saco(self):
        if not self.sacos:
            print("No hay sacos para descargar, la pila está vacia")
        else:
            saco_descargado = self.sacos.pop()  
            print(f"Saco descargado: {saco_descargado}")
        print("\n")

    def mostrar_pila(self):
        if not self.sacos:
            print("La pila está vacía")
        else:
            print("Sacos en la pila:")
            for i, saco in enumerate(self.sacos[::-1], start=1):  
                print(f"{i}. {saco}")
        print("\n")

    def peek(self):
        if not self.sacos:
            print("La pila está vacía, no hay sacos para mostrar.")
        else:
            print(f'El siguiente saco a descargar es: {self.sacos[-1]}')

#instancia
new_mercado = Mercado()
new_mercado.pedir_sacos()
new_mercado.descargar_saco()
new_mercado.mostrar_pila()
new_mercado.peek()