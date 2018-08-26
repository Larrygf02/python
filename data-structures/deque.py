from collections import deque
#Usar una lista como cola (Primero en entrar, primero en salir)
lista = ['hola',1,'kelly',2]
cola = deque(lista)
cola.append('Raul')
print(cola)
#Funcion popleft retorna el primero de la lista y lo elimna
print(cola.popleft())
print(cola)
