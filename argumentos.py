def funcion(*argumento):#el '*' permite trabajar con varios argumentos
	return argumento

resultado = funcion(10,20)
print(resultado)
resultado = funcion(10,20,30)
print(resultado)

def suma(*argumento):
	resultado = 0
	for valor in argumento:
		resultado = resultado + valor
	return resultado


resultado = suma(1,2)
print(resultado)
resultado = suma(1,2,3,4,5,6,7,8,9)
print(resultado)
 