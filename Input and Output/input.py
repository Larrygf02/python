curso = 'python'; version = 3.7
#No funciona en python 2
resultado = f'Estoy estudiando el curso de {curso} version {version}'
print(resultado)
decimal = 3.57655
print('{:1.1%}'.format(decimal))

string = 'Hola , mundo'
print(str(string))
x = 5 * 3.5
"""
__str__ el objetivo es ser legible
__repr__ el objetivo es ser inequivoco
"""
print(repr(x))

class X(object):
	def __repr__(object): return 'foo'

#Ambos van a devolver el mismo resultado
print(str(X())) 

print(repr(X()))

class Y(object):
	def __str__(object): return 'foo'

print(str(Y())) #return foo

print(repr(Y())) #return object y
