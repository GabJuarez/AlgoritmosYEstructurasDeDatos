from collections import deque

class clinica:
    def __init__(self):
        self.colaPacientes = deque()

    def llegarPaciente(self, nombre):
        self.colaPacientes.append(nombre)
        print(f"El paciente {nombre} ya llego")

    def atenderPaciente(self):
        if self.colaPacientes:
            paciente = self.colaPacientes.popleft()
            print(f"El paciente de nombre: {paciente} está siendo atendido")
        else:
            print(f"No hay pacientes en la cola de espera")

    def cancelarTurno(self):
        if self.colaPacientes:
            paciente = input("Ingrese el nombre del paciente que va a cancelar su turno: ")
            self.colaPacientes.remove()
            print(f"El paciente {paciente} cancelo su turno y fue removido de la lista de espera")
        else:
            print("No hay pacientes disponibles para cancelar su turno")        

    def mostrarCola(self):
        if self.colaPacientes:
            print("Clientes que estan en espera: ")
            for i, paciente in enumerate(self.colaPacientes,1):
                print(f"{i}. {paciente}")
            else:
                print("Ahora mismo no hay clientes esperando...")
            
clinica = clinica()

while True:
    print("Opciones: ")
    print("1. LLegada de paciente")
    print("2. Atender paciente")
    print("3. Mostrar la cola de espera")
    print("4. Cancelar turno de paciente")
    print("5. Salir")
    op = input("seleccione una opcion: ")
    
    if op == "1":
        nombre = input("Nombre del paciente: ")
        clinica.llegarPaciente(nombre)
    elif op == "2":
        clinica.atenderPaciente()
    elif op == "3":
        clinica.mostrarCola()
    elif op == "4":
        clinica.cancelarTurno()
    elif op == "5":
        print("Saliendo")
        break
    else:
        print("la opcion seleccionada no fue valida")
