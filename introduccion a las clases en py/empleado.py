empleados = []

class Empleado:
    def __init__(self, nombre, apellido, cedula, edad, posicion, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad
        self.posicion = posicion
        self.salario = salario

    def mostrar_datos(self):
        return print(f"Empleado: {self.nombre} {self.apellido}, Cedula: {self.cedula}, Edad: {self.edad}, Posicion: {self.posicion}, Salario: {self.salario}")

def solicitarInfo():

    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")
    cedula = input("Ingrese la cedula del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    posicion = input("Ingrese la posicion en la que el empleado trabaja: ")
    salario = input("Ingrese el salario del empleado: ")
    
    empleado = Empleado(nombre, apellido, cedula, edad, posicion, salario)
    return empleado

cant = int(input("Ingrese la cantidad de empleados que desea registrar: "))

for i in range(cant):
    print(f"Ingrese los datos del empleado {i+1}")
    empleado = solicitarInfo()
    empleados.append(empleado)

for empleado in empleados:
    empleado.mostrar_datos()


