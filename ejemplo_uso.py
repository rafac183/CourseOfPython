#!/usr/bin/env python3
"""
Ejemplo de Uso del Paquete de Operaciones y Utilidades
=====================================================

Este archivo demuestra cómo usar todas las funcionalidades disponibles
en el paquete de operaciones matemáticas y utilidades.

Autor: Tu Nombre
Fecha: 2024
"""

from paquete import operaciones, utilidades
from datetime import datetime


def ejemplo_operaciones_basicas():
    """Demuestra las operaciones matemáticas básicas."""
    utilidades.imprimir_mensaje("=== OPERACIONES MATEMÁTICAS BÁSICAS ===", "info")
    
    # Suma
    resultado = operaciones.suma(15, 25)
    utilidades.imprimir_mensaje(f"15 + 25 = {resultado}", "success")
    
    # Resta
    resultado = operaciones.resta(50, 20)
    utilidades.imprimir_mensaje(f"50 - 20 = {resultado}", "success")
    
    # Multiplicación
    resultado = operaciones.multiplicacion(7, 8)
    utilidades.imprimir_mensaje(f"7 × 8 = {resultado}", "success")
    
    # División
    resultado = operaciones.division(100, 4)
    utilidades.imprimir_mensaje(f"100 ÷ 4 = {resultado}", "success")


def ejemplo_operaciones_avanzadas():
    """Demuestra las operaciones matemáticas avanzadas."""
    utilidades.imprimir_mensaje("\n=== OPERACIONES MATEMÁTICAS AVANZADAS ===", "info")
    
    # Potencia
    resultado = operaciones.potencia(2, 10)
    utilidades.imprimir_mensaje(f"2^10 = {resultado}", "success")
    
    # Raíz cuadrada
    resultado = operaciones.raiz_cuadrada(144)
    utilidades.imprimir_mensaje(f"√144 = {resultado}", "success")
    
    # Factorial
    resultado = operaciones.factorial(5)
    utilidades.imprimir_mensaje(f"5! = {resultado}", "success")
    
    # Porcentaje
    resultado = operaciones.porcentaje(25, 100)
    utilidades.imprimir_mensaje(f"25 de 100 = {resultado}%", "success")


def ejemplo_utilidades_matematicas():
    """Demuestra las utilidades matemáticas."""
    utilidades.imprimir_mensaje("\n=== UTILIDADES MATEMÁTICAS ===", "info")
    
    # Verificar si es par
    numero = 42
    if operaciones.es_par(numero):
        utilidades.imprimir_mensaje(f"{numero} es un número par", "success")
    else:
        utilidades.imprimir_mensaje(f"{numero} es un número impar", "info")
    
    # Verificar si es primo
    numero = 17
    if operaciones.es_primo(numero):
        utilidades.imprimir_mensaje(f"{numero} es un número primo", "success")
    else:
        utilidades.imprimir_mensaje(f"{numero} no es un número primo", "info")
    
    # Redondear
    numero = 3.14159
    resultado = operaciones.redondear(numero, 2)
    utilidades.imprimir_mensaje(f"{numero} redondeado a 2 decimales = {resultado}", "success")


def ejemplo_utilidades_interaccion():
    """Demuestra las utilidades de interacción con el usuario."""
    utilidades.imprimir_mensaje("\n=== UTILIDADES DE INTERACCIÓN ===", "info")
    
    # Obtener nombre del usuario
    nombre = utilidades.obtener_nombre_usuario()
    utilidades.imprimir_mensaje(f"¡Hola, {nombre}!", "success")
    
    # Obtener número
    numero = utilidades.obtener_numero("Ingresa un número para calcular su factorial", "int")
    resultado = operaciones.factorial(numero)
    utilidades.imprimir_mensaje(f"El factorial de {numero} es {resultado}", "success")
    
    # Confirmar acción
    if utilidades.confirmar("¿Quieres continuar con más ejemplos?"):
        utilidades.imprimir_mensaje("¡Perfecto! Continuemos...", "success")
    else:
        utilidades.imprimir_mensaje("Entendido, terminando ejemplos.", "info")
        return


