lista1 = ['raul','larriega',1993,23]
lista2 = [1,2,3,4,5,6]

print ("lista1[0]",lista1[0])
print ("lista2[1:5]",lista2[1:5])
#modificando un valor de la lista1
lista1[1] = "gallegos"
print (lista1)

#eliminar un valor de la lista1
del lista1[3]
print ("Eliminando el valor de la lista 23")
print (lista1)

#metodos de la lista 
print (len(lista2))
print ([1,2,3]+[4,5,6])
print (['Hola']*3)
print (3 in [1,2,3])

#indexing
print (lista2[-2])
print (lista2[3:])

#agregando elemento 
lista1.insert(1,"kelly")
print (lista1)

#eliminando elemento
lista1.pop(1)
print (lista1)