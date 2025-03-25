c1=[]
c2=[]
c3=[]

print("Ingrese el número de evaluaciones que vas a realizar en el primer corte: ")
while True:
    try:
        long = int(input())
        if long > 0:  
            break  
        else:
            print("Ingrese un numero mayor que 0")
    except ValueError:
        print("Ingrese un numero valido")

print("Ingrese sus notas del primer corte: ")
for i in range(long):
    while True:
        try:
            print(f"Ingrese su nota {i+1}: ")
            nota = int(input())
            if 0 <= nota <= 100:
                c1.append(nota)
                break
            else:
                print("Valores entre 0 y 100")
        except ValueError:
            print("Ingrese un numero valido")

prom1 = sum(c1)/len(c1)

print("Ingrese el número de evaluaciones que vas a realizar en el segundo corte: ")
while True:
    try:
        long = int(input())
        if long > 0:  
            break  
        else:
            print("Ingrese un numero mayor que 0")
    except ValueError:
        print("Ingrese un numero valido")


print("Ingrese sus notas del segundo corte: ")
for i in range(long):
    while True:
        try:
            print(f"Ingrese su nota {i + 1}: ")
            nota = int(input())
            if 0 <= nota <= 100:
                c2.append(nota)
                break 
            else:
                print("Valores entre 0 y 100")
        except ValueError:
            print("Ingrese un número válido")

prom2 = sum(c2)/len(c2)

print("Ingrese el número de evaluaciones que vas a realizar en el tercer corte: ")
while True:
    try:
        long = int(input())
        if long > 0:  
            break  
        else:
            print("Ingrese un numero mayor que 0")
    except ValueError:
        print("Ingrese un numero valido")


print("Ingrese sus notas del tercer corte: ")
for i in range(long):
    while True:
        try:
           print(f"Ingrese su nota {i+1}: ")
           nota = int(input())
           if 0 <= nota <= 100:
               c3.append(nota)
               break
           else:
                print("Valores entre 0 y 100")
        except ValueError:
            print("Ingrese un número válido")
               

prom3 = sum(c3)/len(c3)
nfinal= round((prom1 + prom2 + prom3)/3)

print(f"Nota final es: {nfinal} ")