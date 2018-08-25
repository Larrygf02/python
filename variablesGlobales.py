def palindromo():
	nuevo_valor = frase.replace(' ','') #variables locales
	return nuevo_valor == nuevo_valor[::-1]
frase = "anita lava la tina"
resultado = palindromo() #variables globales
print(resultado)
