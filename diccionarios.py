diccionario = { 'a': 55, 5: "esto es un string", 'a':23 } #las claves deben ser inmutables
#añadir un nuevo elemento
diccionario['c']='nuevo string'
diccionario['a']='nuevo string'
#sino se encuentra va a devolver un error
#valor = diccionario['z']
valor = diccionario.get('z', "No se encontro el dato")

#para eliminar un dato del diccionario
del diccionario[5]
print(valor)
print(diccionario)
