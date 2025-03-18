print("Ingrese el monto que va a pagar por sus articulos: ")
monto = int(input())
montoconimpuesto = monto *1.1
montocondescuento= montoconimpuesto - montoconimpuesto *.05
montocondescuento = round(montocondescuento, 1)
print(f"El monto de sus articulos despues de aplicar el impuesto y el descuento queda en: {montocondescuento}")