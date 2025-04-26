from collections import deque

# Cola única para todos los cajeros
cola_cajeros = deque()

class Cajero:   # Representa un cajero individual
    def __init__(self, id_cajero):
        self.id = id_cajero
        self.clientes_atendidos = []  # Para rastrear los clientes atendidos por este cajero

    def atender_cliente(self, cliente):
        """Atiende a un cliente específico."""
        self.clientes_atendidos.append(cliente)
        print(f"🎉 Cajero {self.id} atendió a {cliente}.")

class Banco:    # Gestiona múltiples cajeros
    def __init__(self, num_cajeros):
        self.cajeros = [Cajero(i) for i in range(num_cajeros)]

    def llegar_cliente(self, nombre_cliente):
        """Agrega un cliente a la cola única."""
        cola_cajeros.append(nombre_cliente)
        print(f"🔄 {nombre_cliente} llegó a la cola. Total en cola: {len(cola_cajeros)}")

    def atender_clientes(self):
        """Reparte los clientes en la cola entre los cajeros usando slicing."""
        if not cola_cajeros:
            print("🕳️ No hay clientes en la cola.")
            return

        # Repartir clientes entre los cajeros
        for i, cajero in enumerate(self.cajeros):
            if cola_cajeros:
                cliente = cola_cajeros.popleft()  # Extrae el cliente de la cola
                cajero.atender_cliente(cliente)

# Ejemplo de uso
# Crear un banco con 3 cajeros
banco = Banco(num_cajeros=3)

# Llegan clientes
banco.llegar_cliente("Ana")
banco.llegar_cliente("Carlos")
banco.llegar_cliente("Marta")
banco.llegar_cliente("Luis")

# Atender un turno
print("\n--- Atendiendo clientes ---")
banco.atender_clientes()

# Llegan más clientes
banco.llegar_cliente("Sofía")
banco.llegar_cliente("Jorge")

# Atender otro turno
print("\n--- Atendiendo clientes ---")
banco.atender_clientes()
