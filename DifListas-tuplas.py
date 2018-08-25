tupla = (1,2,3,4,5,6,7,8,9)
lista = [1,2,3,4,5,6,7,8,9]


#la lista consume mas bytes que una tupla
print (tupla.__sizeof__())
print (lista.__sizeof__())
#no se puede alterar una tupla
#tupla[0] = 20 

diccionario = {tupla,"asignamos una tupla"}
print (diccionario)

#no podemos poner de clave una lista
diccionario2 = {lista,"asignamos una lista"}
print (diccionario2)