#no hay la necesidad de declarar una variable

c = 3
b = "hola"
d = 3.2

print(c)
print(b)
print(d)

#variables globales y variables locales

def variable():
	global c
	c = 5
	

variable()
print(c)


