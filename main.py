frutas = ["manzana", "banana", "naranja"]

""" print(frutas[0])
print(frutas[2])  
print("\n")
print(frutas[-1])
print(frutas[-2])
print(frutas[-3]) """

""" #Agregar a lista
frutas.append("pera")
print(frutas)

#Agregar a lista en lugar especifico
frutas.insert(1, "uva")
print(frutas)

#Eliminar de lista
frutas.remove("banana")
print(frutas)

#Eliminar de lista en lugar especifico
fruta_eliminada = frutas.pop(2)
print(frutas)
print(fruta_eliminada)

frutas.sort()
print(frutas)

frutas.reverse()
print(frutas) """

numeros = [1,2,3,4,5]
cuadrados = [x**2 for x in numeros if x % 3 == 0]
print(cuadrados)