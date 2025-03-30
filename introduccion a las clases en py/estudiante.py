class estudiante:
    def __init__(self, nombre, apellido, edad, carrera, cif):
        self.nombre = nombre
        self.apellido = apellido
        self.edad= edad
        self.carrera = carrera
        self.cif = cif

    def presentarse(self):
        return print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} y estudio {self.carrera}")
    

gabriel = estudiante('Gabriel', 'Juarez', 18, 'ingenieria en sistemas', 23021082)
gabriel.presentarse()