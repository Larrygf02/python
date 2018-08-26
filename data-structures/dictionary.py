#Los diccionarias son un tipo de datos que estan indexados por claves
diccionario = {'nombre': 'Kelly', 'edad':25}
print(diccionario)
diccionario['apellido'] = 'Baldeon'
print(diccionario)

#Function items para obtener clave y valor del diccionario
for k, v in diccionario.items():
    print(k,v)

#Comprension de dictionarios
dicts = {x: x**2 for x in (1,2,3)}
print(dicts)