def saludo():
    print("Hola mundo")
    
def saludo2(nombre):
    print(f"Hola, {nombre}")
    
#name = input("Indique su nombre:\n")

cuadrado = lambda x: x**2
#print(cuadrado(5))

def area_rectangulo(base, altura):
    return base * altura

def suma(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(suma(1,5,8))
print(suma(5,2))