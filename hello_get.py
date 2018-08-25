import cgi,cgitb

form = cgi.FieldStorage()

nombre = form.getValue("nombre")
apellido = form.getValue("apellido")

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
	print("<title>Capturando datos programa cgi</title>")
print("</head>")
print("<body>")
print("<h2>Hola %s %s</h2>" %(nombre,apellido))
print("</body>")
print("</html>")