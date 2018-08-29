
diccionario = {'nombre':'kelly','apellido': 'Baldeon','edad':24}
#El literal f te permite acceder a variables de python por medio del {}
for k,v in diccionario.items():
	print(f'{k} ==> {v}')

lenguage = 'python'
print(f'Aprendiendo {lenguage}.')
# !a aplica ASCII
print(f'Aprendiendo {lenguage !a}.')
# !s aplica str()
print(f'Aprendiendo {lenguage !s}.')
# !r aplica repr()
print(f'Aprendiendo {lenguage !r}.')