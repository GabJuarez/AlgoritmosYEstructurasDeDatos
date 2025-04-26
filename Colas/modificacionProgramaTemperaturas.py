class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = [None] * capacidad  # Arreglo para almacenar las temperaturas
        self.frente = 0                 # Índice del elemento más antiguo
        self.final = -1                 # Índice del elemento más reciente
        self.contador = 0               # Número actual de elementos

    def esta_llena(self):
        return self.contador == self.capacidad

    def esta_vacia(self):
        return self.contador == 0

    def encolar(self, temperatura):
        """Añade una nueva temperatura, sobrescribe la más antigua si está llena."""
        if self.esta_llena():
            print(f"⚠️ Cola llena. Sobrescribiendo temperatura más antigua: {self.cola[self.frente]}")
            self.frente = (self.frente + 1) % self.capacidad
        else:
            self.contador += 1
        
        self.final = (self.final + 1) % self.capacidad
        self.cola[self.final] = temperatura
        print(f"Temperatura registrada: {temperatura}°C")

    def desencolar(self):
        """Elimina y retorna la temperatura más antigua."""
        if self.esta_vacia():
            print("❌ No hay temperaturas registradas.")
            return None
        
        temp = self.cola[self.frente]
        self.cola[self.frente] = None  # Opcional: Limpiar el espacio
        self.frente = (self.frente + 1) % self.capacidad
        self.contador -= 1
        print(f"Eliminada temperatura: {temp}°C")
        return temp

    def mostrar_temperaturas(self):
        """Muestra las temperaturas en orden cronológico (del más antiguo al más reciente)."""
        if self.esta_vacia():
            print("No hay temperaturas para mostrar.")
            return
        
        print("Registro de temperaturas (24h):")
        for i in range(self.contador):
            indice = (self.frente + i) % self.capacidad
            print(f"  - {self.cola[indice]}°C")

    def calcularPromedio(self):
        if self.esta_vacia():
            print("No hay temperaturas registradas para poder calcular la temperatura promedio.")
            return None
        
        suma = 0
        for i in range(self.contador):
            indice = (self.frente + i) % self.capacidad
            suma += self.cola[indice]
        
        promedio = suma / self.contador
        print(f"Promedio de temperaturas: {promedio:.2f}°C")
        return promedio
    
    def detectarPicos(self):
        if self.esta_vacia():
            print("No hay temperaturas registradas para poder detectar picos.")
            return
        
        print("Picos de temperatura (>30°C):")
        encontrado = False
        for i in range(self.contador):
            indice = (self.frente + i) % self.capacidad
            temperatura = self.cola[indice]
            if temperatura > 30:
                horaAprox = i + 1
                print(f"  - {temperatura}°C a la hora {horaAprox}")
                encontrado = True

        if not encontrado:
            print("No se detectaron picos.")

# Crear una cola circular para 24 temperaturas (1 por hora)
registro_temperaturas = ColaCircular(24)

# Simular lecturas cada hora (temperaturas entre 25°C y 35°C para simular picos)
for hora in range(1, 25):
    if hora == 12:  # Ejemplo de un pico a las 12:00
        registro_temperaturas.encolar(32)
    elif hora == 18:  # Otro pico a las 18:00
        registro_temperaturas.encolar(31)
    else:
        registro_temperaturas.encolar(hora)

registro_temperaturas.calcularPromedio()

registro_temperaturas.detectarPicos()
