persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

print(persona["nombre"])
print(persona["edad"])  
print(persona["ciudad"])

print(persona.keys())
print(persona.values())
print(persona.items())

persona.update({"profesion": "Ingeniero"})
print(persona)