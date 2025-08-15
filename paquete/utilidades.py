"""
Módulo de Utilidades
===================

Este módulo contiene funciones de utilidad para la interacción con el usuario,
formateo de texto, validación de entrada y otras operaciones comunes.

Funciones disponibles:
- imprimir_mensaje(mensaje): Imprime un mensaje formateado
- obtener_nombre_usuario(): Solicita y valida el nombre del usuario
- obtener_numero(mensaje): Solicita y valida un número
- limpiar_pantalla(): Limpia la pantalla de la consola
- pausar(): Pausa la ejecución hasta que el usuario presione Enter
- validar_email(email): Valida formato de email
- formatear_fecha(fecha): Formatea una fecha
- generar_id(): Genera un ID único

Autor: Tu Nombre
Fecha: 2024
Versión: 1.0
"""

import os
import sys
import re
import time
import uuid
from datetime import datetime
from typing import Optional, Union


def imprimir_mensaje(mensaje: str, tipo: str = "info") -> None:
    """
    Imprime un mensaje formateado con diferentes estilos según el tipo.
    
    Args:
        mensaje: El mensaje a imprimir
        tipo: Tipo de mensaje ('info', 'error', 'success', 'warning')
        
    Returns:
        None
    """
    # Definir colores y símbolos para diferentes tipos de mensaje
    estilos = {
        "info": ("ℹ️", ""),
        "error": ("❌", ""),
        "success": ("✅", ""),
        "warning": ("⚠️", ""),
        "debug": ("🐛", "")
    }
    
    # Obtener el estilo correspondiente al tipo
    simbolo, color = estilos.get(tipo, estilos["info"])
    
    # Formatear y imprimir el mensaje
    mensaje_formateado = f"{simbolo} {mensaje}"
    print(mensaje_formateado)


def obtener_nombre_usuario() -> str:
    """
    Solicita al usuario que ingrese su nombre y lo valida.
    
    Returns:
        El nombre del usuario validado
        
    Raises:
        KeyboardInterrupt: Si el usuario cancela la entrada
    """
    while True:
        try:
            nombre = input("👤 Ingresa tu nombre: ").strip()
            
            # Validar que el nombre no esté vacío
            if not nombre:
                imprimir_mensaje("El nombre no puede estar vacío. Intenta de nuevo.", "warning")
                continue
            
            # Validar que el nombre solo contenga letras y espacios
            if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", nombre):
                imprimir_mensaje("El nombre solo puede contener letras y espacios.", "warning")
                continue
            
            # Validar longitud del nombre
            if len(nombre) < 2:
                imprimir_mensaje("El nombre debe tener al menos 2 caracteres.", "warning")
                continue
            
            if len(nombre) > 50:
                imprimir_mensaje("El nombre es demasiado largo (máximo 50 caracteres).", "warning")
                continue
            
            return nombre.title()
            
        except KeyboardInterrupt:
            imprimir_mensaje("\nOperación cancelada por el usuario.", "warning")
            sys.exit(0)


def obtener_numero(mensaje: str, tipo: str = "float") -> Union[int, float]:
    """
    Solicita al usuario que ingrese un número y lo valida.
    
    Args:
        mensaje: Mensaje a mostrar al usuario
        tipo: Tipo de número ('int' o 'float')
        
    Returns:
        El número ingresado y validado
        
    Raises:
        KeyboardInterrupt: Si el usuario cancela la entrada
    """
    while True:
        try:
            entrada = input(f"{mensaje}: ").strip()
            
            # Permitir salir con 'q' o 'quit'
            if entrada.lower() in ['q', 'quit', 'salir']:
                raise KeyboardInterrupt
            
            if tipo == "int":
                numero = int(entrada)
            else:
                numero = float(entrada)
            
            return numero
            
        except ValueError:
            imprimir_mensaje(f"Por favor ingresa un número válido ({tipo}).", "error")
        except KeyboardInterrupt:
            imprimir_mensaje("\nOperación cancelada por el usuario.", "warning")
            raise


def limpiar_pantalla() -> None:
    """
    Limpia la pantalla de la consola según el sistema operativo.
    
    Returns:
        None
    """
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')


def pausar(mensaje: str = "Presiona Enter para continuar...") -> None:
    """
    Pausa la ejecución hasta que el usuario presione Enter.
    
    Args:
        mensaje: Mensaje a mostrar antes de pausar
        
    Returns:
        None
    """
    try:
        input(mensaje)
    except KeyboardInterrupt:
        imprimir_mensaje("\nOperación cancelada por el usuario.", "warning")


