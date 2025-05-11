'''
Ejercicio 4.
Un centro de distribución en el mercado Oriental recibe camiones para entregar productos como arroz, frijoles, 
aceite o gaseosas. Cada camión debe registrarse con: número de placa, nombre del conductor, empresa de origen 
y hora de llegada. Se debe implementar:
✔	La cola de espera de camiones,
✔	Visualización del orden actual,
✔	Salida del camión ya descargado.

'''

from collections import deque

camiones = deque()

def recibirCamiones():

    n = int(input("Ingrese el numero de camiones a recibir:"))

    for i in range (n):
        print(f"Camión #{i+1}")
        placa = input("Ingrese la placa del camión: ")
        nombre = input("Ingrese el nombre del conductor: ")
        origen = input("Ingrese la empresa de origen del camión: ")
        horaLlegada = input("Ingrese la hora de llegada del camión: ")

        camion = (placa, nombre, origen, horaLlegada)
        camiones.append(camion)
        print("\n")
        
def visualizarCola():
    if camiones:
        print("Cola de camiones en espera:")
        for i, camion in enumerate(camiones, start=1):
            print(f"{i}. Placa: {camion[0]} Nombre: {camion[1]} Empresa de origen: {camion[2]} Hora de llegada: {camion[3]}")
    else:
        print("No hay camiones en espera.")
    print("\n")

    
def salirCamiones():
     if camiones:
            camion = camiones.popleft()
            print(f"El camion de placa: {camion[0]}, conducido por: {camion[1]}, ha sido recibido y salió de la cola descargado")
            print("\n")
     else:
        print(f"No hay camiones esperando a ser recibidos")
        print("\n")


recibirCamiones()
visualizarCola()
salirCamiones()
visualizarCola()