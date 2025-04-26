listaImpares = []

"""for i in range(1,10,2):
    listaImpares.append(i)"""
    
numero = 1
while len(listaImpares)<5:
    listaImpares.append(numero)
    numero +=2

for i in range (0,11):
    if i %2 == 0:
        listaImpares.insert(2*i,i)

del listaImpares[2]
listaImpares.pop()
listaImpares.remove(8)

"agregando varios 2 para ver como se comporta el metodo remove"
listaImpares.append(2)
listaImpares.insert(4 and 0 and 5, 2)
listaImpares.remove(2)

print(listaImpares)