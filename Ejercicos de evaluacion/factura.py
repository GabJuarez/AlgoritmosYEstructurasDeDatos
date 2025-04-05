import datetime

class Factura:
    idsUsados = set()

    def __init__(self, id, cliente, items: dict[str, dict[str, float]], pymt):
        self.id = id
        self.fecha = datetime.datetime.now()
        self.cliente = cliente
        self.items = items
        self.pymt = pymt
        self._subtotal = 0
        self._total = 0

#region access modifiers
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        if not isinstance(valor, int):  
            raise ValueError("El id debe ser un número entero")
        if valor <= 0:  
         raise ValueError("Ingrese un id positivo")
        if valor in Factura.idsUsados:
            raise ValueError("El id no puede ser repetido")
        self._id = valor
        Factura.idsUsados.add(valor)

    @property
    def fecha(self):
        return self._fecha.strftime("%d/%m/%Y %H:%M:%S")
    
    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor

    @property
    def cliente(self):
        return self._cliente
    
    @cliente.setter
    def cliente(self, valor):
        if not valor:
            raise ValueError("Ingrese un cliente valido")
        self._cliente = valor

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if not isinstance(value, dict):  # validando de que sea un diccionario
            raise ValueError("Los items deben ser un diccionario. Ejemplo de formato correcto: {'item1': {'precio': 10.0, 'cantidad': 2}}")
    
    # cada valor del diccionario debe tener las claves 'precio' y 'cantidad'
        for key, val in value.items():
            if not isinstance(val, dict):
                raise ValueError(f"El valor de {key} debe ser un diccionario. Ejemplo: {'precio': 10.0, 'cantidad': 2}")
            if 'precio' not in val or 'cantidad' not in val:
                raise ValueError(f"Cada item debe tener las claves 'precio' y 'cantidad' en {key}. Ejemplo: {'precio': 10.0, 'cantidad': 2}")
            if not isinstance(val['precio'], (int, float)) or not isinstance(val['cantidad'], int):
                raise ValueError(f"El precio debe ser un número y la cantidad debe ser un entero en {key}. Ejemplo: {'precio': 10.0, 'cantidad': 2}")
    
        self._items = value  
    
    @property
    def pymt(self):
        return self._pymt
    
    @pymt.setter
    def pymt(self, valor):
        if valor not in ['efectivo', 'tarjeta', 'transferencia']:
            raise ValueError("El metodo de pago debe ser efectivo, tarjeta o transferencia")
        self._pymt = valor  

    @property
    def subtotal(self):
        return self._subtotal

    @property
    def total(self):
        return self._total
    

#end region

#region methods
    def pedirDatos(self):
        cant = int(input("Ingrese el numero de facturas que quiere registrar: "))

        for i in range(cant):
            print(f"---------Factura {i+1}---------")
            print("Ingrese el nombre del cliente: ")
            self.cliente = input()
            numItems = int(input("Ingrese el numero de items comprados: "))

            itemsFactura = {}

            for j in range(numItems):
                nombre = input(f"Ingrese el nombre del item: {j+1}")
                precio = float(input(f"Ingrese el precio de {nombre}"))
                cantidad = int(input(f"Ingrese la cantidad de {nombre}"))
                itemsFactura[nombre] = {'precio': precio, 'cantidad': cantidad}
                self.items = itemsFactura
                
            print("--------------------------------")

    def actualizarSuntotalYTotal(self):
        #calcula el subtotal y el total(con un impuesto del 15%)
        self._subtotal = sum(val['precio']* val['cantidad'] for val in self.items.values())
        self._total = self._subtotal*1.15
#end region