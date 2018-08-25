def suma(valor_uno,valor_dos, valor_tres):
	return valor_uno+valor_dos+valor_tres
resultado = suma(1,2,3)
print(resultado)

def saludo(nombre):
  print("hola "+ nombre)

saludo("kelly")  

def multiple_valores():
	return "Hola", 1, True,  10.2
resultado = multiple_valores()

string, entero, bol, floa = multiple_valores()

print(string)
print(entero)
print(bol)
print(floa)
print(resultado)

mv = multiple_valores
resultado = mv()
print(resultado)