def validar_email(email: str) -> bool:
    """
    Valida el formato de una dirección de email.
    
    Args:
        email: La dirección de email a validar
        
    Returns:
        True si el email es válido, False en caso contrario
    """
    # Patrón regex para validar email
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None


def formatear_fecha(fecha: datetime, formato: str = "%d/%m/%Y %H:%M:%S") -> str:
    """
    Formatea una fecha según el formato especificado.
    
    Args:
        fecha: Objeto datetime a formatear
        formato: Formato de fecha (por defecto: dd/mm/yyyy hh:mm:ss)
        
    Returns:
        La fecha formateada como string
    """
    try:
        return fecha.strftime(formato)
    except Exception as e:
        imprimir_mensaje(f"Error al formatear fecha: {str(e)}", "error")
        return str(fecha)


def generar_id() -> str:
    """
    Genera un ID único usando UUID.
    
    Returns:
        Un ID único como string
    """
    return str(uuid.uuid4())[:8]


def mostrar_progreso(actual: int, total: int, mensaje: str = "Progreso") -> None:
    """
    Muestra una barra de progreso en la consola.
    
    Args:
        actual: Valor actual del progreso
        total: Valor total del progreso
        mensaje: Mensaje a mostrar junto con la barra
        
    Returns:
        None
    """
    if total <= 0:
        return
    
    porcentaje = (actual / total) * 100
    barra_largo = 30
    completado = int(barra_largo * actual // total)
    barra = "█" * completado + "░" * (barra_largo - completado)
    
    print(f"\r{mensaje}: |{barra}| {porcentaje:.1f}% ({actual}/{total})", end="", flush=True)
    
    if actual == total:
        print()  # Nueva línea al completar


def esperar(segundos: float, mostrar_progreso: bool = True) -> None:
    """
    Espera un número específico de segundos.
    
    Args:
        segundos: Número de segundos a esperar
        mostrar_progreso: Si mostrar una barra de progreso
        
    Returns:
        None
    """
    if mostrar_progreso and segundos > 1:
        for i in range(int(segundos)):
            mostrar_progreso(i + 1, int(segundos), "Esperando")
            time.sleep(1)
        mostrar_progreso(int(segundos), int(segundos), "Esperando")
    else:
        time.sleep(segundos)


def confirmar(mensaje: str = "¿Estás seguro?") -> bool:
    """
    Solicita confirmación al usuario.
    
    Args:
        mensaje: Mensaje de confirmación
        
    Returns:
        True si el usuario confirma, False en caso contrario
    """
    while True:
        respuesta = input(f"{mensaje} (s/n): ").lower().strip()
        
        if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
            return True
        elif respuesta in ['n', 'no']:
            return False
        else:
            imprimir_mensaje("Por favor responde 's' para sí o 'n' para no.", "warning")


def obtener_opcion_menu(opciones: list, mensaje: str = "Selecciona una opción") -> int:
    """
    Muestra un menú de opciones y obtiene la selección del usuario.
    
    Args:
        opciones: Lista de opciones a mostrar
        mensaje: Mensaje a mostrar antes de las opciones
        
    Returns:
        El índice de la opción seleccionada (1-indexed)
        
    Raises:
        KeyboardInterrupt: Si el usuario cancela la entrada
    """
    print(f"\n{mensaje}:")
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    
    while True:
        try:
            seleccion = input(f"Selecciona (1-{len(opciones)}): ").strip()
            
            if seleccion.lower() in ['q', 'quit', 'salir']:
                raise KeyboardInterrupt
            
            numero = int(seleccion)
            
            if 1 <= numero <= len(opciones):
                return numero
            else:
                imprimir_mensaje(f"Por favor selecciona un número entre 1 y {len(opciones)}.", "warning")
                
        except ValueError:
            imprimir_mensaje("Por favor ingresa un número válido.", "error")
        except KeyboardInterrupt:
            imprimir_mensaje("\nOperación cancelada por el usuario.", "warning")
            raise


def formatear_numero(numero: Union[int, float], decimales: int = 2) -> str:
    """
    Formatea un número con separadores de miles y decimales.
    
    Args:
        numero: Número a formatear
        decimales: Número de decimales a mostrar
        
    Returns:
        El número formateado como string
    """
    try:
        if isinstance(numero, int):
            return f"{numero:,}"
        else:
            return f"{numero:,.{decimales}f}"
    except Exception:
        return str(numero)