#inicializando lista
lista = []
for x in range(6):
    lista.append(x*2)

print(lista)

#Funcion map en python 3 retorna un objeto, es necesario convertirlo a lista
listac = list(map(lambda x:x*2, range(6)))
print(listac)

listac = [x*2 for x in range(6)]
print(str(listac)+ "\n")

#Generadorees 
def generador_pares():
    index = 1
    while True:
        yield index*2
        index += 1

for i in generador_pares():
    print(i)