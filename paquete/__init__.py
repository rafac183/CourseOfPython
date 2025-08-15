"""
Paquete de Utilidades y Operaciones Matemáticas
==============================================

Este paquete contiene módulos para realizar operaciones matemáticas
y utilidades de interacción con el usuario.

Módulos incluidos:
- operaciones: Funciones matemáticas básicas y avanzadas
- utilidades: Funciones de utilidad para interacción con el usuario

Autor: Tu Nombre
Fecha: 2024
Versión: 1.0
"""

# Importar funciones principales para facilitar el acceso
from .operaciones import (
    suma,
    resta,
    multiplicacion,
    division,
    potencia,
    raiz_cuadrada,
    factorial,
    porcentaje,
    redondear,
    es_par,
    es_primo
)

from .utilidades import (
    imprimir_mensaje,
    obtener_nombre_usuario,
    obtener_numero,
    limpiar_pantalla,
    pausar,
    validar_email,
    formatear_fecha,
    generar_id,
    mostrar_progreso,
    esperar,
    confirmar,
    obtener_opcion_menu,
    formatear_numero
)

# Información del paquete
__version__ = "1.0.0"
__author__ = "Tu Nombre"
__email__ = "tu.email@ejemplo.com"

# Lista de todas las funciones disponibles
__all__ = [
    # Operaciones matemáticas
    'suma',
    'resta', 
    'multiplicacion',
    'division',
    'potencia',
    'raiz_cuadrada',
    'factorial',
    'porcentaje',
    'redondear',
    'es_par',
    'es_primo',
    
    # Utilidades
    'imprimir_mensaje',
    'obtener_nombre_usuario',
    'obtener_numero',
    'limpiar_pantalla',
    'pausar',
    'validar_email',
    'formatear_fecha',
    'generar_id',
    'mostrar_progreso',
    'esperar',
    'confirmar',
    'obtener_opcion_menu',
    'formatear_numero'
]
