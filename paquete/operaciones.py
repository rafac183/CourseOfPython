"""
Módulo de Operaciones Matemáticas
================================

Este módulo contiene funciones para realizar operaciones matemáticas básicas
y avanzadas. Todas las funciones incluyen validación de entrada y manejo
de errores apropiado.

Funciones disponibles:
- suma(a, b): Suma dos números
- resta(a, b): Resta dos números
- multiplicacion(a, b): Multiplica dos números
- division(a, b): Divide dos números
- potencia(base, exponente): Calcula la potencia
- raiz_cuadrada(numero): Calcula la raíz cuadrada
- factorial(n): Calcula el factorial de un número
- porcentaje(valor, total): Calcula el porcentaje

Autor: Tu Nombre
Fecha: 2024
Versión: 1.0
"""

import math
from typing import Union, Optional


def suma(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Suma dos números.
    
    Args:
        a: Primer número a sumar
        b: Segundo número a sumar
        
    Returns:
        La suma de los dos números
        
    Raises:
        TypeError: Si los argumentos no son números
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los argumentos deben ser números")
    
    return a + b


def resta(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Resta dos números.
    
    Args:
        a: Número del cual restar
        b: Número a restar
        
    Returns:
        La diferencia entre los dos números
        
    Raises:
        TypeError: Si los argumentos no son números
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los argumentos deben ser números")
    
    return a - b


def multiplicacion(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiplica dos números.
    
    Args:
        a: Primer número a multiplicar
        b: Segundo número a multiplicar
        
    Returns:
        El producto de los dos números
        
    Raises:
        TypeError: Si los argumentos no son números
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los argumentos deben ser números")
    
    return a * b


def division(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Divide dos números.
    
    Args:
        a: Numerador (número a dividir)
        b: Denominador (número por el cual dividir)
        
    Returns:
        El cociente de la división
        
    Raises:
        TypeError: Si los argumentos no son números
        ZeroDivisionError: Si el denominador es cero
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los argumentos deben ser números")
    
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    
    return a / b


def potencia(base: Union[int, float], exponente: Union[int, float]) -> Union[int, float]:
    """
    Calcula la potencia de un número.
    
    Args:
        base: Número base
        exponente: Exponente al cual elevar la base
        
    Returns:
        El resultado de elevar la base al exponente
        
    Raises:
        TypeError: Si los argumentos no son números
        ValueError: Si la base es negativa y el exponente no es entero
    """
    if not isinstance(base, (int, float)) or not isinstance(exponente, (int, float)):
        raise TypeError("Los argumentos deben ser números")
    
    if base < 0 and not isinstance(exponente, int):
        raise ValueError("No se puede calcular la potencia de un número negativo con exponente no entero")
    
    return base ** exponente


def raiz_cuadrada(numero: Union[int, float]) -> float:
    """
    Calcula la raíz cuadrada de un número.
    
    Args:
        numero: Número del cual calcular la raíz cuadrada
        
    Returns:
        La raíz cuadrada del número
        
    Raises:
        TypeError: Si el argumento no es un número
        ValueError: Si el número es negativo
    """
    if not isinstance(numero, (int, float)):
        raise TypeError("El argumento debe ser un número")
    
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    
    return math.sqrt(numero)


def factorial(n: int) -> int:
    """
    Calcula el factorial de un número entero no negativo.
    
    Args:
        n: Número entero no negativo
        
    Returns:
        El factorial del número
        
    Raises:
        TypeError: Si el argumento no es un entero
        ValueError: Si el número es negativo
    """
    if not isinstance(n, int):
        raise TypeError("El argumento debe ser un entero")
    
    if n < 0:
        raise ValueError("No se puede calcular el factorial de un número negativo")
    
    if n == 0 or n == 1:
        return 1
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    
    return resultado


def porcentaje(valor: Union[int, float], total: Union[int, float]) -> float:
    """
    Calcula el porcentaje que representa un valor de un total.
    
    Args:
        valor: El valor del cual calcular el porcentaje
        total: El valor total (100%)
        
    Returns:
        El porcentaje como un número decimal
        
    Raises:
        TypeError: Si los argumentos no son números
        ValueError: Si el total es cero
    """
    if not isinstance(valor, (int, float)) or not isinstance(total, (int, float)):
        raise TypeError("Los argumentos deben ser números")
    
    if total == 0:
        raise ValueError("El total no puede ser cero")
    
    return (valor / total) * 100


def redondear(numero: Union[int, float], decimales: int = 2) -> float:
    """
    Redondea un número a un número específico de decimales.
    
    Args:
        numero: Número a redondear
        decimales: Número de decimales (por defecto 2)
        
    Returns:
        El número redondeado
        
    Raises:
        TypeError: Si los argumentos no son del tipo correcto
        ValueError: Si el número de decimales es negativo
    """
    if not isinstance(numero, (int, float)):
        raise TypeError("El número debe ser un valor numérico")
    
    if not isinstance(decimales, int):
        raise TypeError("El número de decimales debe ser un entero")
    
    if decimales < 0:
        raise ValueError("El número de decimales no puede ser negativo")
    
    return round(numero, decimales)


def es_par(numero: int) -> bool:
    """
    Verifica si un número entero es par.
    
    Args:
        numero: Número entero a verificar
        
    Returns:
        True si el número es par, False si es impar
        
    Raises:
        TypeError: Si el argumento no es un entero
    """
    if not isinstance(numero, int):
        raise TypeError("El argumento debe ser un entero")
    
    return numero % 2 == 0


def es_primo(numero: int) -> bool:
    """
    Verifica si un número entero es primo.
    
    Args:
        numero: Número entero a verificar
        
    Returns:
        True si el número es primo, False en caso contrario
        
    Raises:
        TypeError: Si el argumento no es un entero
        ValueError: Si el número es menor que 2
    """
    if not isinstance(numero, int):
        raise TypeError("El argumento debe ser un entero")
    
    if numero < 2:
        return False
    
    if numero == 2:
        return True
    
    if numero % 2 == 0:
        return False
    
    # Verificar divisores impares hasta la raíz cuadrada
    for i in range(3, int(math.sqrt(numero)) + 1, 2):
        if numero % i == 0:
            return False
    
    return True