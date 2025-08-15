""" try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
    
try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")
    
try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción """

def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    elif edad > 150:
        raise ValueError("La edad no puede ser mayor a 150")
    elif edad < 18:
        raise Exception("Debes ser mayor de edad")
    return True

# Uso
try:
    validar_edad(5)
except ValueError as e:
    print(f"Error de valor: {e}")
except Exception as e:
    print(f"Error general: {e}")