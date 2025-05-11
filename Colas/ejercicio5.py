'''
Ejercicio 5.
En un centro de salud en León, los pacientes se registran para consultas médicas, pero se 
atienden según el orden de llegada. La consulta está basada en una cola, donde el paciente 
más reciente que llega espera en el final de la fila. Implementa el sistema de atención con 
las siguientes operaciones:
✔	enqueue: agregar un nuevo paciente.
✔	dequeue: atender al paciente en el frente de la cola.
✔	peek: visualizar quién es el siguiente paciente sin atenderlo.
'''

from collections import deque

class centroDeSalud:
    def __init__(self):
        self.colaPacientes = deque()

    def llegarPaciente(self, nombre):
        self.colaPacientes.append(nombre)
        print(f"El paciente {nombre} ya llegó y está esperando")
        print("\n")

    def atenderPaciente(self):
        if self.colaPacientes:
            paciente = self.colaPacientes.popleft()
            print(f"El paciente de nombre: {paciente} está siendo atendido")
        else:
            print(f"No hay pacientes en la cola de espera")
        print("\n")


    
    def visualizarSiguiente(self):
        if self.colaPacientes:
            paciente = self.colaPacientes[0]
            print(f"Próximo paciente:\n{paciente}")
            print("\n")
        else:
         print("No hay pacientes en la cola.")


    def mostrarCola(self):
        if self.colaPacientes:
            print("Pacientes que estan en espera: ")
            for i, paciente in enumerate(self.colaPacientes,1):
                print(f"{i}. {paciente}")
        else:
            print("Ahora mismo no hay pacientes esperando...")
        print("\n")
            
centroDeSalud = centroDeSalud()

while True:
    print("Opciones: ")
    print("1. LLegada de paciente")
    print("2. Atender paciente")
    print("3. Mostrar la cola de espera")
    print("4. Visualizar el siguiente paciente sin atenderlo")
    print("5. Salir")
    op = input("seleccione una opcion: ")
    
    
    if op == "1":
        nombre = input("Nombre del paciente: ")
        print("\n")
        centroDeSalud.llegarPaciente(nombre)
    elif op == "2":
        centroDeSalud.atenderPaciente()
    elif op == "3":
        centroDeSalud.mostrarCola()
    elif op == "4":
        centroDeSalud.visualizarSiguiente()
    elif op == "5":
        print("Saliendo")
        break
    else:
        print("la opcion seleccionada no fue valida")
