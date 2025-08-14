edad = float(input("Introduce tu edad: \n"))

if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad <= 60:
    print("Eres adulto")
else:
    print("Eres mayor")    