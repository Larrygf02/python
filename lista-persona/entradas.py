import persona
#la funcion input()
#sirve para capturar entrada de datos desde el teclado
respuesta = "S"
lista_persona = []
while(respuesta == "S"):
	print("Ingresa tu nombre")
	nom = input()
	while True:
	   try:
	       x = int(input("Ingrese una edad: "))
	       break
	   except ValueError:
	       print("Chucha pones letra donde debe ser numero")
	
	p = persona.Persona(nom,edad)
	lista_persona.append(p)
	print("Desea continuar (S/N)")
	respuesta = input()


for obj in lista_persona:
	print (obj.nombre,obj.edad)

#print("Tu nombre es : " ,p.nombre)
#print("tu edad es : ", p.edad)

