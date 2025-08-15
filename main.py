#!/usr/bin/env python3
"""
Programa Principal - Calculadora Interactiva
============================================

Este es el archivo principal que demuestra el uso de los módulos
del paquete personalizado. Incluye operaciones matemáticas básicas
y utilidades de interacción con el usuario.

Autor: Tu Nombre
Fecha: 2024
Versión: 1.0
"""

import sys
from paquete import operaciones, utilidades


def mostrar_menu():
    """
    Muestra el menú principal de opciones disponibles.
    
    Returns:
        str: La opción seleccionada por el usuario
    """
    print("\n" + "="*50)
    print("        CALCULADORA INTERACTIVA")
    print("="*50)
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Calcular potencia")
    print("6. Salir")
    print("="*50)
    
    return input("Selecciona una opción (1-6): ")


def obtener_numeros():
    """
    Solicita al usuario que ingrese dos números.
    
    Returns:
        tuple: (numero1, numero2) o (None, None) si hay error
    """
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        return num1, num2
    except ValueError:
        utilidades.imprimir_mensaje("❌ Error: Por favor ingresa números válidos.")
        return None, None


def ejecutar_operacion(opcion, num1, num2):
    """
    Ejecuta la operación matemática seleccionada.
    
    Args:
        opcion (str): La opción del menú seleccionada
        num1 (float): Primer número
        num2 (float): Segundo número
        
    Returns:
        float: Resultado de la operación o None si hay error
    """
    try:
        if opcion == "1":
            resultado = operaciones.suma(num1, num2)
            operacion = "suma"
        elif opcion == "2":
            resultado = operaciones.resta(num1, num2)
            operacion = "resta"
        elif opcion == "3":
            resultado = operaciones.multiplicacion(num1, num2)
            operacion = "multiplicación"
        elif opcion == "4":
            if num2 == 0:
                utilidades.imprimir_mensaje("❌ Error: No se puede dividir por cero.")
                return None
            resultado = operaciones.division(num1, num2)
            operacion = "división"
        elif opcion == "5":
            resultado = operaciones.potencia(num1, num2)
            operacion = "potencia"
        else:
            utilidades.imprimir_mensaje("❌ Opción no válida.")
            return None
            
        utilidades.imprimir_mensaje(f"✅ El resultado de la {operacion} es: {resultado}")
        return resultado
        
    except Exception as e:
        utilidades.imprimir_mensaje(f"❌ Error durante la operación: {str(e)}")
        return None


def main():
    """
    Función principal del programa.
    Maneja el flujo principal de la aplicación.
    """
    # Mensaje de bienvenida
    utilidades.imprimir_mensaje("🚀 ¡Bienvenido a la Calculadora Interactiva!")
    
    # Obtener nombre del usuario
    nombre = utilidades.obtener_nombre_usuario()
    utilidades.imprimir_mensaje(f"👋 ¡Hola, {nombre}! Comencemos a calcular.")
    
    # Bucle principal del programa
    while True:
        try:
            # Mostrar menú y obtener opción
            opcion = mostrar_menu()
            
            # Verificar si el usuario quiere salir
            if opcion == "6":
                utilidades.imprimir_mensaje(f"👋 ¡Gracias por usar la calculadora, {nombre}! ¡Hasta luego!")
                break
            
            # Verificar si la opción es válida
            if opcion not in ["1", "2", "3", "4", "5"]:
                utilidades.imprimir_mensaje("❌ Opción no válida. Por favor selecciona 1-6.")
                continue
            
            # Obtener números del usuario
            num1, num2 = obtener_numeros()
            if num1 is None or num2 is None:
                continue
            
            # Ejecutar la operación seleccionada
            ejecutar_operacion(opcion, num1, num2)
            
            # Preguntar si quiere continuar
            continuar = input("\n¿Deseas realizar otra operación? (s/n): ").lower()
            if continuar not in ['s', 'si', 'sí', 'y', 'yes']:
                utilidades.imprimir_mensaje(f"👋 ¡Gracias por usar la calculadora, {nombre}! ¡Hasta luego!")
                break
                
        except KeyboardInterrupt:
            utilidades.imprimir_mensaje(f"\n👋 ¡Hasta luego, {nombre}! Programa interrumpido por el usuario.")
            break
        except Exception as e:
            utilidades.imprimir_mensaje(f"❌ Error inesperado: {str(e)}")
            utilidades.imprimir_mensaje("🔄 Reiniciando programa...")
            continue


if __name__ == "__main__":
    """
    Punto de entrada del programa.
    Solo se ejecuta si este archivo se ejecuta directamente.
    """
    try:
        main()
    except SystemExit:
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error crítico: {str(e)}")
        sys.exit(1)