def ejemplo_utilidades_avanzadas():
    """Demuestra utilidades avanzadas."""
    utilidades.imprimir_mensaje("\n=== UTILIDADES AVANZADAS ===", "info")
    
    # Validar email
    email = "usuario@ejemplo.com"
    if utilidades.validar_email(email):
        utilidades.imprimir_mensaje(f"El email {email} es válido", "success")
    else:
        utilidades.imprimir_mensaje(f"El email {email} no es válido", "error")
    
    # Formatear fecha
    fecha_actual = datetime.now()
    fecha_formateada = utilidades.formatear_fecha(fecha_actual)
    utilidades.imprimir_mensaje(f"Fecha actual: {fecha_formateada}", "info")
    
    # Generar ID
    id_unico = utilidades.generar_id()
    utilidades.imprimir_mensaje(f"ID único generado: {id_unico}", "info")
    
    # Formatear número
    numero_grande = 1234567.89
    numero_formateado = utilidades.formatear_numero(numero_grande)
    utilidades.imprimir_mensaje(f"Número formateado: {numero_formateado}", "info")


def ejemplo_menu_interactivo():
    """Demuestra el uso de menús interactivos."""
    utilidades.imprimir_mensaje("\n=== MENÚ INTERACTIVO ===", "info")
    
    opciones = [
        "Calcular suma",
        "Calcular potencia",
        "Verificar si es primo",
        "Salir"
    ]
    
    while True:
        try:
            opcion = utilidades.obtener_opcion_menu(opciones, "Selecciona una operación")
            
            if opcion == 1:
                num1 = utilidades.obtener_numero("Primer número")
                num2 = utilidades.obtener_numero("Segundo número")
                resultado = operaciones.suma(num1, num2)
                utilidades.imprimir_mensaje(f"Resultado: {resultado}", "success")
                
            elif opcion == 2:
                base = utilidades.obtener_numero("Base")
                exponente = utilidades.obtener_numero("Exponente")
                resultado = operaciones.potencia(base, exponente)
                utilidades.imprimir_mensaje(f"Resultado: {resultado}", "success")
                
            elif opcion == 3:
                numero = utilidades.obtener_numero("Número a verificar", "int")
                if operaciones.es_primo(numero):
                    utilidades.imprimir_mensaje(f"{numero} es primo", "success")
                else:
                    utilidades.imprimir_mensaje(f"{numero} no es primo", "info")
                    
            elif opcion == 4:
                utilidades.imprimir_mensaje("¡Hasta luego!", "success")
                break
                
        except KeyboardInterrupt:
            utilidades.imprimir_mensaje("\nOperación cancelada por el usuario.", "warning")
            break


def ejemplo_barra_progreso():
    """Demuestra el uso de barras de progreso."""
    utilidades.imprimir_mensaje("\n=== BARRA DE PROGRESO ===", "info")
    
    utilidades.imprimir_mensaje("Simulando proceso...", "info")
    for i in range(10):
        utilidades.mostrar_progreso(i + 1, 10, "Procesando")
        utilidades.esperar(0.5, mostrar_progreso=False)
    
    utilidades.imprimir_mensaje("¡Proceso completado!", "success")


def main():
    """Función principal que ejecuta todos los ejemplos."""
    utilidades.imprimir_mensaje("🚀 EJEMPLOS DE USO DEL PAQUETE", "info")
    utilidades.imprimir_mensaje("=" * 50, "info")
    
    try:
        # Ejecutar ejemplos
        ejemplo_operaciones_basicas()
        utilidades.pausar()
        
        ejemplo_operaciones_avanzadas()
        utilidades.pausar()
        
        ejemplo_utilidades_matematicas()
        utilidades.pausar()
        
        ejemplo_utilidades_interaccion()
        utilidades.pausar()
        
        ejemplo_utilidades_avanzadas()
        utilidades.pausar()
        
        ejemplo_barra_progreso()
        utilidades.pausar()
        
        ejemplo_menu_interactivo()
        
        utilidades.imprimir_mensaje("\n🎉 ¡Todos los ejemplos completados exitosamente!", "success")
        
    except KeyboardInterrupt:
        utilidades.imprimir_mensaje("\n👋 Ejemplos interrumpidos por el usuario.", "warning")
    except Exception as e:
        utilidades.imprimir_mensaje(f"❌ Error durante la ejecución: {str(e)}", "error")


if __name__ == "__main__":
    main()
