from collections import deque

class Banco:
    def __init__(self):
        self.cola_clientes = deque()

    def llegar_cliente(self, nombre):
        self.cola_clientes.append(nombre)
        print(f"📥 Cliente {nombre} llegó y fue agregado a la cola.")

    def atender_cliente(self):
        if self.cola_clientes:
            cliente = self.cola_clientes.popleft()
            print(f"✅ Cliente {cliente} está siendo atendido.")
        else:
            print("⚠️ No hay clientes en la cola para atender.")

    def mostrar_cola(self):
        if self.cola_clientes:
            print("🧾 Clientes en espera:")
            for i, cliente in enumerate(self.cola_clientes, 1):
                print(f"{i}. {cliente}")
        else:
            print("🟢 No hay clientes en la cola.")

# Programa principal
banco = Banco()

while True:
    print("\nMenú:")
    print("1. Llegada de cliente")
    print("2. Atender cliente")
    print("3. Mostrar cola")
    print("4. Salir")
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        nombre = input("Nombre del cliente: ")
        banco.llegar_cliente(nombre)
    elif opcion == "2":
        banco.atender_cliente()
    elif opcion == "3":
        banco.mostrar_cola()
    elif opcion == "4":
        print("👋 Cerrando el sistema.")
        break
    else:
        print("❌ Opción no válida. Intentá de nuevo.")
