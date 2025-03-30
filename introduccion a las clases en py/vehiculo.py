from datetime import datetime
actual = datetime.now().year

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
    
    """"practicando los modificadores de acceso, tambien
    se pueden hacer funciones simples si los atributos no
    necesitan validaciones o logica extra pero siempre es
    buena practica usar el property"""

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self,nuevaMarca):
        if isinstance(nuevaMarca, str) and nuevaMarca:
            self.__marca = nuevaMarca
        else:
            print("marca invalida")

    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, nuevoModelo):
        if isinstance(nuevoModelo, str) and nuevoModelo:
            self.__modelo = nuevoModelo
        else: 
            print("Modelo invalido")
        
    @property
    def año(self):
        return self.__año
    
    @año.setter
    def año(self, nuevoAño):
        if 1900<= nuevoAño <=actual:
            self.__año = nuevoAño
        else:
            print("Ingrese un año valido")
    
    def mostrarInfo(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")    
        print(f"Año: {self.año}")

#instancias para ejemplos
vehiculo1 = Vehiculo("toyota", "corolla", 2020)
vehiculo1.mostrarInfo()

vehiculo2 = Vehiculo("honda", "civic", 2022)
vehiculo2.mostrarInfo()
        

#creando subclase
class moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindros):
        super().__init__(marca, modelo, año)
        self.__cilindros = cilindros
    
    @property
    def cilindros(self):
        return self.__cilindros
    
    @cilindros.setter
    def cilindros(self, nuevoCilindros):
        if isinstance(nuevoCilindros, int) and nuevoCilindros > 0:
            self.__cilindros = nuevoCilindros
        else:
            print("Ingrese un dato valido")
    
    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Cilindros: {self.__cilindros}cc")

moto1 = moto("Yamaha", "R1", 2020, 998)
moto1.mostrarInfo()





    
