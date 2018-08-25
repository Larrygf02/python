def valor_global():
	global variable_global
	variable_global= "Cambiar valor variable"#una variable local no puede modificar una variable global
def mostrar_global():
	print(variable_global)

variable_global = "Esto es una variable global"

valor_global()
mostrar_global()
print(variable_global)
