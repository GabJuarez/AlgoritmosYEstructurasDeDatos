class perro:
    def __init__(self, nombre, raza, altura):
        self.nombre = nombre
        self.raza = raza
        self.altura = altura

    def comer(self):
            return print(f"{self.nombre} esta comiendo")
        
    def dormir(self):
            return print(f"{self.nombre} esta durmiendo")

        
mugi = perro('Mugi','Husky', 0.6)

print("Creando clase perro")
print(mugi.nombre, "," ,mugi.raza , "," , mugi.altura)
mugi.comer()
mugi.dormir()

print("-" * 10)

print("Creando clase humano")

class humano:
      def __init__(self, nombre, edad,):
            self.nombre = nombre
            self.edad = edad
        
      def presentarse(self):
            print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")

humano1 = humano('Gabriel', 18)
humano1.presentarse()
