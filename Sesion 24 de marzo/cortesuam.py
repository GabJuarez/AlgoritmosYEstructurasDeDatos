c1=[]
c2=[]
c3=[]

print("Ingrese el numero de evaluaciones que vas a realizar en el primer corte: ")
long= int(input())
print("Ingrese sus notas del primer corte: ")
for i in range(long):
    print(f"Ingrese su nota {i+1}: ")
    nota = int(input())
    c1.append(nota)

prom1 = sum(c1)/len(c1)

print("Ingrese el numero de evaluaciones que vas a realizar en el segundo corte: ")
long= int(input())
print("Ingrese sus notas del segundo corte: ")
for i in range(long):
    print(f"Ingrese su nota {i+1}: ")
    nota = int(input())
    c2.append(nota)

prom2 = sum(c2)/len(c2)

print("Ingrese el numero de evaluaciones que vas a realizar en el tercer corte: ")
long= int(input())
print("Ingrese sus notas del tercer corte: ")
for i in range(long):
    print(f"Ingrese su nota {i+1}: ")
    nota = int(input())
    c3.append(nota)

prom3 = sum(c3)/len(c3)
nfinal= (prom1 + prom2 + prom3)/3

print(f"Nota final es: {nfinal} ")