""" archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close() """

with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

""" archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close() """

""" archivo = open("datos.txt", "a")
archivo.write("Hola rafael!")
archivo.close() """