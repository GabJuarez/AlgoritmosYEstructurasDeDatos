"""Restaurante Chino
Los platos se colocan en una mesa giratoria (circular). Los comensales toman 
comida siguiendo el orden de llegada, pero la bandeja tiene capacidad limitada: 
cuando se llena, los nuevos platos reemplazan a los más antiguos (como una cola circular)."""

class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = [None] * capacidad  # Arreglo para almacenar elementos
        self.frente = 0  # Índice del primer elemento
        self.final = -1   # Índice del último elemento
        self.tamano = 0   # Número actual de elementos

    def esta_llena(self):
        return self.tamano == self.capacidad

    def esta_vacia(self):
        return self.tamano == 0
    
    def redimensionar(self):
        nuevaCapacidad = self.capacidad *2
        nuevaCola =[None] * nuevaCapacidad

        for i in range (self.tamano):
            nuevaCola[i] = self.cola[(self.frente + i)%self.capacidad]
        
        self.cola = nuevaCola
        self.capacidad = nuevaCapacidad
        self.frente =0
        self.final = self.tamano -1
        print(f"Cola redimensionada a la siguiente capacidad: {self.capacidad} ")

    def enqueue(self, elemento):
        if self.esta_llena():
            self.redimensionar() #metodo nuevo para redimensionar en lugar de sobreescribir
        
        self.final = (self.final +1)% self.capacidad
        self.cola[self.final] = elemento
        self.tamano +=1
        print(f"➕ Añadido: {elemento}. Frente: {self.frente}, Final: {self.final}")


    def dequeue(self):
        """Elimina y retorna el elemento más antiguo."""
        if self.esta_vacia():
            print("❌ Cola vacía.")
            return None
        elemento = self.cola[self.frente]
        self.cola[self.frente] = None  # Opcional: Limpiar el espacio
        self.frente = (self.frente + 1) % self.capacidad
        self.tamano -= 1
        print(f"➖ Eliminado: {elemento}. Frente: {self.frente}, Final: {self.final}")
        return elemento

    def mostrar_cola(self):
        """Muestra la cola actual."""
        print(f"🎯 Cola: {self.cola}, Frente: {self.frente}, Final: {self.final}")

# Crear una cola circular para 3 platos
buffet = ColaCircular(3)

# Añadir platos
buffet.enqueue("Ensalada")   # ➕ Añadido: Ensalada. Frente: 0, Final: 0
buffet.enqueue("Pasta")      # ➕ Añadido: Pasta. Frente: 0, Final: 1
buffet.enqueue("Pollo")      # ➕ Añadido: Pollo. Frente: 0, Final: 2

buffet.mostrar_cola()        # 🎯 Cola: ['Ensalada', 'Pasta', 'Pollo'], Frente: 0, Final: 2

# Intentar añadir otro plato (sobrescribe el más antiguo)
buffet.enqueue("Postre")     # ⚠️ Cola llena. Sobrescribiendo elemento antiguo.
                             # ➕ Añadido: Postre. Frente: 1, Final: 0

buffet.mostrar_cola()        # 🎯 Cola: ['Postre', 'Pasta', 'Pollo'], Frente: 1, Final: 0

# Servir platos (FIFO)
buffet.dequeue()             # ➖ Eliminado: Pasta. Frente: 2, Final: 0
buffet.dequeue()             # ➖ Eliminado: Pollo. Frente: 0, Final: 0
buffet.dequeue()             # ➖ Eliminado: Postre. Frente: 1, Final: 0
buffet.dequeue()             # ❌ Cola vacía.
